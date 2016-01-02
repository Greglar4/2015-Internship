# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:11:50 2015

@author: Greg
"""

import os
import scipy
import matplotlib.pyplot as plt
import csv
import re
import numpy as np

""" Opening files """

file1 = open('4.6echmaAtra.txt')
file2 = open('4.6echmaBtra.txt')
file3 = open('4.6lbcmaAtra.txt')
file4 = open('4.6lbcmaBtra.txt')
file5 = open('4.6ubcmaAtra.txt')
file6 = open('4.6ubcmaBtra.txt')
file7 = open('6.8echmaAtra.txt')
file8 = open('6.8echmaBtra.txt')
file9 = open('6.8lbcmaAtra.txt')
file10 = open('6.8lbcmaBtra.txt')
file11 = open('6.8ubcmaAtra.txt')
file12 = open('6.8ubcmaBtra.txt')

""" Read files to strings """

string1 = file1.read()
string2 = file2.read()
string3 = file3.read()
string4 = file4.read()
string5 = file5.read()
string6 = file6.read()
string7 = file7.read()
string8 = file8.read()
string9 = file9.read()
string10 = file10.read()
string11 = file11.read()
string12 = file12.read()

""" Close files """

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()
file11.close()
file12.close()

""" Find data """

Data4_6ECHA = string1[string1.find('P2 -')+5:len(string1)-3]
Data4_6ECHB = string2[string2.find('P2 -')+5:len(string2)-3]
Data4_6LBCA = string3[string3.find('P2 -')+5:len(string3)-3]
Data4_6LBCB = string4[string4.find('P2 -')+5:len(string4)-3]
Data4_6UBCA = string5[string5.find('P2 -')+5:len(string5)-3]
Data4_6UBCB = string6[string6.find('P2 -')+5:len(string6)-3]
Data6_8ECHA = string7[string7.find('P2 -')+5:len(string7)-3]
Data6_8ECHB = string8[string8.find('P2 -')+5:len(string8)-3]
Data6_8LBCA = string9[string9.find('P2 -')+5:len(string9)-3]
Data6_8LBCB = string10[string10.find('P2 -')+5:len(string10)-3]
Data6_8UBCA = string11[string11.find('P2 -')+5:len(string11)-3]
Data6_8UBCB = string12[string12.find('P2 -')+5:len(string12)-3]

""" Rewrite with single spaces """

Data4_6ECHA = re.sub(' +', ' ', Data4_6ECHA)
Data4_6ECHB = re.sub(' +', ' ', Data4_6ECHB)
Data4_6LBCA = re.sub(' +', ' ', Data4_6LBCA)
Data4_6LBCB = re.sub(' +', ' ', Data4_6LBCB)
Data4_6UBCA = re.sub(' +', ' ', Data4_6UBCA)
Data4_6UBCB = re.sub(' +', ' ', Data4_6UBCB)
Data6_8ECHA = re.sub(' +', ' ', Data6_8ECHA)
Data6_8ECHB = re.sub(' +', ' ', Data6_8ECHB)
Data6_8LBCA = re.sub(' +', ' ', Data6_8LBCA)
Data6_8LBCB = re.sub(' +', ' ', Data6_8LBCB)
Data6_8UBCA = re.sub(' +', ' ', Data6_8UBCA)
Data6_8UBCB = re.sub(' +', ' ', Data6_8UBCB)

""" Write up/down files """

file1 = open('Data4_6ECHA.txt', 'w')
file1.write(Data4_6ECHA)
file1.close()
file2 = open('Data4_6ECHB.txt', 'w')
file2.write(Data4_6ECHB)
file2.close()
file3 = open('Data4_6LBCA.txt', 'w')
file3.write(Data4_6LBCA)
file3.close()
file4 = open('Data4_6LBCB.txt', 'w')
file4.write(Data4_6LBCB)
file4.close()
file5 = open('Data4_6UBCA.txt', 'w')
file5.write(Data4_6UBCA)
file5.close()
file6 = open('Data4_6UBCB.txt', 'w')
file6.write(Data4_6UBCB)
file6.close()
file7 = open('Data6_8ECHA.txt', 'w')
file7.write(Data6_8ECHA)
file7.close()
file8 = open('Data6_8ECHB.txt', 'w')
file8.write(Data6_8ECHB)
file8.close()
file9 = open('Data6_8LBCA.txt', 'w')
file9.write(Data6_8LBCA)
file9.close()
file10 = open('Data6_8LBCB.txt', 'w')
file10.write(Data6_8LBCB)
file10.close()
file11 = open('Data6_8UBCA.txt', 'w')
file11.write(Data6_8UBCA)
file11.close()
file12 = open('Data6_8UBCB.txt', 'w')
file12.write(Data6_8UBCB)
file12.close()


""" CSV reader """

csvrup1 = csv.reader(open('Data4_6ECHA.txt', 'rb'), delimiter = ' ')
csvrup2 = csv.reader(open('Data4_6ECHB.txt', 'rb'), delimiter = ' ')
csvrup3 = csv.reader(open('Data4_6LBCA.txt', 'rb'), delimiter = ' ')
csvrup4 = csv.reader(open('Data4_6LBCB.txt', 'rb'), delimiter = ' ')
csvrup5 = csv.reader(open('Data4_6UBCA.txt', 'rb'), delimiter = ' ')
csvrup6 = csv.reader(open('Data4_6UBCB.txt', 'rb'), delimiter = ' ')
csvrup7 = csv.reader(open('Data6_8ECHA.txt', 'rb'), delimiter = ' ')
csvrup8 = csv.reader(open('Data6_8ECHB.txt', 'rb'), delimiter = ' ')
csvrup9 = csv.reader(open('Data6_8LBCA.txt', 'rb'), delimiter = ' ')
csvrup10 = csv.reader(open('Data6_8LBCB.txt', 'rb'), delimiter = ' ')
csvrup11 = csv.reader(open('Data6_8UBCA.txt', 'rb'), delimiter = ' ')
csvrup12 = csv.reader(open('Data6_8UBCB.txt', 'rb'), delimiter = ' ')


""" Zip """

"""4.6 ECHA"""
u1_1,u1_2,u1_3,u1_4,u1_5,u1_6,u1_7 = zip(*csvrup1) 
"""4.6 ECHB"""
u2_1,u2_2,u2_3,u2_4,u2_5,u2_6,u2_7 = zip(*csvrup2)
"""4.6 LBCA"""
u3_1,u3_2,u3_3,u3_4,u3_5,u3_6,u3_7 = zip(*csvrup3) 
"""4.6 LBCB"""
u4_1,u4_2,u4_3,u4_4,u4_5,u4_6,u4_7 = zip(*csvrup4)
"""4.6 UBCA"""
u5_1,u5_2,u5_3,u5_4,u5_5,u5_6,u5_7 = zip(*csvrup5) 
"""4.6 UBCB"""
u6_1,u6_2,u6_3,u6_4,u6_5,u6_6,u6_7 = zip(*csvrup6)
"""6.8 ECHA"""
u7_1,u7_2,u7_3,u7_4,u7_5,u7_6,u7_7 = zip(*csvrup7) 
"""6.8 ECHB"""
u8_1,u8_2,u8_3,u8_4,u8_5,u8_6,u8_7 = zip(*csvrup8)
"""6.8 LBCA"""
u9_1,u9_2,u9_3,u9_4,u9_5,u9_6,u9_7 = zip(*csvrup9) 
"""6.8 LBCB"""
u10_1,u10_2,u10_3,u10_4,u10_5,u10_6,u10_7 = zip(*csvrup10)
"""6.8 UBCA"""
u11_1,u11_2,u11_3,u11_4,u11_5,u11_6,u11_7 = zip(*csvrup11)
"""6.8 UBCB"""
u12_1,u12_2,u12_3,u12_4,u12_5,u12_6,u12_7 = zip(*csvrup12) 


u1_2 = list(u1_2)
u1_3 = list(u1_3)
u2_3 = list(u2_3)
u3_3 = list(u3_3)
u4_3 = list(u4_3)
u5_3 = list(u5_3)
u6_3 = list(u6_3)
u7_3 = list(u7_3)
u8_3 = list(u8_3)
u9_3 = list(u9_3)
u10_3 = list(u10_3)
u11_3 = list(u11_3)
u12_3 = list(u12_3)

""" Convert to float """

for i in range(0,10000):
    u1_2[i]=float(u1_2[i])
    
for i in range(0,10000):
    u1_3[i]=float(u1_3[i])
    
for i in range(0,10000):
    u2_3[i]=float(u2_3[i])
    
for i in range(0,10000):
    u3_3[i]=float(u3_3[i])
    
for i in range(0,10000):
    u4_3[i]=float(u4_3[i])
    
for i in range(0,10000):
    u5_3[i]=float(u5_3[i])
    
for i in range(0,10000):
    u6_3[i]=float(u6_3[i])
    
for i in range(0,10000):
    u7_3[i]=float(u7_3[i])
    
for i in range(0,10000):
    u8_3[i]=float(u8_3[i])
    
for i in range(0,10000):
    u9_3[i]=float(u9_3[i])
    
for i in range(0,10000):
    u10_3[i]=float(u10_3[i])
    
for i in range(0,10000):
    u11_3[i]=float(u11_3[i])
    
for i in range(0,10000):
    u12_3[i]=float(u12_3[i])
    


Eps4_6NoWaves = [0]*599
Eps4_6ECH = [0]*599
Eps4_6UBC = [0]*599
Eps4_6LBC = [0]*599
Eps6_8NoWaves = [0]*599
Eps6_8ECH = [0]*599
Eps6_8UBC = [0]*599
Eps6_8LBC = [0]*599

for i in range(0,599):
    Eps4_6NoWaves[i] = 1-u2_3[i]
for i in range(0,599):
    Eps4_6ECH[i] = 1-u1_3[i]
for i in range(0,599):
    Eps4_6LBC[i] = 1-u3_3[i]
for i in range(0,599):
    Eps4_6UBC[i] = 1-u5_3[i]

for i in range(0,599):
    Eps6_8NoWaves[i] = 1-u8_3[i]
for i in range(0,599):
    Eps6_8ECH[i] = 1-u7_3[i]
for i in range(0,599):
    Eps6_8LBC[i] = 1-u9_3[i]
for i in range(0,599):
    Eps6_8UBC[i] = 1-u11_3[i]
    
plt.subplot(1,2,1)
plt.plot(u1_2[0:599],Eps4_6NoWaves, 'k', label='Epsilon No Waves')
plt.plot(u1_2[0:599],Eps4_6ECH, 'r', label='Epsilon ECH')
plt.plot(u1_2[0:599],Eps4_6LBC, 'b', label='Epsilon LBC')
plt.plot(u1_2[0:599],Eps4_6UBC, 'g', label='Epsilon UBC')
plt.legend(loc='lower left')
plt.title('L = 4.6')
plt.ylabel('Epsilon')
plt.xlabel('Energy (eV)')
plt.xscale('log')
plt.suptitle('Epsilon as a Function of Energy')

plt.subplot(1,2,2)
plt.plot(u1_2[0:599],Eps6_8NoWaves, 'k', label='Epsilon No Waves')
plt.plot(u1_2[0:599],Eps6_8ECH, 'r', label='Epsilon ECH')
plt.plot(u1_2[0:599],Eps6_8LBC, 'b', label='Epsilon LBC')
plt.plot(u1_2[0:599],Eps6_8UBC, 'g', label='Epsilon UBC')
plt.title('L = 6.8')
plt.ylabel('Epsilon')
plt.xlabel('Energy (eV)')
plt.xscale('log')



