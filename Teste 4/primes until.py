# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:54:00 2019

@author: diogo
"""

def prime():
    primes = []
    for possiblePrime in range(2,10000):
        isPrime = True
        for num in range(2,possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime: primes.append(possiblePrime)
    return primes

print(prime())