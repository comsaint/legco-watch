"""
Some utilities for working with spiders
"""
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from itertools import izip_longest
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
import magic
import subprocess
import pydocx
import os
import lxml.etree
import lxml.html
from lxml.html import HTMLParser
from lxml.html.clean import clean_html,Cleaner
from logging import raiseExceptions


HTML = 1
DOC = 2
DOCX = 3
PDF = 4
#ZIP = 5

def list_spiders():
    settings = get_project_settings()
    crawler = Crawler(settings)
    return crawler.spiders.list()


def check_file_type(filepath, as_string=False):
    filetype = magic.from_file(filepath)
    if not filetype:
        # Filetype Could Not Be Determined
        return None
    elif filetype == 'empty':
        # Filetype Could Not Be Determined (file looks empty)
        return None
    elif filetype == 'very short file (no magic)':
        # Filetype Could Not Be Determined (very short file)
        return None
    elif "Microsoft Office Word" in filetype:
        return DOC if not as_string else 'DOC'
    elif filetype[0:4] == 'HTML':
        return HTML if not as_string else 'HTML'
    elif filetype == 'Microsoft Word 2007+':
        return DOCX if not as_string else 'DOCX'
    elif 'PDF' in filetype:
        return PDF if not as_string else 'PDF'
    elif filetype[0:3] == 'Zip':
        # a lot of hansards are found to be in ZIP format, but can be opened with python-docx
        return DOCX if not as_string else 'DOCX'
    else:
        # some other filetype that we don't account for
        return None


def doc_to_html(filepath, overwrite=False):
    """
    Converts a doc file to in-memory html string.

    :param filepath: full filepath to the file to convert
    :return: unicode string
    """
    html_file = '{}.html'.format(filepath)
    if not os.path.exists(html_file) or overwrite:
        cmd = ['abiword', '--to=html', '--to-name=fd://1', filepath]
        try:
            res = subprocess.check_output(cmd)
        except:
            return None
        with open(html_file, 'wb') as tmp:
            tmp.write(res)
    else:
        with open(html_file, 'rb') as tmp:
            res = tmp.read()
    return res.decode('utf-8')


def docx_to_html(filepath, overwrite=False):
    """
    Converts docx file to in-memory html string

    :param filepath: full path to the file to convert
    :return: unicode string
    """
    html_file = '{}.html'.format(filepath)
    if not os.path.exists(html_file) or overwrite:
        #res = pydocx.docx2html(filepath)
        res = pydocx.PyDocX.to_html(filepath)
        with open(html_file, 'wb') as tmp:
            tmp.write(res.encode('utf-8'))
    else:
        with open(html_file, 'rb') as tmp:
            res = tmp.read().decode('utf-8')
    return res


def get_file_path(rel_path):
    """
    Given a relative path for a file downloaded by scrapy, get the absolute path
    """
    files_folder = getattr(settings, 'SCRAPY_FILES_PATH', None)
    if files_folder is None:
        raise ImproperlyConfigured("No SCRAPY_FILES_PATH defined")

    file_path = os.path.join(files_folder, rel_path)
    if not os.path.exists(file_path):
        raise RuntimeError("Could not find file at {}".format(file_path))

    return file_path


def to_string(obj, encoding='utf-8'):
    """
    Converts unicode objects to strings, and returns strings directly
    """
    if isinstance(obj, basestring):
        if isinstance(obj, unicode):
            obj = obj.encode(encoding)
    return obj


def to_unicode(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks
    """
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def utf2html(ustring):
    ustring = ustring.replace('\r\n','<br><br />')
    ustring = ustring.replace('\n','<br><br />')
    ustring = ustring.replace('\t','    ')
    return ustring

def merge_docx(docx_list=None, out_htmlpath=None):
    """
    docx_list is a list of strings which contains the (absolute) path of DOC/DOCX files to be merged.
    MERGE_DOCX() will follow the index order of docx_list for appending.
    Returns the HTML file as string. 
    If OUT_HTMLPATH is given, write the HTML file out as well.
    """
    if docx_list is None:
        return None
    
    cleaner = Cleaner()
    parser = HTMLParser(encoding='utf-8')
    html_list = []
    for path in docx_list:
        try:
            tmp_html = pydocx.PyDocX.to_html(path)
            html_list.append(cleaner.clean_html(lxml.html.fromstring(tmp_html, parser=parser)))
        except:
            #'MalformedDocxException'
            try:
                # Pretend it is a html
                html_file = '{}.html'.format(path)
                with open(html_file, 'rb') as tmp:
                    tmp_html = tmp.read()
                tmp_html = tmp_html.decode('utf-8')
                html_list.append(cleaner.clean_html(lxml.html.fromstring(tmp_html, parser=parser)))
            except:
                # Cannot convert
                continue
    
    #print html_list
    if len(html_list)>1:
        #Append element at the end of first body
        main_body = html_list[0].xpath('./body')[0]
        for tree in html_list[1:]:
            elem_list = tree.xpath('./body/*')
            for elem in elem_list:
                main_body.append(elem)
    elif len(html_list)==1:
        main_body = html_list[0].xpath('./body')[0]
    else:
        try:
            main_body = html_list[0].xpath('./body')[0]
        except IndexError:
            # no body content. Most likely just an image/appendix
            return None
    
    # Convert ElementTree back to string
    # in this way we will lose the 'style' info in html_list[0][0], which is usually in header,
    # but not sure if it will cause any differences to parser later on. Probably not.
    html_str = lxml.etree.tostring(main_body)
    
    if out_htmlpath is not None:
        with open(out_htmlpath, 'wb') as tmp:
            tmp.write(html_str.encode('utf-8'))
                
    return html_str
        
