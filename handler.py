#!/usr/bin/env python
import signal
import sys
import time
import os

def signal_handler(sig, frame):
    timeout = os.environ.get('WAIT_BEFORE_CLOSE', '0')
    print("Interupt recieved.  Sleeping for: " + timeout)
    time.sleep(float(timeout))
    print("Sleep elapsed.  Closing")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Waiting for interupt')
signal.pause()