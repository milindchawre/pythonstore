#!/usr/bin/env python3.9

from time import localtime, mktime, strftime

start_time = localtime()

print(f"Time started at {strftime('%X', start_time)}")

input("Press 'Enter' to stop timer.")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time difference: {difference} seconds")
