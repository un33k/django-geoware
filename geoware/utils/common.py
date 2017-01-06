import os
import sys

from django.utils.encoding import smart_str


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


def get_float(item, index):
    """
    Given an record list & an index, it returns a float or 0.0.
    """
    value = 0.0
    try:
        value = float(smart_str(item[index]))
    except:
        pass
    return value


def get_int(item, index):
    """
    Given an record list & an index, it returns an int or 0.
    """
    value = 0
    try:
        value = int(smart_str(item[index]))
    except:
        pass
    return value


def get_str(item, index):
    """
    Given an record list & an index, it returns a str or ''.
    """
    value = ''
    try:
        value = smart_str(item[index])
    except:
        pass
    return value
