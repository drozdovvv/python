#!/usr/bin/env python
#encoding: utf-8

napis = """ k1:w1
k2:w2
k3:w3"""
slownik ={}
for linia in napis.splitlines():
	element= linia.split(":")
	slownik[element[0]]=element[1]
	
#print (slownik)

import sys
with open(sys.argv[1],"r") as f:
  napis = f.read()
slownik= {}
for linia in  filter(None,napis.splitlines()):
  element = linia.split(":")
  slownik[element[0]]=element[1]
  
#print slownik


import sys
slownik = {}
with open(sys.argv[1],"r") as plik:
  for linia in plik:
     for slowo in linia.split():
	    if (slowo in slownik):
		  slownik[slowo] += 1
        else:
		  slownik[slowo] = 1
		
		
		
#print (slownik)






