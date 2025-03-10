from Crypto.Util.number import *

# flag = b'NSSCTF{******}'

# p = getPrime(128)
# q = getPrime(128)
# n = p*q
# e = 65537
# phi = (p-1)*(q-1)

# m = bytes_to_long(flag)

# c = pow(m, e, n)

# print(f'n = {n}')
# print(f'e = {e}')
# print(f'c = {c}')

n = 53690629441472827148854210396580805205350972614395425306316047967905824330731
e = 65537
c = 22130296334673852790451396673112575082637108306697684532954477845025885087040
p = 277349599849597463956171076348973750041
q = n // p
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
