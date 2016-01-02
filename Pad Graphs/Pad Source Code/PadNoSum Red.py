# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:11:50 2015

@author: Greg
"""

import os
import matplotlib.pyplot as plt
import csv
import re

""" Opening files """

file1 = open('4.6echmaA.txt')
file2 = open('4.6echmaB.txt')
file3 = open('4.6lbcmaA.txt')
file4 = open('4.6lbcmaB.txt')
file5 = open('4.6ubcmaA.txt')
file6 = open('4.6ubcmaB.txt')
file7 = open('6.8echmaA.txt')
file8 = open('6.8echmaB.txt')
file9 = open('6.8lbcmaA.txt')
file10 = open('6.8lbcmaB.txt')
file11 = open('6.8ubcmaA.txt')
file12 = open('6.8ubcmaB.txt')

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

""" Find up data """

Data4_6ECHA = string1[string1.find('equator')+74:len(string1)-6]
Data4_6ECHB = string2[string2.find('equator')+74:len(string2)-6]
Data4_6LBCA = string3[string3.find('equator')+74:len(string3)-6]
Data4_6LBCB = string4[string4.find('equator')+74:len(string4)-6]
Data4_6UBCA = string5[string5.find('equator')+74:len(string5)-6]
Data4_6UBCB = string6[string6.find('equator')+74:len(string6)-6]
Data6_8ECHA = string7[string7.find('equator')+74:len(string7)-6]
Data6_8ECHB = string8[string8.find('equator')+74:len(string8)-6]
Data6_8LBCA = string9[string9.find('equator')+74:len(string9)-6]
Data6_8LBCB = string10[string10.find('equator')+74:len(string10)-6]
Data6_8UBCA = string11[string11.find('equator')+74:len(string11)-6]
Data6_8UBCB = string12[string12.find('equator')+74:len(string12)-6]



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

""" Write data files """

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

""" Convert to list """

u1_2 = list(u1_2)
u1_7 = list(u1_7)
u2_7 = list(u2_7)
u3_7 = list(u3_7)
u4_7 = list(u4_7)
u5_7 = list(u5_7)
u6_7 = list(u6_7)
u7_7 = list(u7_7)
u8_7 = list(u8_7)
u9_7 = list(u9_7)
u10_7 = list(u10_7)
u11_7 = list(u11_7)
u12_7 = list(u12_7)
u1_6 = list(u1_6)
u2_6 = list(u2_6)
u3_6 = list(u3_6)
u4_6 = list(u4_6)
u5_6 = list(u5_6)
u6_6 = list(u6_6)
u7_6 = list(u7_6)
u8_6 = list(u8_6)
u9_6 = list(u9_6)
u10_6 = list(u10_6)
u11_6 = list(u11_6)
u12_6 = list(u12_6)
u1_5 = list(u1_5)
u2_5 = list(u2_5)
u3_5 = list(u3_5)
u4_5 = list(u4_5)
u5_5 = list(u5_5)
u6_5 = list(u6_5)
u7_5 = list(u7_5)
u8_5 = list(u8_5)
u9_5 = list(u9_5)
u10_5 = list(u10_5)
u11_5 = list(u11_5)
u12_5 = list(u12_5)
u1_4 = list(u1_4)
u2_4 = list(u2_4)
u3_4 = list(u3_4)
u4_4 = list(u4_4)
u5_4 = list(u5_4)
u6_4 = list(u6_4)
u7_4 = list(u7_4)
u8_4 = list(u8_4)
u9_4 = list(u9_4)
u10_4 = list(u10_4)
u11_4 = list(u11_4)
u12_4 = list(u12_4)
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
    if '-' in u1_7[i]:
        if 'E' not in u1_7[i]:
            u1_7[i] = '0'
    u1_7[i]=float(u1_7[i])
    
for i in range(0,10000):
    if '-' in u2_7[i]:
        if 'E' not in u2_7[i]:
            u2_7[i] = '0'
    u2_7[i]=float(u2_7[i])

for i in range(0,10000):
    if '-' in u3_7[i]:
        if 'E' not in u3_7[i]:
            u3_7[i] = '0'
    u3_7[i]=float(u3_7[i])
    
for i in range(0,10000):
    if '-' in u4_7[i]:
        if 'E' not in u4_7[i]:
            u4_7[i] = '0'
    u4_7[i]=float(u4_7[i])
    
for i in range(0,10000):
    if '-' in u5_7[i]:
        if 'E' not in u5_7[i]:
            u5_7[i] = '0'
    u5_7[i]=float(u5_7[i])
    
for i in range(0,10000):
    if '-' in u6_7[i]:
        if 'E' not in u6_7[i]:
            u6_7[i] = '0'
    u6_7[i]=float(u6_7[i])

for i in range(0,10000):
    if '-' in u7_7[i]:
        if 'E' not in u7_7[i]:
            u7_7[i] = '0'
    u7_7[i]=float(u7_7[i])
    
for i in range(0,10000):
    if '-' in u8_7[i]:
        if 'E' not in u8_7[i]:
            u8_7[i] = '0'
    u8_7[i]=float(u8_7[i])
    
for i in range(0,10000):
    if '-' in u9_7[i]:
        if 'E' not in u9_7[i]:
            u9_7[i] = '0'
    u9_7[i]=float(u9_7[i])
    
for i in range(0,10000):
    if '-' in u10_7[i]:
        if 'E' not in u10_7[i]:
            u10_7[i] = '0'
    u10_7[i]=float(u10_7[i])
    
for i in range(0,10000):
    if '-' in u11_7[i]:
        if 'E' not in u11_7[i]:
            u11_7[i] = '0'
    u11_7[i]=float(u11_7[i])
    
for i in range(0,10000):
    if '-' in u12_7[i]:
        if 'E' not in u12_7[i]:
            u12_7[i] = '0'
    u12_7[i]=float(u12_7[i])
    
for i in range(0,10000):
    if '-' in u1_6[i]:
        if 'E' not in u1_6[i]:
            u1_6[i] = '0'
    u1_6[i]=float(u1_6[i])
    
for i in range(0,10000):
    if '-' in u2_6[i]:
        if 'E' not in u2_6[i]:
            u2_6[i] = '0'
    u2_6[i]=float(u2_6[i])

for i in range(0,10000):
    if '-' in u3_6[i]:
        if 'E' not in u3_6[i]:
            u3_6[i] = '0'
    u3_6[i]=float(u3_6[i])
    
for i in range(0,10000):
    if '-' in u4_6[i]:
        if 'E' not in u4_6[i]:
            u4_6[i] = '0'
    u4_6[i]=float(u4_6[i])
    
for i in range(0,10000):
    if '-' in u5_6[i]:
        if 'E' not in u5_6[i]:
            u5_6[i] = '0'
    u5_6[i]=float(u5_6[i])
    
for i in range(0,10000):
    if '-' in u6_6[i]:
        if 'E' not in u6_6[i]:
            u6_6[i] = '0'
    u6_6[i]=float(u6_6[i])

for i in range(0,10000):
    if '-' in u7_6[i]:
        if 'E' not in u7_6[i]:
            u7_6[i] = '0'
    u7_6[i]=float(u7_6[i])
    
for i in range(0,10000):
    if '-' in u8_6[i]:
        if 'E' not in u8_6[i]:
            u8_6[i] = '0'
    u8_6[i]=float(u8_6[i])
    
for i in range(0,10000):
    if '-' in u9_6[i]:
        if 'E' not in u9_6[i]:
            u9_6[i] = '0'
    u9_6[i]=float(u9_6[i])
    
for i in range(0,10000):
    if '-' in u10_6[i]:
        if 'E' not in u10_6[i]:
            u10_6[i] = '0'
    u10_6[i]=float(u10_6[i])
    
for i in range(0,10000):
    if '-' in u11_6[i]:
        if 'E' not in u11_6[i]:
            u11_6[i] = '0'
    u11_6[i]=float(u11_6[i])

for i in range(0,10000):
    if '-' in u12_6[i]:
        if 'E' not in u12_6[i]:
            u12_6[i] = '0'
    u12_6[i]=float(u12_6[i])    
    
for i in range(0,10000):
    if '-' in u1_5[i]:
        if 'E' not in u1_5[i]:
            u1_5[i] = '0'
    u1_5[i]=float(u1_5[i])
    
for i in range(0,10000):
    if '-' in u2_5[i]:
        if 'E' not in u2_5[i]:
            u2_5[i] = '0'
    u2_5[i]=float(u2_5[i])
    
for i in range(0,10000):
    if '-' in u3_5[i]:
        if 'E' not in u3_5[i]:
            u3_5[i] = '0'
    u3_5[i]=float(u3_5[i])
    
for i in range(0,10000):
    if '-' in u4_5[i]:
        if 'E' not in u4_5[i]:
            u4_5[i] = '0'
    u4_5[i]=float(u4_5[i])
    
for i in range(0,10000):
    if '-' in u5_5[i]:
        if 'E' not in u5_5[i]:
            u5_5[i] = '0'
    u5_5[i]=float(u5_5[i])
    
for i in range(0,10000):
    if '-' in u6_5[i]:
        if 'E' not in u6_5[i]:
            u6_5[i] = '0'
    u6_5[i]=float(u6_5[i])
    
for i in range(0,10000):
    if '-' in u7_5[i]:
        if 'E' not in u7_5[i]:
            u7_5[i] = '0'
    u7_5[i]=float(u7_5[i])
    
for i in range(0,10000):
    if '-' in u8_5[i]:
        if 'E' not in u8_5[i]:
            u8_5[i] = '0'
    u8_5[i]=float(u8_5[i])
    
for i in range(0,10000):
    if '-' in u9_5[i]:
        if 'E' not in u9_5[i]:
            u9_5[i] = '0'
    u9_5[i]=float(u9_5[i])
    
for i in range(0,10000):
    if '-' in u10_5[i]:
        if 'E' not in u10_5[i]:
            u10_5[i] = '0'
    u10_5[i]=float(u10_5[i])
    
for i in range(0,10000):
    if '-' in u11_5[i]:
        if 'E' not in u11_5[i]:
            u11_5[i] = '0'
    u11_5[i]=float(u11_5[i])
    
for i in range(0,10000):
    if '-' in u12_5[i]:
        if 'E' not in u12_5[i]:
            u12_5[i] = '0'
    u12_5[i]=float(u12_5[i])
    
for i in range(0,10000):
    if '-' in u1_4[i]:
        if 'E' not in u1_4[i]:
            u1_4[i] = '0'
    u1_4[i]=float(u1_4[i])
    
for i in range(0,10000):
    if '-' in u2_4[i]:
        if 'E' not in u2_4[i]:
            u2_4[i] = '0'
    u2_4[i]=float(u2_4[i])
    
for i in range(0,10000):
    if '-' in u3_4[i]:
        if 'E' not in u3_4[i]:
            u3_4[i] = '0'
    u3_4[i]=float(u3_4[i])
    
for i in range(0,10000):
    if '-' in u4_4[i]:
        if 'E' not in u4_4[i]:
            u4_4[i] = '0'
    u4_4[i]=float(u4_4[i])
    
for i in range(0,10000):
    if '-' in u5_4[i]:
        if 'E' not in u5_4[i]:
            u5_4[i] = '0'
    u5_4[i]=float(u5_4[i])
    
for i in range(0,10000):
    if '-' in u6_4[i]:
        if 'E' not in u6_4[i]:
            u6_4[i] = '0'
    u6_4[i]=float(u6_4[i])
    
for i in range(0,10000):
    if '-' in u7_4[i]:
        if 'E' not in u7_4[i]:
            u7_4[i] = '0'
    u7_4[i]=float(u7_4[i])
    
for i in range(0,10000):
    if '-' in u8_4[i]:
        if 'E' not in u8_4[i]:
            u8_4[i] = '0'
    u8_4[i]=float(u8_4[i])
    
for i in range(0,10000):
    if '-' in u9_4[i]:
        if 'E' not in u9_4[i]:
            u9_4[i] = '0'
    u9_4[i]=float(u9_4[i])
    
for i in range(0,10000):
    if '-' in u10_4[i]:
        if 'E' not in u10_4[i]:
            u10_4[i] = '0'
    u10_4[i]=float(u10_4[i])
    
for i in range(0,10000):
    if '-' in u11_4[i]:
        if 'E' not in u11_4[i]:
            u11_4[i] = '0'
    u11_4[i]=float(u11_4[i])
    
for i in range(0,10000):
    if '-' in u12_4[i]:
        if 'E' not in u12_4[i]:
            u12_4[i] = '0'
    u12_4[i]=float(u12_4[i])

for i in range(0,10000):
    if '-' in u1_3[i]:
        if 'E' not in u1_3[i]:
            u1_3[i] = '0'
    u1_3[i]=float(u1_3[i])
    
for i in range(0,10000):
    if '-' in u2_3[i]:
        if 'E' not in u2_3[i]:
            u2_3[i] = '0'
    u2_3[i]=float(u2_3[i])
    
for i in range(0,10000):
    if '-' in u3_3[i]:
        if 'E' not in u3_3[i]:
            u3_3[i] = '0'
    u3_3[i]=float(u3_3[i])
    
for i in range(0,10000):
    if '-' in u4_3[i]:
        if 'E' not in u4_3[i]:
            u4_3[i] = '0'
    u4_3[i]=float(u4_3[i])
    
for i in range(0,10000):
    if '-' in u5_3[i]:
        if 'E' not in u5_3[i]:
            u5_3[i] = '0'
    u5_3[i]=float(u5_3[i])
    
for i in range(0,10000):
    if '-' in u6_3[i]:
        if 'E' not in u6_3[i]:
            u6_3[i] = '0'
    u6_3[i]=float(u6_3[i])
    
for i in range(0,10000):
    if '-' in u7_3[i]:
        if 'E' not in u7_3[i]:
            u7_3[i] = '0'
    u7_3[i]=float(u7_3[i])
    
for i in range(0,10000):
    if '-' in u8_3[i]:
        if 'E' not in u8_3[i]:
            u8_3[i] = '0'
    u8_3[i]=float(u8_3[i])
    
for i in range(0,10000):
    if '-' in u9_3[i]:
        if 'E' not in u9_3[i]:
            u9_3[i] = '0'
    u9_3[i]=float(u9_3[i])
    
for i in range(0,10000):
    if '-' in u10_3[i]:
        if 'E' not in u10_3[i]:
            u10_3[i] = '0'
    u10_3[i]=float(u10_3[i])
    
for i in range(0,10000):
    if '-' in u11_3[i]:
        if 'E' not in u11_3[i]:
            u11_3[i] = '0'
    u11_3[i]=float(u11_3[i])
    
for i in range(0,10000):
    if '-' in u12_3[i]:
        if 'E' not in u12_3[i]:
            u12_3[i] = '0'
    u12_3[i]=float(u12_3[i])


"""************************* PLOTTING ***************************"""
plt.figure(1)

""" ECH for 0, 5, and 10 degrees at L = 4.6 """
plt.subplot(2,3,1)
plt.plot(u1_2,u1_3, 'k', label='0 Degrees With Waves')
plt.plot(u1_2,u2_3, 'r', label='0 Degrees No Waves')
plt.plot(u1_2,u1_4, 'k--')
plt.plot(u1_2,u2_4, 'r--')
plt.plot(u1_2,u1_5, 'k:')
plt.plot(u1_2,u2_5, 'r:')
plt.legend(loc='upper right', fontsize=12)
plt.title('ECH', fontsize = 18, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,10000])
plt.ylim([1,100000000])
plt.suptitle('Energy Distribution for Several Pitch Angles at the Equator at L = 4.6', fontsize = 18, fontweight = 'bold')

""" ECH for 68 and 90 degrees at L = 4.6 """
plt.subplot(2,3,4)
plt.plot(u1_2,u1_6, 'k', label='68 Degrees With Waves')
plt.plot(u1_2,u2_6, 'r', label='68 Degrees No Waves')
plt.plot(u1_2,u1_7, 'k--', label='90 Degrees With Waves')
plt.plot(u1_2,u2_7, 'r--', label='90 Degrees No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.xscale('log')
plt.xlim([1,10000])
plt.ylim([0.0001,100000])

""" UBC for 0, 5, and 10 degrees at L = 4.6 """
plt.subplot(2,3,2)
plt.plot(u1_2,u5_3, 'k')
plt.plot(u1_2,u6_3, 'r')
plt.plot(u1_2,u5_4, 'k--', label= '5 Degrees With Waves')
plt.plot(u1_2,u6_4, 'r--', label='5 Degrees No Waves')
plt.plot(u1_2,u5_5, 'k:')
plt.plot(u1_2,u6_5, 'r:')
plt.legend(loc='upper right', fontsize=12)
plt.title('UBC', fontsize = 18, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,10000])
plt.ylim([1,100000000])

""" UBC for 68 and 90 degrees at L = 4.6 """
plt.subplot(2,3,5)
plt.plot(u1_2,u5_6, 'k')
plt.plot(u1_2,u6_6, 'r')
plt.plot(u1_2,u5_7, 'k--')
plt.plot(u1_2,u6_7, 'r--')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.xscale('log')
plt.xlim([1,10000])
plt.ylim([0.0001,100000])

""" LBC for 0, 5, and 10 degrees at L = 4.6 """
plt.subplot(2,3,3)
plt.plot(u1_2,u3_3, 'k')
plt.plot(u1_2,u4_3, 'r')
plt.plot(u1_2,u3_4, 'k--')
plt.plot(u1_2,u4_4, 'r--')
plt.plot(u1_2,u3_5, 'k:', label='10 Degrees With Waves')
plt.plot(u1_2,u4_5, 'r:', label='10 Degrees No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.title('LBC', fontsize = 18, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,10000])
plt.ylim([1,100000000])

""" LBC for 68 and 90 degrees at L = 4.6 """
plt.subplot(2,3,6)
plt.plot(u1_2,u3_6, 'k')
plt.plot(u1_2,u4_6, 'r')
plt.plot(u1_2,u3_7, 'k--')
plt.plot(u1_2,u4_7, 'r--')
plt.legend(loc='upper right', fontsize=12)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.xscale('log')
plt.xlim([1,10000])
plt.ylim([0.0001,100000])


plt.figure(2)

""" ECH for 0, 5, and 10 degrees at L = 6.8 """
plt.subplot(2,3,1)
plt.plot(u1_2,u7_3, 'k', label='0 Degrees With Waves')
plt.plot(u1_2,u8_3, 'r', label='0 Degrees No Waves')
plt.plot(u1_2,u7_4, 'k--')
plt.plot(u1_2,u8_4, 'r--')
plt.plot(u1_2,u7_5, 'k:')
plt.plot(u1_2,u8_5, 'r:')
plt.legend(loc='upper right', fontsize=12)
plt.title('ECH', fontsize = 18, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,10000])
plt.ylim([1,100000000])
plt.suptitle('Energy Distribution for Several Pitch Angles at the Equator at L = 6.8', fontsize = 18, fontweight = 'bold')

""" ECH for 68 and 90 degrees at L = 6.8"""
plt.subplot(2,3,4)
plt.plot(u1_2,u7_6, 'k', label='68 Degrees With Waves')
plt.plot(u1_2,u8_6, 'r', label='68 Degrees No Waves')
plt.plot(u1_2,u7_7, 'k--', label='90 Degrees With Waves')
plt.plot(u1_2,u8_7, 'r--', label='90 Degrees No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.xscale('log')
plt.xlim([1,10000])
plt.ylim([0.0001,100000])

""" UBC for 0, 5, and 10 degrees at L = 6.8 """
plt.subplot(2,3,2)
plt.plot(u1_2,u11_3, 'k')
plt.plot(u1_2,u12_3, 'r')
plt.plot(u1_2,u11_4, 'k--', label= '5 Degrees With Waves')
plt.plot(u1_2,u12_4, 'r--', label='5 Degrees No Waves')
plt.plot(u1_2,u11_5, 'k:')
plt.plot(u1_2,u12_5, 'r:')
plt.legend(loc='upper right', fontsize=12)
plt.title('UBC', fontsize = 18, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,10000])
plt.ylim([1,100000000])

""" UBC for 68 and 90 degrees at L = 6.8 """
plt.subplot(2,3,5)
plt.plot(u1_2,u11_6, 'k')
plt.plot(u1_2,u12_6, 'r')
plt.plot(u1_2,u11_7, 'k--')
plt.plot(u1_2,u12_7, 'r--')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.xscale('log')
plt.xlim([1,10000])
plt.ylim([0.0001,100000])

""" LBC for 0, 5, and 10 degrees at L = 6.8 """
plt.subplot(2,3,3)
plt.plot(u1_2,u9_3, 'k')
plt.plot(u1_2,u10_3, 'r')
plt.plot(u1_2,u9_4, 'k--')
plt.plot(u1_2,u10_4, 'r--')
plt.plot(u1_2,u9_5, 'k:', label='10 Degrees With Waves')
plt.plot(u1_2,u10_5, 'r:', label='10 Degrees No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.title('LBC', fontsize = 18, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,10000])
plt.ylim([1,100000000])

""" LBC for 68 and 90 degrees at L = 6.8 """
plt.subplot(2,3,6)
plt.plot(u1_2,u9_6, 'k')
plt.plot(u1_2,u10_6, 'r')
plt.plot(u1_2,u9_7, 'k--')
plt.plot(u1_2,u10_7, 'r--')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.xscale('log')
plt.xlim([1,10000])
plt.ylim([0.0001,100000])


plt.show()
