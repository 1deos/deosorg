#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json

templates = "../templates/graphviz/"
state = {
    'fontname': 'Arial',
}

def load():
    i = 0
    store = []
    keys = None
    with open("../var/data/csv/eth-000.csv") as f:
        for line in f:
            data = line.split('","')[1:-2]
            if i == 0:
                keys = [k for k in line.split('","')[1:-2]]
            else:
                d = {}
                for j in range(0, len(keys)):
                    d[keys[j]] = data[j]
                store += [d]
            i += 1
    with open('../var/json/eth-000.json', 'w') as f:
        f.write(json.dumps(store, sort_keys=True, indent=4))
    return store

def read(fname):
    data = open(templates+fname).read()
    data = data.replace('$','$$'
              ).replace('Δ with', '$def with'
              ).replace('Δ','$')
    return data

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

def write(fname, code):
    with open(fname, 'w') as f:
        f.write(code)

def main():
    data = load()
    state['data'] = data
    if isinstance(data, list):
        res = build('g.dot', state)
        write('../var/dot/g.dot', res)

if __name__ == "__main__":
    main()
