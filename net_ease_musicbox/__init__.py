#!/usr/bin/env python
# encoding: UTF-8

"""
网易云音乐 Entry
"""

import os
from menu import Menu


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def start():
    Menu().start()

if __name__ == "__name__":
    Menu.start()
