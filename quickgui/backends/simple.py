#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, division


# Fix Python 2.x.
try: input = raw_input
except NameError: pass

TITLE='QuickGUI'

def ask_yn(msg='Answer yes or no',title=TITLE,default=True,
        prompt=' [Y/n]? ', **kargs):
    print(title)
    val = input(msg+prompt)
    if val=='':
        return default
    elif val.lower()[0] == 'y':
        return True
    elif val.lower()[0] == 'n':
        return False
    else:
        return None
