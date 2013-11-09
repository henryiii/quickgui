#!/usr/bin/env python

from .. import quickqt, quicktkinter

guis = [quickqt, quicktkinter]

def test_yes():
    for gui in guis:
        assert True == gui.ask_yn('Answer yes')


def test_no():
    for gui in guis:
        assert False == gui.ask_yn('Answer no')

