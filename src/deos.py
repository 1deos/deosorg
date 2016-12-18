#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import configobj
import jsonschema
import ruamel.yaml as yaml
import simplejson as json
import web

#config = configobj.ConfigObj('Deosfile.meta.ini')
templates = "src/templates/"

def read(fname):
    data = open(templates+fname).read()
    data = data.replace('$','$$'
              ).replace('Δ with', '$def with'
              ).replace('Δ','$')
    return data

def write(fname, code):
    with open(fname, 'w') as f:
        f.write(code)

def render(fname):
    raw = read(fname)
    code = web.template.Template(raw)
    return code

def build(fname, data):
    code = render(fname)
    return str(code(data)).replace(8*' ','\t'
                         ).replace('$(False)', '$(FALSE)'
                         ).replace('$(True)', '$(TRUE)'
                         ).replace('\n\nifeq', '\nifeq'
                         ).replace('\n\nelse', '\nelse'
                         ).replace('\n\nendif', '\nendif'
                         )[1:]

def load():
    data, schema = None, None
    with open('Deosfile') as f:
        raw = f.read().split('---')
    if isinstance(raw, list):
        if isinstance(raw[1], basestring):
            data = yaml.safe_load(raw[2])
        if isinstance(raw[0], basestring):
            schema = yaml.safe_load(raw[1])
    if isinstance(data, dict) and isinstance(schema, dict):
        jsonschema.validate(data, schema)
        print(json.dumps(data, sort_keys=True, indent=2))
    else:
        return None
    return data

def main():
    data = load()
    if isinstance(data, dict):
        code = build('make/deosrc.mk', data['.deosrc'])
        write('var/build/.deosrc', code)
        code = build('make/makefile.mk', data['Makefile'])
        write('var/build/Makefile', code)

if __name__ == "__main__":
    main()
