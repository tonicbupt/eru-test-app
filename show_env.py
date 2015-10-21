import os
import sys
import time

for key, value in os.environ.iteritems():
    print >> sys.stderr, key, value

while True:
    time.sleep(10)
    print >> sys.stderr, 'sleep, waiting for ending'

    for key, value in os.environ.iteritems():
        print >> sys.stderr, key, value
