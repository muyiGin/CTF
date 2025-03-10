from Crypto.Util.number import *
from gmpy2 import *

# flag = b'NSSCTF{******}'

# p = getPrime(256)
# q = getPrime(256)

# assert p%4 == 3 and q%4 == 3

# n = p*q
# e = 2
# m = bytes_to_long(flag)

# c = powmod(m, e, n)

# print(f'p = {p}')
# print(f'q = {q}')
# print(f'e = {e}')
# print(f'c = {c}')

p = 67711062621608175960173275013534737889372437946924512522469843485353704013203
q = 91200252033239924238625443698357031288749612243099728355449192607988117291739
e = 2
c = 5251890478898826530186837207902117236305266861227697352434308106457554098811792713226801824100629792962861125855696719512180887415808454466978721678349614


def rabin(n):
    exp = (n + 1) // 4
    m1 = pow(c, exp, n)
    m2 = n - m1
    return m1, m2


def CRT(a, b, na, nb):
    N = na * nb
    return (a * nb * inverse(nb, na) + b * na * inverse(na, nb)) % N


for mp in rabin(p):
    for mq in rabin(q):
        m = CRT(mp, mq, p, q)
        print(long_to_bytes(m))
