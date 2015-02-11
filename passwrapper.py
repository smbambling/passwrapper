#!/usr/bin/python

import argparse
import os
import subprocess

__author__ = 'Steven Bambling'

parser = argparse.ArgumentParser(
        description='Password-Store (pass) wrapper for mass input and/or changes',
        epilog='Example: ./passwrapper.py -n \'blah1 foo/bar/baz\' -s \'sec1 sec2 \''
        )
parser.add_argument('-n','--names', help='End Point Names (pass-names)',required=True)
parser.add_argument('-s','--secrets',help='End Point Passwords', required=True)
args = parser.parse_args()

### convert to array ##
pass_names = args.names.split(' ')
pass_secrets = args.secrets.split(' ')

### show values ##
#print ("Password Names: %s" % args.names)
#print ("Password Secrets: %s" % args.secrets)

## verify we have enough password names and secrets
if len(pass_names) != len(pass_secrets):
    if len(pass_names) > len(pass_secrets):
        print ('Not enough -s secrets provided')
        exit(1)
    elif len(pass_secrets) > len(pass_names):
        print ('Not engough -n names provided')
        exit(1)
    else:
        print ('How did we get here ??')
        exit(1)

for name, secret in zip(pass_names, pass_secrets):
    print ('pass insert %s' % name)
    p1 = subprocess.Popen(['echo', secret], stdout=subprocess.PIPE)
    p2 = subprocess.check_call(['pass', 'insert', '-e', name], stdin=p1.stdout)
    p1.stdout.close()
