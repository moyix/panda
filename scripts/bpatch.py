#!/usr/bin/env python

import sys
import shutil
import os

if len(sys.argv) < 2:
    print >>sys.stderr, "usage: %s <patchfile>" % sys.argv[0]
    sys.exit(1)

f = open(sys.argv[1])
ref = f.readline().strip()

if not os.path.exists(ref):
    print >>sys.stderr, "error: couldn't find reference snapshot %s" % ref
    sys.exit(1)
else:
    print "Using reference %s as a base" % ref

basename = os.path.splitext(sys.argv[1])[0]
patched = basename + '-rr-snp'
print "Creating patched snapshot %s" % patched
shutil.copy(ref, patched)

of = open(patched, 'rb+')

for line in f:
    off, val = line.strip().split()
    off = int(off, 16)
    val = val.decode('hex')
    of.seek(off)
    of.write(val)

f.close()
of.close()

print "All done, no errors."
