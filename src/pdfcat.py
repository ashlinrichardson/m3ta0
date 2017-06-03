#!/usr/bin/env python
import os
import sys
from fl0w3r import error, run

args = sys.argv
if len(args) < 4:
  error('pdfcat.py.\nUsage: [file1] [file2] ... [filen] [outfilename.pdf]')

files = args[1:]
outfile, infile = files[-1], files[:-1]

if os.path.exists(outfile):
  error('output file already exists: aborting')

s = ''
for infile in infiles: 
	s += (infile + ' ')

print("input file names: " + s)
print("output file name:  " + str(outfile))

cmd = "gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=" + outfile
for infile in infiles: 
	cmd += (" " + infile)
run(cmd)
