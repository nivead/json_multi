#!/usr/bin/env python3
'''
parse multi-object json docs
@author: nivead
'''

import json

def parse(jdata):
    '''
    function to parse string, seperate out json objects and add to list
    '''
    segment = ''
    jlist = []

    for chunk in jdata:
        segment += chunk
        try:
            data = json.loads(segment)
            if data:
                jlist.append(data)
                segment = ""
        except ValueError:
            pass
    return jlist
