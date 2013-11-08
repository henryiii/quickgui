#!/usr/bin/env python

_backend = None

# Init logic

def init(system=None):
    if system is None or system.lower() == 'auto':
        _init_auto()
    elif system.lower() == 'ipython':
        _init_ipython()
    elif system.lower() == 'simple':
        _init_simple()
    elif system.lower() == 'curses' or system.lower() == 'dialog':
        _init_dialog()
    elif system.lower() == 'tkinter':
        _init_tkinter()
    elif system.lower() == 'qt':
        _init_qt()
    else:
        raise ImportError()

def _init_auto():
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



# Importing functions
def _init_qt():
    raise ImportError()
def _init_ipython():
    raise ImportError()
def _init_dialog():
    import quickgui.backends.quickdialog as quick
    _init_any(quick)
    global _backend
    _backend = 'dialog'
def _init_simple():
    import quickgui.backends.simple as quick
    _init_any(quick)
    global _backend
    _backend = 'simple'
def _init_tkinter():
    raise ImportError()

# Loading process
def _init_any(quick):
    global ask_yn
    ask_yn = quick.ask_yn

