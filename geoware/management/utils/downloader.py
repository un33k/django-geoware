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
from urllib.parse import urlparse

from django.utils.translation import ugettext as _

from ... import defaults as defs

logger = logging.getLogger('geoware.downloader')


class FileDownloader(object):
    """
    Class to download files.
    """
    cache_dir = defs.GEOWARE_DATA_DIR
    response_headers = None

    def __init__(self, stdout=None):
        self.stdout = stdout or sys.stdout
        if not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)

    def _is_file_up2date(self):
        """
        Returns True if local and remote files are not the same.
        """
        up2date = False
        local_path = self.downloaded_file_path
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
            resp = requests.head(self.remote_file_path)
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
            'Fetching [ %(file)s ] :: ', dict(file=self.remote_file_name),
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
        self.file_info = defs.GEOWARE_FILE_DICT.get(file_type)
        if not self.file_info:
            raise Exception("Invalid File Type {type}".format(type=file_type))

    def download(self, force=False):
        """
        Returns the path to a newly downloaded, or an unchanged file.
        """
        up2date = self._is_file_up2date()
        if up2date and not force:
            self.stdout.write("Fetched file from cache ({file})\n".format(file=self.downloaded_file_name))
            return self.downloaded_file_path

        self.stdout.write("Downloading file ({file}) from ({host})\n".format(
            file=self.remote_file_name, host=urlparse(self.remote_file_path).hostname))

        resp = requests.get(self.remote_file_path, stream=True)
        if resp.status_code != requests.codes.ok:
            self.stdout.write("Download failed with ({status})\n".format(code=resp.status_code))
            return None

        size_so_far = 0
        chunk_size = 4096
        total_size = self._get_remote_file_size()
        widgets = self._get_progress_widgets()

        with progressbar.ProgressBar(max_value=total_size, widgets=widgets) as pbar:
            with open(self.downloaded_file_path, 'wb') as aFile:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    size_so_far += len(chunk)
                    if chunk:
                        aFile.write(chunk)
                    pbar.update(size_so_far)

        self.stdout.write("Fetched file from server ({file})\n".format(file=self.downloaded_file_name))
        return self.downloaded_file_path

    def extract(self):
        """
        Extract a compressed file.
        """
        file_path = self.downloaded_file_path
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
            self.stdout.write("Unable to extract file ({file})\n".format(file=self.downloaded_file_name))
            return None

        cwd = os.getcwd()
        os.chdir(self.cache_dir)
        try:
            efile = extractor(file_path, mode)
            try:
                efile.extractall()
            except Exception as err:
                self.stdout.write("File failed to extract fully\n({file})\n".format(file=self.downloaded_file_path))
                return
            finally:
                efile.close()
        except Exception as err:
            self.stdout.write("Unable to extract. Bad or corrupted file\n({file})\n".format(file=self.downloaded_file_path))
            return
        finally:
            os.chdir(cwd)

        self.stdout.write("Extracted file ({file})\n".format(file=self.extracted_file_name))
        return self.extracted_file_path

    @property
    def remote_file_name(self):
        return self.file_info['remote']

    @property
    def remote_file_path(self):
        return urljoin(self.file_info['url'], self.file_info['remote'])

    @property
    def downloaded_file_name(self):
        return self.remote_file_name

    @property
    def downloaded_file_path(self):
        return os.path.abspath(os.path.join(self.cache_dir, self.remote_file_name))

    @property
    def extracted_file_name(self):
        return self.file_info['local']

    @property
    def extracted_file_path(self):
        return os.path.abspath(os.path.join(self.cache_dir, self.extracted_file_name))
