from Crypto.Util.number import *
from random import choice

# flag = b'NSSCTF{******}'

# def getMyPrime(nbits):
#     while True:
#         p = 1
#         while p.bit_length() <= nbits:
#             p *= choice(sieve_base)

#         if isPrime(p+1):
#             return p+1

# p = getMyPrime(256)
# q = getMyPrime(256)

# n = p*q
# e = 65537
# m = bytes_to_long(flag)

# c = pow(m, e, n)

# print(f'n = {n}')
# print(f'e = {e}')
# print(f'c = {c}')

n = 53763529836257082401813045869248978487210852880716446938539970599235060144454914000042178896730979463959004404421520555831136502171902051936080825853063287829
e = 65537
c = 50368170865606429432907125510556310647510431461588875539696416879298699197677994843344925466156992948241894107250131926237473102312181031875514294014181272618

import math


def p_plus_1_attack():
    x = 1
    a = 2**x
    while True:
        x += 1
        a = pow(a % n, x, n)
        p = GCD(a - 1, n)
        if p != n and p != 1:
            return p


p = p_plus_1_attack()
q = n // p
print(p, q)
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(long_to_bytes(pow(c, d, n)))
