#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import atdlib

def main():
    print(atdlib)
    print(atdlib.deos)
    print(atdlib.vault)

__all__ = [ "main" ] if __name__ != "__main__" else main()
