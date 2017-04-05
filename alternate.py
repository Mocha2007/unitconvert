#!/usr/bin/env python
#Mocha's unit conversion suite
#velocity
from math import pi
def mih2ms(v):
    return v*1397/3125
def mih2kmh(v):
    return v*25146/15625
#length
def mi2m(l):
    return l*201168/125
def mi2km(l):
    return l*25146/15625
def au2m(l):
    return l*149597870700
def ly2m(l):
    return l*9460730472580800
def pc2m(l):
    return au2m(l*648000/pi())
#time
def y2s(t):
    return t*31556952
#pressure
def atm2pa(p):
    return t*101325
#temperature
def f2k(t):
    return (t+459.67)*5/9
def f2c(t):
    return (t-32)*5/9
def c2k(t):
    return t+273.15