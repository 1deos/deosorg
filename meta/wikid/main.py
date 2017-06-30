#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import yaml

render = web.template.render('./templates/')
render._add_global(render, 'render')

def main():
    data = {
        'toc': None,
        'author_name': 'Andrew DeSantis',
        'author_email': 'atd@bitcoin.sh'
    }
    content = render.base(data)
    with open('./var/wiki/index.md', 'w') as fp:
        fp.write(str(content).replace('\n\n\n', '\n\n'))
    lines = open('./var/wiki/index.md').readlines()
    open('./var/wiki/index.md', 'w').writelines(lines[1:])

if __name__ == "__main__":
    main()
