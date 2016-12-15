#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def get_color(color):
    if 'default' == color:
        return '\x1b[39;01m'
    elif 'black' == color:
        return '\x1b[30;01m'
    elif 'red' == color:
        return '\x1b[31;01m'
    elif 'green' == color:
        return '\x1b[32;01m'
    elif 'yellow' == color:
        return '\x1b[33;01m'
    elif 'blue' == color:
        return '\x1b[34;01m'
    elif 'magenta' == color:
        return '\x1b[35;01m'
    elif 'cyan' == color:
        return '\x1b[36;01m'
    return '\x1b[34;01m'

def main():
    if 4 == len(sys.argv):
        color, cmd, action = get_color(sys.argv[1]), sys.argv[2], sys.argv[3]
        if action == 'stop':
            action = 'exit'
            template = '\x1b[1m%s[ ΔOS : %s : make : %s ]\x1b[0m'
        else:
            action = 'init'
            template = '\x1b[1m%s[ ΔOS : %s : make : %s ]\x1b[0m'
        print template % (color, action, cmd)

if __name__ == "__main__":
    main()
