# a)
from numpy.ma import sqrt, count

from RSA import RSA_encrypt, eratosthenes, gcd, check_key, mult_inverse, powermod, powermod2

t = [3040003]
n = 115912873
e = 133
u = RSA_encrypt(n, e, t)
print(u)

# b)
qn = int(sqrt(n))
print(qn)
print(count(eratosthenes(qn)))

# c)
liste = eratosthenes(qn)
for i in liste:
    if n%i == 0:
        p = i

q = n//p
print(p, q)

# d)
d = mult_inverse(e,(p-1)*(q-1))
print(d)

# e)
print(powermod(u[0],d, n))
message = [88709091,115282881,44754833,5274204,37162740,69569552,73765472]
for i in message:
    print(powermod(i,d, n), end=' ')
print('   C' + 'OFFE' + 'E IS' + ' SERVED ' + 'T EIGHT')