#!/usr/bin/env python
#Mocha's unit conversion suite
#velocity
from math import pi
def mih2ms(v):
    return n*1397/3125
def mih2kmh(v):
    return n*50292/3125
#length
def mi2m(l):
    return n*201168/125
def mi2km(l):
    return n*50292/3125
def au2m(l):
    return n*149597870700
def ly2m(l):
    return n*9460730472580800
def pc2m(l):
    return au2m(n*648000/pi())
#time
def y2s(t):
    return n*31556952
#pressure
def atm2pa(p):
    return n*101325
#temperature
def f2k(t):
    return (n+459.67)*5/9
def f2c(t):
    return (n-32)*5/9
def c2k(t):
    return n+273.15
while 1:
    print(input("Use a function: "))
