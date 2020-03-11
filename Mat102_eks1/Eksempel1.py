import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(6, -6)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()
#
# svar = 0
# for i in range(100):
#     if i % 2 == 1:
#         svar += i
# print(svar)
#
# oddetall = [i for i in range(100) if i % 2 == 1]
# print(oddetall)
#
# kvadrater = []
# i = 0
# while i**2 < 1000:
#     kvadrater.append(i**2)
#     i += 1
# print(kvadrater)
#
# kvadrat = [i**2 for i in range(int(np.sqrt(1000)))]
# print(kvadrat)

def andregradsligning(a,b,c):
    diskriminannt = b**2-4*a*c
    if diskriminannt < 0:
        print("Ingen reelle løsninger")
    else:
        x1 = (-b + np.sqrt(diskriminannt))/(2*a)
        x2 = (-b - np.sqrt(diskriminannt))/(2*a)
        return(x1,x2)
print(andregradsligning(1,0,-4))



