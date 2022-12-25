#!/usr/bin/python3

from decimal import *

with open('n_val', 'rb') as fn:
  n = fn.read()
  n = n.decode('utf-8')
  #print()
   
with open('e_val', 'rb') as fe:
  e = fe.read()
  e = e.decode('utf-8')
  #print(e_value)
  
with open('c_cipher', 'rb') as fc:
  c = fc.read()
  c = c.decode('utf-8')
  #print(c_value)
  
# https://docs.python.org/3/library/decimal.html
c = Decimal(c)
e = Decimal(e)

getcontext().prec = 500 # Set a big enough precision
root = pow(c, 1/e) # Calculate c^(1/e) = m^(e * 1/e) = m
print(root)

# Decode with no padding
m = hex(int(root))[2:-1] # Number to hex
m = ''.join(chr(int(m[i:i+2], 16)) for i in range(0, len(m), 2)) # Hex to Ascii
print(m)
