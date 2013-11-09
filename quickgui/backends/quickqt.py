#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, division

import sys

try:
    from PySide import QtGui
except ImportError:
    try:
        from PyQt5 import QtGui
    except ImportError:
        from PyQt4 import QtGui

TITLE='QuickGUI'

root = QtGui.QApplication([sys.argv[0]])

def ask_yn(msg='Answer yes or no',title=TITLE, **kargs):
    quest = QtGui.QMessageBox()
    quest.setWindowTitle(title)
    quest.setText(msg)
    quest.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    quest.setDefaultButton(QtGui.QMessageBox.Yes)
    ans = quest.exec_()
    return ans == QtGui.QMessageBox.Yes
