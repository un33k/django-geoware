import os
import time
import mmap
import requests
import zipfile
import tarfile
import logging
import resource
import progressbar
from django.utils.translation import ugettext as _

from .. import defaults

logger = logging.getLogger('geoware.downloader')

__all__ = ["file_download", "file_extract", "parse_data", "parse_file", "load_file_mmap", "parse_data_mmap"]


def file_download(url='', to_dir=defaults.GEOWARE_DATA_DIR, extract=False, force=False):
    """ Download a file if forced or newer found """

    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    lfile = os.path.join(to_dir, os.path.basename(url))
    resp = requests.head(url)
    if resp.status_code != requests.codes.ok:
        return False, {'name': '', 'type': '', 'updated': False}
    rtime = time.strptime(resp.headers['last-modified'].strip(), '%a, %d %b %Y %H:%M:%S %Z')
    rsize = int(resp.headers['content-length'].strip())
    rtype = resp.headers['content-type'].strip()

    if os.path.exists(lfile) and not force:
        ltime = time.gmtime(os.path.getmtime(lfile))
        lsize = os.path.getsize(lfile)
        if ltime >= rtime and lsize == rsize:
            logger.debug(_('File up2date ({0})'.format(url)))
            return True, {'name': lfile, 'type': rtype, 'updated': False}

    logger.debug(_('File is being dowloaded. ({0})'.format(url, to_dir)))

    fname = os.path.basename(url)
    fname = (fname[:10] + (fname[10:] and '..'))
    widgets = [
        '{0}|File Size: {1} kB|'.format("|Fetching: {0}".format(fname.rjust(12)), str(rsize/1024).rjust(7)),
        progressbar.ETA(),
        '|Done:',
        progressbar.Percentage(),
        progressbar.Bar(),
    ]

    resp = requests.get(url)
    if resp.status_code != requests.codes.ok:
        return True, {'name': lfile, 'type': rtype, 'updated': False}

    chunk_size=4096
    total_size = rsize
    size_so_far = 0
    progress = progressbar.ProgressBar(maxval=total_size, widgets=widgets)

    with open(lfile, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=chunk_size):
            size_so_far += len(chunk); progress.update(size_so_far)
            if chunk:
                f.write(chunk)

    logger.debug(_('Download complete. ({0})'.format(url, to_dir)))

    if extract:
        file_extract(lfile)
        logger.debug(_('File extracted'))
    return True, {'name': lfile, 'type': rtype, 'updated': True}


def file_extract(filepath, to_dir=defaults.GEOWARE_DATA_DIR):
    """ Extract a compressed file """

    filetype = filepath.split('?')[0]
    if filetype.endswith('.zip'):
        extractor, mode = zipfile.ZipFile, 'r'
    elif filetype.endswith('.tar.gz') or filepath.endswith('.tgz'):
        extractor, mode = tarfile.open, 'r:gz'
    elif filetype.endswith('.tar.bz2') or filepath.endswith('.tbz'):
        extractor, mode = tarfile.open, 'r:bz2'
    elif not filetype.endswith('.txt'):
        logger.warning(_("Could not extract unsupported file. ({0})".format(filepath)))
        return False
    else:
        return True

    cwd = os.getcwd()
    os.chdir(to_dir)
    try:
        efile = extractor(filepath, mode)
        try: efile.extractall()
        finally: efile.close()
    finally:
        os.chdir(cwd)

    logger.debug('Extracted ({0})'.format(filepath))
    return True


def parse_file(filepath):
    """ Return a file one line at a time """

    for line in open(filepath, 'r'):
        line = line.strip()
        if len(line) < 1 or line.strip()[0] == '#':
            continue
        yield [e.strip() for e in line.split('\t')]


def parse_data(data):
    """ Return a file one line at a time """

    for line in data:
        line = line.strip()
        if len(line) < 1 or line.strip()[0] == '#':
            continue
        yield [e.strip() for e in line.split('\t')]


def load_file_mmap(filepath, skip_char="#"):
    """ Using memory map, open and read a file """

    total_lines = 0
    data = []
    with open(filepath, "r") as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        while True:
            line = m.readline()
            if line == "": break
            if line.lstrip()[0] == skip_char:
                continue
            total_lines += 1
            data.append(line)
        m.close()
    return data, total_lines


def parse_data_mmap(filepath, skip_char='#'):
    """ Return a file one line at a time using mmap """

    with open(filepath, "r") as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        while True:
            line = m.readline()
            if line.lstrip()[0] == skip_char:
                continue
            yield [e.strip() for e in line.split('\t')]


