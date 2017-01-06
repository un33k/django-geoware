import os
import sys
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
    url = None
    file_name = None

    def __init__(self, stdout=None):
        self.stdout = stdout or sys.stdout
        if not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)

    def _get_file_path(self):
        """
        Returns a local path of a file given a URL.
        """
        file_name = os.path.basename(self.url)
        local_file_path = os.path.join(self.cache_dir, file_name)
        return local_file_path

    def _is_file_up2date(self):
        """
        Returns True if local and remote files are not the same.
        """
        up2date = False
        local_path = self._get_file_path()
        if os.path.isfile(local_path):
            response_headers = self._get_remote_file_info()
            if response_headers:
                ltime = time.gmtime(os.path.getmtime(local_path))
                lsize = os.path.getsize(local_path)
                rtime = time.strptime(response_headers['last-modified'].strip(), '%a, %d %b %Y %H:%M:%S %Z')
                rsize = int(response_headers['content-length'].strip())
                if ltime >= rtime or lsize == rsize:
                    up2date = True
        return up2date

    def _get_remote_file_info(self):
        """
        Returns the response headers for URL.
        """
        if not self.response_headers:
            resp = requests.head(self.url)
            if resp.status_code == requests.codes.ok:
                self.response_headers = resp.headers
        return self.response_headers

    def _get_remote_file_size(self):
        """
        Returns the remote file size.
        """
        headers = self._get_remote_file_info()
        size = int(headers['content-length'].strip())
        return size

    def _get_progress_widgets(self):
        """
        Returns the progress widgets for a file download.
        """
        format_custom_text = progressbar.FormatCustomText(
            'Fetching [ %(file)s ] :: ', dict(file=os.path.basename(self.url)),
        )

        widgets = [
            format_custom_text,
            progressbar.ETA(),
            progressbar.Percentage(),
            progressbar.Bar(),
        ]
        return widgets

    def stage(self, file_type=None):
        """
        Stage the next file download.
        """
        file_info = defs.GEOWARE_FILE_DICT.get(file_type)
        if not file_info:
            raise Exception("Invalid File Type {type}".format(type=file_type))
        self.url = urljoin(file_info['url'], file_info['filename'])
        self.file_name = os.path.basename(self.url)

    def download(self, force=False):
        """
        Returns the path to a newly downloaded, or an unchanged file.
        """
        file_path = self._get_file_path()
        up2date = self._is_file_up2date()
        if up2date and not force:
            self.stdout.write("Fetched file from cache ({file}).\n".format(file=self.file_name))
            return file_path

        self.stdout.write("Downloading file ({file}).\n".format(file=self.file_name))

        resp = requests.get(self.url, stream=True)
        if resp.status_code != requests.codes.ok:
            self.stdout.write("Download failed with ({status}).\n".format(code=resp.status_code))
            return None

        size_so_far = 0
        chunk_size = 4096
        total_size = self._get_remote_file_size()
        widgets = self._get_progress_widgets()

        with progressbar.ProgressBar(max_value=total_size, widgets=widgets) as pbar:
            with open(file_path, 'wb') as aFile:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    size_so_far += len(chunk)
                    if chunk:
                        aFile.write(chunk)
                    pbar.update(size_so_far)

        self.stdout.write("Fetched file from server ({file}).\n".format(file=self.file_name))
        return file_path

    def extract(self):
        """
        Extract a compressed file.
        """
        file_path = self._get_file_path()
        filetype = file_path.split('?')[0]
        if filetype.endswith('.txt'):
            return file_path

        if filetype.endswith('.zip'):
            extractor, mode = zipfile.ZipFile, 'r'
        elif filetype.endswith('.tar.gz') or file_path.endswith('.tgz'):
            extractor, mode = tarfile.open, 'r:gz'
        elif filetype.endswith('.tar.bz2') or file_path.endswith('.tbz'):
            extractor, mode = tarfile.open, 'r:bz2'
        else:
            self.stdout.write("Unable to extract file ({file}).\n".format(file=os.path.basename(self.url)))
            return None

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

        self.stdout.write("Extracted file ({file}).\n".format(file=self.file_name))
        return file_path

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


