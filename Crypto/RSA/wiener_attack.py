from Crypto.Util.number import *
from gmpy2 import *

# flag = b'NSSCTF{******}'

# p = getPrime(256)
# q = getPrime(256)

# n = p*q
# d = getPrime(128)
# e = inverse(d, (p-1)*(q-1))
# m = bytes_to_long(flag)

# c = powmod(m, e, n)

# print(f'n = {n}')
# print(f'e = {e}')
# print(f'c = {c}')

n = 6969872410035233098344189258766624225446081814953480897731644163180991292913719910322241873463164232700368119465476508174863062276659958418657253738005689
e = 3331016607237504021038095412236348385663413736904453330557803644384818257225138777641344877202234881627514102078530507171735156112302207979925588113589669
c = 1754994938947260364311041300467524420957926989584983693004487724099773647229373820465164193428679197813476633649362998772470084452129370353136199193923837


def continue_fraction(a, b):
    cf = []
    cf.append(a // b)
    a, b = b, a % b
    while b != 0:
        cf.append(a // b)
        a, b = b, a % b
    return cf


def convergent_factor(cf):
    h = [0, 1]
    g = [1, 0]
    i = 2
    for ai in cf:
        hi = ai * h[i - 1] + h[i - 2]
        gi = ai * g[i - 1] + g[i - 2]
        h.append(hi)
        g.append(gi)
        i += 1
    return g


def wiener_attack(e, N):
    cf = continue_fraction(e, N)
    cvg = convergent_factor(cf)
    for d in cvg:
        flag = long_to_bytes(pow(c, d, N))
        if b"NSS" in flag:
            print(flag)
            break


wiener_attack(e, n)
