# passwrapper

## Table of Contents

1. [Overview](#overview)
1. [Usage](#usage)

## Overview

A utility used for mass input and/or changes to the Password-Store

## Usage

### Arguments

The ````-n```` arg is a list of pass-name seperated by a space

> The -n arg can take a pass-name that is the full tree path

The ````-s```` arg is a list of secret passwords seperated by a space

````
  -n NAMES, --names NAMES
                        End Point Names (pass-names)
  -s SECRETS, --secrets SECRETS
                        End Point Passwords
````

### Example

````
./passwrapper.py -n 'blah1 foo/bar/baz' -s 'sec1 sec2'
````
