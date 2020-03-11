from __future__ import division
from numpy.ma import sqrt
import numpy as np
import matplotlib.pyplot as plt
from RSA import RSA_encrypt, eratosthenes, gcd, check_key, mult_inverse, powermod, powermod2
from pca import meanCenter, standardize, pca
from regression import linearRegression, quadraticRegression, cubicRegression

# Oppgave 1 RSA

# a) Kodet beskjed = BERGEN

# b) Kod melding = [7040899,18090405]

# c)

t = [7040899,18090405]
n = 160169311
e = 1737
u = RSA_encrypt(n, e, t)
print(u)

# Krypert melding = [58822763, 79142533]

# d)

qn = int(sqrt(n))
liste = eratosthenes(qn)
for i in liste:
    if n%i == 0:
        p = i

q = n//p
print(p, q)

# p = 11897, q = 13463

# e) gcd(e,(p­1)*(q­1)) å være lik 1, altså at de er primtall mot hverandre

i = check_key(p,q,e)

# i = true, så det er en er en korrekt nøkkel

# f)

d = mult_inverse(e,(p-1)*(q-1))

# Finner d = 104734329

message = [112718817, 85128008, 148479246, 91503316, 26066602, 95584344, 142943071]
for i in message:
    print(powermod(i,d, n), end=' ')

# Kodet melding = 99990904 6990611 4030417 99120406 99190811 99041018 120413

# Melding dekodet = JEG GLEDER MEG TIL EKSAMEN

# Oppgave 2 Regresjon

# a)
temp = [13.14, 12.89, 12.26, 12.64, 12.22, 12.47, 12.51, 12.80, 12.24, 12.77, 13.35, 12.82, 13.57, 13.38, 14.41, 14.00,
        15.68, 15.41, 15.51, 15.86, 15.72]
tid = [2.86, 2*2.86, 3*2.86, 4*2.86, 5*2.86, 6*2.86, 7*2.86, 8*2.86, 9*2.86, 10*2.86, 11*2.86, 12*2.86, 13*2.86,
       14*2.86, 15*2.86, 16*2.86, 17*2.86, 18*2.86, 19*2.86, 20*2.86, 21*2.86]

plt.figure(0)
plt.scatter(tid, temp)

# Ja, det ser ut som det passer.

# b)

[a, b] = linearRegression(tid, temp)
xplot = np.array(list(range(0, 60)))
yplot = np.dot(a, xplot)+b
plt.plot(xplot, yplot)

Sy2 = sum((temp-np.mean(temp))**2)
SSELin = sum((temp-np.dot(a, tid)-b)**2)
r2Linear = (Sy2-SSELin)/Sy2

# Determinasjonskoeffisienten = 0.745

# c)

[a, b, c] = quadraticRegression(tid, temp)
yplot = np.dot(a, np.power(xplot, 2))+np.dot(b, xplot) + c
plt.plot(xplot, yplot)

SSEQuad = sum((temp-(np.dot(a, np.power(tid, 2))+np.dot(b, tid) + c))**2)
r2Quadratic = (Sy2-SSEQuad)/Sy2


# Determinasjonskoeffisienten ved kvadratisk tilnærming = 0.913

[a, b, c, d] = cubicRegression(tid, temp)
yplot = np.dot(a, np.power(xplot, 3))+np.dot(b, np.power(xplot, 2)) + np.dot(c, xplot) + d
plt.plot(xplot, yplot)

SSECubic = sum((temp-(np.dot(a, np.power(tid, 3))+np.dot(b, np.power(tid, 2)) + np.dot(c, tid) + d))**2)
r2Cubic = (Sy2-SSECubic)/Sy2
plt.show()

# Determinasjonskoeffisienten ved kvadratisk tilnærming = 0.934

# d) Det er den kubiske tilnærmingen som passer best, både basert på plot og determinasjonskoeffisienten.

# Oppgave 3

# Fylker (alfabetisk, tallene under står i den samme rekkefølgen):
Fylker = ['Akershus','Aust-Agder','Buskerud','Finnmark','Hedmark','Hordaland','Møre og Romsdal','Nordland',
          'Nord-Trøndelag','Oppland','Oslo','Rogaland','Sogn og Fjordane','Sør-Trøndelag','Telemark','Troms',
          'Vest-Agder','Vestfold','Østfold']

Indikatorer = ['Areal','Folketall', 'BNP/kapita','BNP/sysselsatt', 'Sysselsatte']

#Areal målt i kvadratkilometer

