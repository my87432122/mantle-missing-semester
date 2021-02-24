#!/usr/bin/env python
import signal, time

def handler(signum, time):
    print("\nI got a SIGINT, bug I am not stopping")

signal.signal(signal.SIGINT, handler)
i = 0
while True:
    time.sleep(.1)
    print(f"\r{i}", end="")
    i += 1