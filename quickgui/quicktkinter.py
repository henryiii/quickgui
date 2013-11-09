#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, division

try: # Py2
    import Tkinter as tk
    import tkMessageBox as tkmess
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as tkmess

TITLE='QuickGUI'

def ask_yn(msg='Answer yes or no',title=TITLE, **kargs):
    root = tk.Tk()
    root.withdraw()
    ans = tkmess.askyesno(title,msg)
    root.destroy()
    return ans
