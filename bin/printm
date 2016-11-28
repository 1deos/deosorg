#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

def _set_color():
    color = sys.argv[1]
    if 'black' == color: return "\x1b[30;01m"
    elif 'red' == color: return "\x1b[31;01m"
    elif 'green' == color: return "\x1b[32;01m"
    elif 'yellow' == color: return "\x1b[33;01m"
    elif 'blue' == color: return "\x1b[34;01m"
    elif 'purple' == color: return "\x1b[35;01m"
    elif 'cyan' == color: return "\x1b[36;01m"
    return "\x1b[34;01m"

def main():
    if 4 == len(sys.argv):
        color, cmd, action = _set_color(), sys.argv[2], sys.argv[3]
        if action == "stop": template = '%s[ %s : %s  ]\x1b[0m'
        else: template = '\n%s[ %s : %s ]\x1b[0m'
        print(template % (color, cmd, action))

if __name__ == "__main__":
    main()
