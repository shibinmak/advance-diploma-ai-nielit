#!/usr/bin/python
import sys
import numpy as np
n=int(sys.argv[1])
def prm(n):
 rval=True
 for i in range(2,n/2):
  if n%i==0:
   rval=False
   break
 else:
  rval=True
 return rval
if prm(n):
 n+=1
def factr(n):
 f=[]
 while not(prm(n)) :
  for i in range(2,n/2):
   if n%i == 0:
    f.append(i)
    n/=i
    break
 f.append(n)
 return f
print factr(n)
ar1=np.arange(n).reshape(factr(n))
print ar1
