#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

OUTPUT = '../bin/wallet'
#exclude
import sys
from pypreprocessor import pypreprocessor as cpp
if 'debug' in sys.argv:
    cpp.defines.append('debug')
if 'prod' in sys.argv:
    cpp.defines.append('prod')
    cpp.output = OUTPUT
    cpp.removeMeta = True
if 'post' in sys.argv:
    cpp.defines.append('post')
    cpp.output = OUTPUT
cpp.parse()
#endexclude

import usb

#ifdef debug
print('This script is running in \'debug\' mode')
#ifdef prod
print('This script is running in \'prod\' mode')
print('To see the output open ' + OUTPUT)
#ifdef post
print('This script is running in \'post\' mode')
print('To see the output open ' + OUTPUT)
#endif

def main():
    print('test')
    print(usb)

if __name__ == "__main__":
    main()
