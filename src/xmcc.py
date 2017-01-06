#!/usr/bin/env python
# -*- coding: utf-8 -*-

WRITE_FILE = "../include/.macro/deos.def"
READ_FILE  = "./deos.py"

def main():
    fp = open(WRITE_FILE, 'w')
    with open(READ_FILE) as f:
        data = f.read()
    data = data.replace('"__main__"', "'__main__'")
    result = str()
    for c in data:
        if c == '\t':
            result += 4*' '
        else:
            result += c
    lines = result.split('\n')
    for i in range(0, len(lines)):
        line = lines[i]
        if len(line):
            if line[-1] == '"':
                line += ' '
            line = line.replace('"""', "'''"
                      ).replace(' "', ' \\\"'
                      ).replace('" ', '\\\" '
                      ).replace('":', '\\\":'
                      ).replace('\\n', '\\\\n')
            if line[-1] == ' ':
                line = line[0:-1]
            if i == 0:
                fp.write('X("%s\\n"\\\n' % line)
            elif i == len(lines)-2:
                fp.write('  "%s\\n")\n' % line)
            else:
                fp.write('  "%s\\n"\\\n' % line)
    fp.write('#undef X\n')

if __name__ == "__main__":
    main()
