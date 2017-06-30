#!/usr/bin/env python
# -*- coding: utf-8 -*-

def replace_tab(s):
    r = str()
    for c in s:
        if c == '\t':
            r += '    '
        else:
            r += c
    return r

def main():
    fp = open('../macros/python.def', 'w')
    with open('../main.py') as f:
        data = f.read()
    lines = replace_tab(data).split('\n')
    for i in range(0, len(lines)):
        line = lines[i]
        if len(line):
            if line[-1] == '"':
                line += ' '
            line = line.replace(
                '"""', "'''").replace(
                ' "', ' \\\"').replace(
                '" ', '\\\" ').replace(
                '":', '\\\":').replace(
                '\\n', '\\\\n')
            if line[-1] == ' ':
                line = line[0:-1]
            if i == 0:
                fp.write('X("%s\\n" \\\n' % line)
            elif i == len(lines)-2:
                fp.write('  "%s\\n") \n' % line)
            else:
                fp.write('  "%s\\n" \\\n' % line)
    fp.write('#undef X')

if __name__ == "__main__":
    main()
