#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import requests
import pyperclip
from urllib.parse import urlparse

def find_file_no(file_name):
    rel_files = [i.split('.')[0] for i in os.listdir(file_name) if file_name in i]
    rel_files.sort()
    if file_name not in rel_files:
        return file_name
    else:
        for index in range(1, 200):
            query_name = file_name+str(index)
            if query_name not in rel_files:
                return query_name
    return 'ERROR'


def main(player_name):
    file_name = find_file_no(player_name)
    image_link = pyperclip.paste()
    response = requests.get(image_link)
    new_file_ext = response.headers['Content-Type'].split('/')[1]
    with open(player_name + '/' + file_name + "." + new_file_ext, "wb") as fout:
        fout.write(response.content)
        fout.close()

if __name__=='__main__':
    # print(os.path.dir(os.getcwd()))
    main(sys.argv[1])
