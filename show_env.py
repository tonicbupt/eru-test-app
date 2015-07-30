import os
import time

for key, value in os.environ.iteritems():
    print key, value

while True:
    time.sleep(100)
    print 'sleep, waiting for ending'
