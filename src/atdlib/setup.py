#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
from distutils.core import Extension, setup

def main():
    setup(author = "Andrew DeSantis",
          author_email = "atd@gmx.it",
          packages = ["atdlib"],
          ext_modules = [Extension("atdlib.deos",
                          sources=["atdlib/deos_module.c"]),
                         Extension("atdlib.vault",
                          sources=["atdlib/vault_module.c"])],
          name = "atdlib",
          version = "v0.8-alpha.8")

__all__ = [ "main" ] if __name__ != "__main__" else main()
