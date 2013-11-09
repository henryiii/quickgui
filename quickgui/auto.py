#!/usr/bin/env python

# Importing functions
def _init_qt():
    import quickgui.quickqt as quick
    _init_any(quick)
def _init_dialog():
    import quickgui.quickdialog as quick
    _init_any(quick)
def _init_simple():
    import quickgui.simple as quick
    _init_any(quick)
def _init_tkinter():
    import quickgui.quicktkinter as quick
    _init_any(quick)

# Loading process
def _init_any(quick):
    global ask_yn
    ask_yn = quick.ask_yn

# Do the loading on import
try:
    _init_qt()
except ImportError:
    try:
        _init_tkinter()
    except ImportError:
        try:
            _init_dialog()
        except ImportError:
            _init_simple()
