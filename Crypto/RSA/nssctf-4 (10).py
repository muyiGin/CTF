from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)

flag = b'NSSCTF{******}'

n = p*q
m = bytes_to_long(flag)

e = 7
d = inverse(e, (p-1)*(q-1))
c = pow(m, e, n)

print(f'n = {n}')
print(f'd = {d&(2**410-1)}')
print(f'c = {c}')

'''
n = 156739515226635581524592797610847324418529702729659760727202454324501479907596255649349406182566636617352761983459648380669151952249526892078378572831346100444943020314226860094300911303589453661009834514243241261318188779118227457185670049393331570167726982038500849886842419000632840251465852441285715712609
d = 1865327042408619801352057511348007441275330638921397637214779955824487081626289235627502761209800783644652914147540081431451
c = 72260884070910873253619893714557327479300651539617744913822595501549980223259020597000998829262506949824325397279990912888752157554696212466966682483623575703479116305560808218806054242135099446883072418808228726774129042552815016924170283352225826854235696829480360844745488070927932843928843556296485306121
'''