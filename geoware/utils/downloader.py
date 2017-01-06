import os
import time
import mmap
import requests
import zipfile
import tarfile
import logging
import resource
import progressbar
from urllib.parse import urljoin

from django.utils.translation import ugettext as _

from .. import defaults as defs

logger = logging.getLogger('geoware.downloader')


class FileDownloader(object):
    """
    Class to download files.
    """
    cache_dir = defs.GEOWARE_DATA_DIR
    response_headers = None

    def __init__(self, download_type=None):
        if download_type is None:
            raise Exception(_('Improperly Use! Download Type is required'))
        self.download_type = download_type
        if not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)

    def get_file_path(self, url):
        """
        Returns a local path of a file given a URL.
        """
        file_name = os.path.basename(url)
        local_file_path = os.path.join(self.cache_dir, file_name)
        return local_file_path

    def get_url(self):
        """
        Return the related URL for download.
        """
        base_url = defs.GEOWARE_FILE_DICT[self.download_type]['url']
        file_name = defs.GEOWARE_FILE_DICT[self.download_type]['filename']
        url = urljoin(base_url, file_name)
        return url

    def is_file_up2date(self, url):
        """
        Returns True if local and remote files are not the same.
        """
        up2date = False
        local_path = self.get_file_path(url)
        if os.path.isfile(local_path):
            response_headers = self.get_remote_file_info(url)
            if response_headers:
                ltime = time.gmtime(os.path.getmtime(local_path))
                lsize = os.path.getsize(local_path)
                rtime = time.strptime(response_headers['last-modified'].strip(), '%a, %d %b %Y %H:%M:%S %Z')
                rsize = int(response_headers['content-length'].strip())
                if ltime >= rtime or lsize == rsize:
                    up2date = True
        return up2date

    def get_remote_file_info(self, url):
        """
        Returns the response headers for URL.
        """
        if not self.response_headers:
            resp = requests.head(url)
            if resp.status_code == requests.codes.ok:
                self.response_headers = resp.headers
        return self.response_headers

    def get_remote_file_size(self, url):
        """
        Returns the remote file size.
        """
        headers = self.get_remote_file_info(url)
        size = int(headers['content-length'].strip())
        return size

    def get_progress_widgets(self, url):
        """
        Returns the progress widgets for a file download.
        """
        format_custom_text = progressbar.FormatCustomText(
            'Fetching [ %(file)s ] :: ', dict(file=os.path.basename(url)),
        )

        widgets = [
            format_custom_text,
            progressbar.ETA(),
            progressbar.Percentage(),
            progressbar.Bar(),
        ]
        return widgets

    def download(self, url, force=False):
        """
        Returns the path to a newly downloaded, or an unchanged file.
        """
        file_path = self.get_file_path(url)
        up2date = self.is_file_up2date(url)
        if up2date and not force:
            logger.info(_('DOWNLOAD.FILE.UP_TO_DATE'))
            logger.info('{path}'.format(path=file_path))
            return file_path

        logger.info(_('DOWNLOAD.FILE.DOWNLOADING'))
        logger.info('{path}'.format(path=file_path))

        resp = requests.get(url, stream=True)
        if resp.status_code != requests.codes.ok:
            logger.error(_('DOWNLOAD.FILE.DOWNLOAD_FAILED'))
            logger.error('({code})'.format(code=resp.status_code))
            return None

        size_so_far = 0
        chunk_size = 4096
        total_size = int(self.get_remote_file_info(url)['content-length'].strip())
        widgets = self.get_progress_widgets(url)

        with progressbar.ProgressBar(max_value=total_size, widgets=widgets) as pbar:
            with open(file_path, 'wb') as aFile:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    size_so_far += len(chunk)
                    if chunk:
                        aFile.write(chunk)
                    pbar.update(size_so_far)

        logger.info(_('DOWNLOAD.FILE.DOWNLOAD_COMPLETED'))
        logger.info('{path}'.format(path=file_path))

        return file_path

    def extract(self, file_path):
        """
        Extract a compressed file.
        """
        extracted = True
        filetype = file_path.split('?')[0]
        if filetype.endswith('.txt'):
            return extracted

        if filetype.endswith('.zip'):
            extractor, mode = zipfile.ZipFile, 'r'
        elif filetype.endswith('.tar.gz') or file_path.endswith('.tgz'):
            extractor, mode = tarfile.open, 'r:gz'
        elif filetype.endswith('.tar.bz2') or file_path.endswith('.tbz'):
            extractor, mode = tarfile.open, 'r:bz2'
        else:
            logger.warning(_('DOWNLOAD.FILE.EXTRACT.UNSUPPORTED_FILE'))
            logger.warning('{path}'.format(path=file_path))
            extracted = False
            return extracted

        cwd = os.getcwd()
        os.chdir(self.cache_dir)
        try:
            efile = extractor(file_path, mode)
            try:
                efile.extractall()
            finally:
                efile.close()
        finally:
            os.chdir(cwd)

        logger.info(_('DOWNLOAD.FILE.EXTRACT.COMPLETE'))
        logger.info('{path}'.format(path=file_path))

        return extracted

# def parse_file(filepath):
#     """ Return a file one line at a time """

#     for line in open(filepath, 'r'):
#         line = line.strip()
#         if len(line) < 1 or line.strip()[0] == '#':
#             continue
#         yield [e.strip() for e in line.split('\t')]


# def parse_data(data):
#     """ Return a file one line at a time """

#     for line in data:
#         line = line.strip()
#         if len(line) < 1 or line.strip()[0] == '#':
#             continue
#         yield [e.strip() for e in line.split('\t')]


# def load_file_mmap(filepath, skip_char="#"):
#     """ Using memory map, open and read a file """

#     total_lines = 0
#     data = []
#     with open(filepath, "r") as f:
#         m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
#         while True:
#             line = m.readline()
#             if line == "": break
#             if line.lstrip()[0] == skip_char:
#                 continue
#             total_lines += 1
#             data.append(line)
#         m.close()
#     return data, total_lines


# def parse_data_mmap(filepath, skip_char='#'):
#     """ Return a file one line at a time using mmap """

#     with open(filepath, "r") as f:
#         m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
#         while True:
#             line = m.readline()
#             if line.lstrip()[0] == skip_char:
#                 continue
#             yield [e.strip() for e in line.split('\t')]


