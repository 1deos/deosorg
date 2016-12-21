#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import configobj
import jsonschema
import web

import simplejson as json
import ruamel.yaml as yaml

def build(template,data):
    code=web.template.Template(template.replace('$','$$'
                                      ).replace('Δ with', '$def with'
                                      ).replace('Δ','$'
                                      ).replace('#!/bin/sh','##!/bin/sh'
                                      ).replace('# -*-','## -*-'))
    return str(code(data)).replace(4*' ','\t'
                         ).replace('$(False)','$(FALSE)'
                         ).replace('$(True)','$(TRUE)'
                         ).replace('\n\nifeq','\nifeq'
                         ).replace('\n\nelse','\nelse'
                         ).replace('\n\nendif','\nendif'
                         )[1:]

def get_environment(data,raw,debug=False):
    try:
        res=None
        env=data.split('## Environment\n\n```yaml\n')[1].split(\
            '```\n\n## Template')[0]
        if isinstance(env, basestring):
            res=yaml.safe_load(env)
    except:
        res=None
    else:
        if debug:
            print(res)
    finally:
        return res

def get_name(data,debug=False):
    try:
        res=None
        name=data.split('\n')[0]
        if name[0:3]=='# `' and name[-1]=='`':
            res=name[3:-1]
    except:
        res=None
    else:
        if debug:
            print(res)
    finally:
        return res

def get_schema(data,raw,debug=False):
    try:
        res=None
        schema=data.split('## Schema\n\n```yaml\n')[1].split(\
            '```\n\n## Environment')[0]
        if isinstance(schema,basestring):
            res=yaml.safe_load(schema)
    except:
        res=None
    else:
        if debug:
            print(res)
    finally:
        return res

def get_template(data,raw,debug=False):
    try:
        res=''
        template=data.split('## Template\n\n```')[1]
        line=template.split('\n')
        for i in range(0,len(line)):
            if i!=0 and i!=len(line)-2:
                res=res+line[i]+'\n'
    except:
        res=None
    else:
        if debug:
            print(res)
    finally:
        return res

def main():
    config=configobj.ConfigObj('Deosfile')
    for key,value in config.iteritems():
        if key not in ('author','version') and 'type' in value:
            debug=False
            data,env,name,raw,schema,template=None,None,None,None,None,None
            if value['type']=='make' or value['type']=='sh'\
                or value['type']=='gitignore' or value['type']=='ini'\
                or value['type']=='nvmrc' or value['type']=='ruby'\
                or value['type']=='lz':
                with open(value['meta']) as f:
                    raw=f.read()
            if isinstance(raw,basestring):
                print(key)
                data=raw
                name=get_name(data)
                if isinstance(name,basestring):
                    raw=raw.split('\n')[1:]
                    if '## Environment' in raw and '## Schema' in raw and\
                        '## Template' in raw:
                        env=get_environment(data,raw,debug=False)
                        schema=get_schema(data,raw,debug=False)
                        if isinstance(env,dict) and isinstance(schema,dict):
                            jsonschema.validate(env, schema)
                            if debug:
                                print(json.dumps(env,sort_keys=True,indent=2))
                            template=get_template(data,raw,debug=debug)
                            if isinstance(template,basestring):
                                code = build(template,env)
                                with open(name,'w') as f:
                                    f.write(code)

if __name__=="__main__":
    main()
