from Crypto.Util.number import *
flag = b'NSSCTF{******}'

p = getPrime(512)
q = getPrime(512)
n = p*p*q
e = n

c = pow(bytes_to_long(flag), e, n)
d = inverse(e, (p-1)*(q-1))

print(f'n = {n}')
print(f'd = {d}')
print(f'c = {c}')

'''
n = 539403894871945779827202174061302970341082455928364137444962844359039924160163196863639732747261316352083923762760392277536591121706270680734175544093484423564223679628430671167864783270170316881238613070741410367403388936640139281272357761773388084534717028640788227350254140821128908338938211038299089224967666902522698905762169859839320277939509727532793553875254243396522340305880944219886874086251872580220405893975158782585205038779055706441633392356197489
d = 58169755386408729394668831947856757060407423126014928705447058468355548861569452522734305188388017764321018770435192767746145932739423507387500606563617116764196418533748380893094448060562081543927295828007016873588530479985728135015510171217414380395169021607415979109815455365309760152218352878885075237009
c = 192900246089028524753714085947506209686933390275949638288635203069117504901164350538204619142802436833736532680210208373707687461486601253665313637541968852691434282584934523173439632554783111037594035333325446559685553119339191110056283203940511701992217372405369575376549738295022767068810511670144120539082403063406787770958515441813335548550876818218065412869322721395317537328975187612606437225577060414403223288106406471061759010085578263501971809720648827
'''