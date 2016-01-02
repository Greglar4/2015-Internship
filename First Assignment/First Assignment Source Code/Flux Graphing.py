# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:25:26 2015

@author: Greg
"""

import matplotlib.pyplot as plt
import csv

x=[]
y=[]

"""*****************READING FILE DATA***************************"""

""" ECH UP """
f = open('ECHma0_UP.txt', 'r')
y=f.readlines()
f.close()

for i in range(0,10000):
    y[i]=float(y[i])
    
f = open('ECHmax_UP.txt', 'r')
y2=f.readlines()
f.close()

for i in range(0,10000):
    y2[i]=float(y2[i])
    
""" ECH DOWN """
f = open('ECHma0_DOWN.txt', 'r')
y3=f.readlines()
f.close()

for i in range(0,10000):
    y3[i]=float(y3[i])
    
f = open('ECHmax_DOWN.txt', 'r')
y4=f.readlines()
f.close()

for i in range(0,10000):
    y4[i]=float(y4[i])

f = open('ECHmaf_DOWN.txt', 'r')
y5=f.readlines()
f.close()

for i in range(0,10000):
    y5[i]=float(y5[i])
    
    
""" UBC UP """
f = open('UBCma0_UP.txt', 'r')
y6=f.readlines()
f.close()

for i in range(0,10000):
    y6[i]=float(y6[i])
    
f = open('UBCmax_UP.txt', 'r')
y7=f.readlines()
f.close()

for i in range(0,10000):
    y7[i]=float(y7[i])
    


""" UBC DOWN """
f = open('UBCma0_DOWN.txt', 'r')
y8=f.readlines()
f.close()

for i in range(0,10000):
    y8[i]=float(y8[i])
    
f = open('UBCmax_DOWN.txt', 'r')
y9=f.readlines()
f.close()

for i in range(0,10000):
    y9[i]=float(y9[i])

f = open('UBCmaf_DOWN.txt', 'r')
y10=f.readlines()
f.close()

for i in range(0,10000):
    y10[i]=float(y10[i])

""" LBC UP """
f = open('LBCma0_UP.txt', 'r')
y11=f.readlines()
f.close()

for i in range(0,10000):
    y11[i]=float(y11[i])
    
f = open('LBCmax_UP.txt', 'r')
y12=f.readlines()
f.close()

for i in range(0,10000):
    y12[i]=float(y12[i])

""" LBC DOWN """
f = open('LBCma0_DOWN.txt', 'r')
y13=f.readlines()
f.close()

for i in range(0,10000):
    y13[i]=float(y13[i])
    
f = open('LBCmax_DOWN.txt', 'r')
y14=f.readlines()
f.close()

for i in range(0,10000):
    y14[i]=float(y14[i])

f = open('LBCmaf_DOWN.txt', 'r')
y15=f.readlines()
f.close()

for i in range(0,10000):
    y15[i]=float(y15[i])


""" SUM UP """
f = open('SUMma0_UP.txt', 'r')
y16=f.readlines()
f.close()

for i in range(0,10000):
    y16[i]=float(y16[i])
    
f = open('SUMmax_UP.txt', 'r')
y17=f.readlines()
f.close()

for i in range(0,10000):
    y17[i]=float(y17[i])


""" SUM DOWN """
f = open('SUMma0_DOWN.txt', 'r')
y18=f.readlines()
f.close()

for i in range(0,10000):
    y18[i]=float(y18[i])
    
f = open('SUMmax_DOWN.txt', 'r')
y19=f.readlines()
f.close()

for i in range(0,10000):
    y19[i]=float(y19[i])

f = open('SUMmaf_DOWN.txt', 'r')
y20=f.readlines()
f.close()

for i in range(0,10000):
    y20[i]=float(y20[i])

"""**************************************************************"""
    
x.extend(range(1,10001))

"""************************* PLOTTING ***************************"""
plt.text(5,1,'Downward Fluxes at 800 km')
""" ECH UP """
plt.subplot(2,4,1)
plt.plot(x,y, 'b')
plt.plot(x,y2, 'k')
plt.title('ECH')
plt.xlabel('Energy [eV]')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])
plt.suptitle('Upward Fluxes at 800 km')

""" ECH DOWN """
plt.subplot(2,4,5)
plt.plot(x,y3, 'b')
plt.plot(x,y4, 'k')
plt.plot(x,y5, 'r')
plt.xlabel('Energy [eV]')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" UBC UP """
plt.subplot(2,4,2)
plt.plot(x,y6, 'b')
plt.plot(x,y7, 'k')
plt.title('UBC')
plt.xlabel('Energy [eV]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

"""" UBC DOWN """
plt.subplot(2,4,6)
plt.plot(x,y8, 'b')
plt.plot(x,y9, 'k')
plt.plot(x,y10, 'r')
plt.xlabel('Energy [eV]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" LBC UP """
plt.subplot(2,4,3)
plt.plot(x,y11, 'b')
plt.plot(x,y12, 'k')
plt.title('LBC')
plt.xlabel('Energy [eV]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

"""" LBC DOWN """
plt.subplot(2,4,7)
plt.plot(x,y13, 'b')
plt.plot(x,y14, 'k')
plt.plot(x,y15, 'r')
plt.xlabel('Energy [eV]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" SUM UP """
plt.subplot(2,4,4)
plt.plot(x,y16, 'b')
plt.plot(x,y17, 'k')
plt.title('SUM')
plt.xlabel('Energy [eV]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" SUM DOWN """
plt.subplot(2,4,8)
plt.plot(x,y18, 'b')
plt.plot(x,y19, 'k')
plt.plot(x,y20, 'r')
plt.xlabel('Energy [eV]')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 8)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])


"""***************************************************************"""

plt.show()








