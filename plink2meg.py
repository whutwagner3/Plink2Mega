#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: willhutwagner
"""

import argparse

parser = argparse.ArgumentParser(description='Converts plink .mdist files to MEGA .meg file')
parser.add_argument('-i','--infile', help='input to be converted to meg file (without file extension)',required=True)
parser.add_argument('-o','--outfile',help='output name (without file extension)', required=True)
args = vars(parser.parse_args())

ids = {}
with open(args['infile']+'.mdist.id') as fi:
    for line in fi:
        text = line.strip().split(None,1)
        ids[text[1]] = text[0]

out='#mega\n!TITLE dog_genomes;\n!Format DataType=distance DataFormat=LowerLeft NTaxa='+str(len(ids))+';\n'

for dog in ids:
    out+='#'+dog+'_{'+ids[dog]+'}\n'
out+='\n'
lenid = len(ids)
with open(args['infile']+'.mdist') as fi:
    for line in fi:
        text = line.strip().split()
        for dist in text:
            out+=dist+'\t'
        for i in range(len(text),lenid):
            out+='\t'
        out=out[:-2]+'\n'
with open(args['outfile']+'.meg','w') as fi:
    fi.write(out)