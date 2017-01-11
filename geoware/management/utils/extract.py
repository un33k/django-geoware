import os, sys, re

def between_tags_reverse(string, stag='', etag=''):
    """
    Finds the first substrings wrapped by stag and etag within a string (in reverse).
    Does not include start/end. Scans from the end of the string

    @type string: str
    @param string: The string to search within.
    @type start: str
    @param stag: The starting tag.
    @type end: str
    @param etag: The ending tag.
    @rtype: string
    @return: The first matched (in reverse) substring found between start<>end or an empty string.
    """
    s = string.rfind(stag) if stag else 0
    e = string.rfind(etag) if etag else len(string)
    if s < 0 or e < 0: return ''
    string = string[s+len(stag):e]
    return string


def between_tags(string, stag='', etag=''):
    """
    Finds the first substrings wrapped by stag and etag within a string.
    Does not include start/end. Scans from the start of string

    @type string: str
    @param string: The string to search within.
    @type start: str
    @param stag: The starting tag.
    @type end: str
    @param etag: The ending tag.
    @rtype: string
    @return: The first matched substring found between start<>end or an empty string.
    """
    s = string.find(stag) if stag else 0
    e = string.find(etag) if etag else len(string)
    if s < 0 or e < 0: return ''
    string = string[s+len(stag):e]
    return string


def between_tags_all(string, stag='', etag=''):
    """
    Iteratively find all substrings wrapped by stag and etag within a string.
    Does not include start/end. Scans from the start of string

    @type string: str
    @param string: The string to search within.
    @type string: str
    @param stag: The starting tag.
    @type end: str
    @param etag: The ending tag.
    @rtype: list
    @return: A list of every occurrence of start<>end in the string, or an an empty list
    """
    result = []
    while True:
        s = string.find(stag) if stag else 0
        e = string.find(etag) if etag else len(string)
        if s < 0 or e < 0: break
        result.append(string[s+len(stag):e])
        string = string[e+len(etag):]
    return result


def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_extra_spaces(data):
    p = re.compile(r'\s+')
    return p.sub(' ', data)


