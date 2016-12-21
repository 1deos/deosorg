#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging,logging.config
import ruamel.yaml as yaml

CONFIG_FILE="./etc/logger/logger.yml"

def get_config(fname):
    config=None
    with open(fname) as f:
        config=yaml.safe_load(f)
    return config

def get_logger(fname):
    config=get_config(fname)
    if config:
        logging.config.dictConfig(config)
        logger=logging.getLogger('DeOS')
        return logger
    return None

def log(case,logger,msg):
    if 'DEBUG'==case:
        logger.debug(msg)
    elif 'INFO'==case:
        logger.info(msg)
    elif 'WARN'==case:
        logger.warn(msg)
    elif 'ERROR'==case:
        logger.error(msg)
    elif 'CRITICAL'==case:
        logger.critical(msg)

def main():
    logger=get_logger(CONFIG_FILE)
    if 3==len(sys.argv) and logger:
        case,msg=sys.argv[1],sys.argv[2]
        log(case,logger,str(msg).replace('vm :','vm      :'
                               ).replace(': all :',': all     :'
                               ).replace('build :','build   :'
                               ).replace('check :','check   :'
                               ).replace('clean :','clean   :'
                               ).replace('chmod :','chmod   :'
                               ).replace('rm :','rm      :'
                               ).replace('venv :','venv    :'))

if __name__=="__main__":
    main()
