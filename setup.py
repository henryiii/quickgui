#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='QuickGUI',
      version='0.0.1',
      provides=['quickgui'],
      description='Simple and fast gui with several backends.',
      author='Henry Schreiner III',
      author_email='henryiii@physics.utexas.edu',
      packages=['quickgui','quickgui.backends'],
      )