Areal = [4917.95,9155.36,14912.19,48631.38,27397.85,15436.98,15101.07,38478.13,22414,25192.09,454.10,9376.77,18622.44,
         18848,15298.23,25876.85,7278.71,2225.38,4187.22]

# Folketall 1/1 2017

Folketall =[604368,116673,279714,76149,196190,519963,266274,242866,137233,189479,666759,472024,110266,317363,173307,
            165632,184116,247048,292893]

# BNP og sysselsatte: Tall fra 2017

BNPKap=[435982,337974,397080,438594,364944,488515,433030,428402,367157,363111,820117,488463,455872,473954,371886,
        451887,403893,364007,331575]

BNPSyss =[918710,771973,831298,808765,777248,922939,834642,850163,759414,731136,1125019,899272,846111,886057,817060,
          824648,811833,792748,778412]

Sysselsatte=[270338,47868,125938,37143,86627,254290,127060,116020,62621,86968,468375,233986,54490,166479,74749,84537,
             86997,106931,118320]

X = np.transpose(np.array([Areal,Folketall,BNPKap,BNPSyss,Sysselsatte]))

# a)

X = meanCenter(X)
X = standardize(X)

# Matrise X

# [-0.63453849 -0.94222438 -0.89082706 -0.80036086 -0.85331319]
# [-0.17137967  0.01742517 -0.33347532 -0.11689616 -0.10886456]
# [ 2.54145713 -1.18074621  0.05798917 -0.37649178 -0.95558309]
# [ 0.83313906 -0.47419209 -0.6365081  -0.73958924 -0.48372072]
# [-0.12915832  1.43151638  0.52872913  0.93887103  1.11505589]
# [-0.15618356 -0.06168186  0.00552233 -0.07837098 -0.09816556]
# [ 1.72458964 -0.19945995 -0.03811831  0.10044159 -0.20343919]
# [ 0.43216942 -0.82120945 -0.61564018 -0.94504915 -0.71263366]
# [ 0.6556773  -0.51369263 -0.65379274 -1.27083111 -0.48046906]
# [-1.33458788  2.29554883  3.65563591  3.26697127  3.15649669]
# [-0.61672521  1.1493503   0.52823879  0.66621096  0.92144394]
# [ 0.12712403 -0.9799356   0.2209155   0.05375977 -0.79016807]
# [ 0.14527118  0.23902493  0.3914233   0.51396509  0.27772044]
# [-0.14032128 -0.60888005 -0.57104714 -0.28092769 -0.59698523]
# [ 0.71076884 -0.65405464  0.18333815 -0.19350872 -0.50365024]
# [-0.7855221  -0.54525893 -0.26923079 -0.34114631 -0.48019252]
# [-1.19208168 -0.17484495 -0.64534373 -0.5610186  -0.29010877]
# [-1.03424421  0.09499597 -0.9511677  -0.72617916 -0.18150719]]

# b)

[T, P, E] = pca(X, a=2)

# Matrise T

#  [ 1.50218523 -0.97524612]
#  [ 0.20760365 -0.31732345]
#  [ 1.89445304  2.30564807]
#  [ 1.34601333  0.3516439 ]
#  [-1.98024396  0.12608152]
#  [ 0.07275092 -0.14337589]
#  [ 0.633548    1.53157133]
#  [ 1.61001596  0.01317092]
#  [ 1.58373061  0.0715005 ]
#  [-6.30098955  0.80889087]
#  [-1.74589155 -0.32135939]
#  [ 0.77574032  0.35151157]
#  [-0.64339786  0.37569559]
#  [ 0.94884292 -0.33914827]
#  [ 0.77202904  0.73869986]
#  [ 0.5783785  -0.79674476]
#  [ 0.47240158 -1.40926407]
#  [ 0.55020971 -1.4761789 ]]

# Matrise P

# [ 0.47623838  0.14661766]
# [ 0.44929136 -0.41302703]
# [ 0.49114437 -0.2350542 ]
# [ 0.50652209 -0.00806347]]

# c)

# Scoreplot, loadingplot og biplot.

plt.figure(0)
plt.scatter(T[:, 0], T[:, 1])
for label, x, y in zip(Fylker, T[:, 0], T[:, 1]):
    plt.annotate(
        label,xy = (x, y),
        xytext = (5, -3),
        textcoords = 'offset points', ha = 'left')
plt.show()

# d)

# Østfold og Vestfold er veldig like.
# Nord-Trøndelag og Oppland er mest like.

# e)

# Oslo

# f)

# Finnmark, Troms og Nordland
# Oslo, skilles godt ut på areal.

# g)

# Vi ser at de nordligste fylkene er relativt nær hverandre.