#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function


import sys
import blockstack_client
import blockstack_client.actions
import simplejson as json
import ruamel.yaml as yaml


DOMAIN_PATH='root/id'


#def main():
#    exists=blockstack_client.wallet.wallet_exists()
#    if isinstance(exists,bool):
#        if exists:
#            wallet=blockstack_client.wallet.load_wallet()
#            if 'status' in wallet:
#                if isinstance(wallet['status'],bool):
#                    #print(json.dumps(wallet,sort_keys=True,indent=2))
#                    addr=wallet['wallet']['payment_addresses']
#                    balance=blockstack_client.wallet.get_balance(addr)
#                    print(balance)
#                    wallet_path='var/privkey/wallet.json'
#                    blockstack_client.wallet.write_wallet(wallet['wallet'],
#                                                          wallet_path)


def wallet_test():
    print('hello!')
    return None


def whois(name):
    class A: pass
    A.name=name
    data=blockstack_client.actions.cli_whois(A)
    if 'error' not in data and 'atd.id'!=name:
        out=yaml.dump(data,Dumper=yaml.RoundTripDumper)
        with open('%s/@%s.yml'%(DOMAIN_PATH,name),'w') as f:
            f.write(out)
        return data
    return None


def main():
    if 3==len(sys.argv):
        if isinstance(sys.argv[1],basestring)\
            and isinstance(sys.argv[2],basestring):
            if 'whois'==sys.argv[1]:
                if 2==len(sys.argv[2].split('.'))\
                    and 'id'==sys.argv[2].split('.')[1]:
                    data=whois(sys.argv[2])
            elif 'wallet'==sys.argv[1]:
                if 'test'==sys.argv[2]:
                    data=wallet_test()


if __name__=="__main__":
    main()
