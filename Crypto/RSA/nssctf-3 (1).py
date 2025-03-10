from Crypto.Util.number import *
flag = b'******'

m1 = bytes_to_long(flag[:len(flag)//2])
m2 = bytes_to_long(flag[len(flag)//2:])

assert 18608629446895353521310408885845687520013234781800558*m1-14258810472138345414555137649316815272478951117940067*m2 == 1
