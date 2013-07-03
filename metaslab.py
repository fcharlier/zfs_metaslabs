#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

# "THE BEER-WARE LICENSE" (Revision 42):
# fcharlier@ploup.net wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. François Charlier

import datetime
import os
import re
import socket
import sys

if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
    print >> sys.stderr, 'you shall pass a zpool name as a parameter'
    exit(1)
poolname = sys.argv[1]

pat = re.compile('metaslab\s+(\d+).+?freepct\s+(\d+)%',
                 re.MULTILINE | re.DOTALL)
with os.popen('zdb -mm %s' % poolname) as p:
    data = p.read()
usage = [100 - int(m.group(2)) for m in pat.finditer(data)]
print "barChart(%s, '%s@%s %s');" % (usage,
                                     poolname,
                                     socket.gethostname(),
                                     datetime.datetime.today().isoformat())
