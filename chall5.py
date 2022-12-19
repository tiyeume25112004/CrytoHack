from operator import xor
a="label"
c=""
for i in a:
    b=xor(ord(i),13)
    print(chr(b))
