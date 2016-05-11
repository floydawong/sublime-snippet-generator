# coding:utf8
# Author:Floyda

import os
import re

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

KEYWORD_FILE_PATH = r"./matlab_function_list.txt"
OUTPUT_DIR_PATH = r"./snippet"
SUFFIX = "matlab"

SNIPPET_TEMPLATE = """\
<snippet>
    <content><![CDATA[
%s
]]></content>
    <tabTrigger>%s</tabTrigger>
    <scope>source.%s</scope>
    <description>%s</description>
</snippet>\
"""


def get_snippet_tempate(word):
    return SNIPPET_TEMPLATE % (word, word, SUFFIX, word)


def get_word_list(path):
    rlist = set([])
    with open(path, 'r') as fp:
        for word in fp.readlines():
            rlist.add(re.sub('\n', '', word))
    return rlist


def generate_snippet(word):
    if not os.path.exists(OUTPUT_DIR_PATH): os.mkdir(OUTPUT_DIR_PATH)

    file_name = word + '.sublime-snippet'
    path = os.path.join(OUTPUT_DIR_PATH, file_name)
    with open(path, 'w') as fp:
        fp.write(get_snippet_tempate(word))

    print "%s is OK ..." % file_name


if __name__ == '__main__':
    for word in get_word_list(KEYWORD_FILE_PATH):
        generate_snippet(word)

    print "OK"
