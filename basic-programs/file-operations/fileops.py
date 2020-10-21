#!/usr/bin/env python3.9

f = open('names.txt','r')
print(f.read(), end="")
f.close()

with open('names.txt','a') as f:
    f.write('nikhil\nharshad')

print("\n")
print("=" * 10)

f = open('names.txt','r')
print(f.read(), end="")

print("\n")
print("=" * 10)

# Move to 13th character (offset)
f.seek(13)
print(f.read(), end="")
f.close()
