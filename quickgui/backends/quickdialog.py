#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, division

import dialog

TITLE='QuickGUI'

mygui = dialog.Dialog()

def ask_yn(msg='Answer yes or no',title=TITLE, **kargs):
    global mygui
    mygui.setBackgroundTitle(title)
    return mygui.yesno(msg)
