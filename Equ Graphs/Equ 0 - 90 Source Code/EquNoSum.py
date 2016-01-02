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

Data4_6ECHA = string1[string1.find('Theta')+74:string1.find('91.1')-3]
Data4_6ECHB = string2[string2.find('Theta')+74:string2.find('91.1')-3]
Data4_6LBCA = string3[string3.find('Theta')+74:string3.find('91.1')-3]
Data4_6LBCB = string4[string4.find('Theta')+74:string4.find('91.1')-3]
Data4_6UBCA = string5[string5.find('Theta')+74:string5.find('91.1')-3]
Data4_6UBCB = string6[string6.find('Theta')+74:string6.find('91.1')-3]
Data6_8ECHA = string7[string7.find('Theta')+74:string7.find('91.1')-3]
Data6_8ECHB = string8[string8.find('Theta')+74:string8.find('91.1')-3]
Data6_8LBCA = string9[string9.find('Theta')+74:string9.find('91.1')-3]
Data6_8LBCB = string10[string10.find('Theta')+74:string10.find('91.1')-3]
Data6_8UBCA = string11[string11.find('Theta')+74:string11.find('91.1')-3]
Data6_8UBCB = string12[string12.find('Theta')+74:string12.find('91.1')-3]



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
u1_1,u1_2,u1_3,u1_4,u1_5,u1_6,u1_7,u1_8 = zip(*csvrup1) 
"""4.6 ECHB"""
u2_1,u2_2,u2_3,u2_4,u2_5,u2_6,u2_7,u2_8 = zip(*csvrup2)
"""4.6 LBCA"""
u3_1,u3_2,u3_3,u3_4,u3_5,u3_6,u3_7,u3_8 = zip(*csvrup3) 
"""4.6 LBCB"""
u4_1,u4_2,u4_3,u4_4,u4_5,u4_6,u4_7,u4_8 = zip(*csvrup4)
"""4.6 UBCA"""
u5_1,u5_2,u5_3,u5_4,u5_5,u5_6,u5_7,u5_8 = zip(*csvrup5) 
"""4.6 UBCB"""
u6_1,u6_2,u6_3,u6_4,u6_5,u6_6,u6_7,u6_8 = zip(*csvrup6)
"""6.8 ECHA"""
u7_1,u7_2,u7_3,u7_4,u7_5,u7_6,u7_7,u7_8 = zip(*csvrup7) 
"""6.8 ECHB"""
u8_1,u8_2,u8_3,u8_4,u8_5,u8_6,u8_7,u8_8 = zip(*csvrup8)
"""6.8 LBCA"""
u9_1,u9_2,u9_3,u9_4,u9_5,u9_6,u9_7,u9_8 = zip(*csvrup9) 
"""6.8 LBCB"""
u10_1,u10_2,u10_3,u10_4,u10_5,u10_6,u10_7,u10_8 = zip(*csvrup10)
"""6.8 UBCA"""
u11_1,u11_2,u11_3,u11_4,u11_5,u11_6,u11_7,u11_8 = zip(*csvrup11)
"""6.8 UBCB"""
u12_1,u12_2,u12_3,u12_4,u12_5,u12_6,u12_7,u12_8 = zip(*csvrup12) 

""" Convert to list """

u1_2 = list(u1_2)
u1_8 = list(u1_8)
u2_8 = list(u2_8)
u3_8 = list(u3_8)
u4_8 = list(u4_8)
u5_8 = list(u5_8)
u6_8 = list(u6_8)
u7_8 = list(u7_8)
u8_8 = list(u8_8)
u9_8 = list(u9_8)
u10_8 = list(u10_8)
u11_8 = list(u11_8)
u12_8 = list(u12_8)
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

""" Convert to float """

for i in range(0,136):
    u1_2[i]=float(u1_2[i])
    
for i in range(0,136):
    u1_8[i]=float(u1_8[i])
    
for i in range(0,136):
    u2_8[i]=float(u2_8[i])
    
for i in range(0,136):
    u3_8[i]=float(u3_8[i])
    
for i in range(0,136):
    u4_8[i]=float(u4_8[i])
    
for i in range(0,136):
    u5_8[i]=float(u5_8[i])
    
for i in range(0,136):
    u6_8[i]=float(u6_8[i])
    
for i in range(0,136):
    u7_8[i]=float(u7_8[i])
    
for i in range(0,136):
    u8_8[i]=float(u8_8[i])
    
for i in range(0,136):
    u9_8[i]=float(u9_8[i])
    
for i in range(0,136):
    u10_8[i]=float(u10_8[i])
    
for i in range(0,136):
    u11_8[i]=float(u11_8[i])
    
for i in range(0,136):
    u12_8[i]=float(u12_8[i])
    
for i in range(0,136):
    u1_5[i]=float(u1_5[i])
    
for i in range(0,136):
    u2_5[i]=float(u2_5[i])
    
for i in range(0,136):
    u3_5[i]=float(u3_5[i])
    
for i in range(0,136):
    u4_5[i]=float(u4_5[i])
    
for i in range(0,136):
    u5_5[i]=float(u5_5[i])
    
for i in range(0,136):
    u6_5[i]=float(u6_5[i])
    
for i in range(0,136):
    u7_5[i]=float(u7_5[i])
    
for i in range(0,136):
    u8_5[i]=float(u8_5[i])
    
for i in range(0,136):
    u9_5[i]=float(u9_5[i])
    
for i in range(0,136):
    u10_5[i]=float(u10_5[i])
    
for i in range(0,136):
    u11_5[i]=float(u11_5[i])
    
for i in range(0,136):
    u12_5[i]=float(u12_5[i])


"""************************* PLOTTING ***************************"""
plt.figure(1)
plt.figtext(.2113,.5,'Pitch Angle Distribution at the Equator for 10 eV and 50 eV at L = 6.8', fontsize = 18, fontweight = 'bold')
""" ECH at 10 and 50 EV at L = 4.6 """
plt.subplot(2,3,1)
plt.plot(u1_2,u1_5, 'k--', label='10 eV w/ Waves')
plt.plot(u1_2,u2_5, 'r--', label='10 eV w/ No Waves')
plt.plot(u1_2,u1_8, 'k', label='50 eV w/ Waves')
plt.plot(u1_2,u2_8, 'r', label='50 eV w/ No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.title('ECH', fontsize = 18, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.ylim([1,100000000])
plt.suptitle('Pitch Angle Distribution at the Equator for 10 eV and 50 eV at L = 4.6', fontsize = 18, fontweight = 'bold')

""" ECH at 10 and 50 eV at L = 6.8 """
plt.subplot(2,3,4)
plt.plot(u1_2,u7_5, 'k--', label='10 eV w/ Waves')
plt.plot(u1_2,u8_5, 'r--', label='10 eV w/ No Waves')
plt.plot(u1_2,u7_8, 'k', label='50 eV w/ Waves')
plt.plot(u1_2,u8_8, 'r', label='50 eV w/ No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.xlabel('Pitch Angle (degrees)', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.ylim([1,100000000])

""" UBC at 10 and 50 eV at L = 4.6 """
plt.subplot(2,3,2)
plt.plot(u1_2,u6_8, 'r', label='50 eV w/ No Waves')
plt.plot(u1_2,u5_8, 'k', label='50 eV w/ Waves')
plt.plot(u1_2,u6_5, 'r--', label='10 eV w/ No Waves')
plt.plot(u1_2,u5_5, 'k--', label='10 eV Fluxes w/ Waves')
plt.title('UBC', fontsize = 18, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.ylim([1,100000000])

"""" UBC at 10 and 50 eV at L = 6.8 """
plt.subplot(2,3,5)
plt.plot(u1_2,u12_8, 'r', label='50 eV w/ No Waves')
plt.plot(u1_2,u11_8, 'k', label='50 eV w/ Waves')
plt.plot(u1_2,u12_5, 'r--', label='10 eV w/ No Waves')
plt.plot(u1_2,u11_5, 'k--', label='10 eV w/ Waves')
plt.xlabel('Pitch Angle (degrees)', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.ylim([1,100000000])

""" LBC at 10 and 50 eV at L = 4.6 """
plt.subplot(2,3,3)
plt.plot(u1_2,u4_8, 'r', label='50 eV w/ No Waves')
plt.plot(u1_2,u3_8, 'k', label='50 eV w/ Waves')
plt.plot(u1_2,u4_5, 'r--', label='10 eV w/ No Waves')
plt.plot(u1_2,u3_5, 'k--', label='10 eV w/ Waves')
plt.title('LBC', fontsize = 18, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.ylim([1,100000000])

"""" LBC at 10 and 50 eV at L = 6.8 """
plt.subplot(2,3,6)
plt.plot(u1_2,u10_8, 'r', label='50 eV w/ No Waves')
plt.plot(u1_2,u9_8, 'k', label='50 eV w/ Waves')
plt.plot(u1_2,u10_5, 'r--', label='10 eV w/ No Waves')
plt.plot(u1_2,u9_5, 'k--', label='10 eV w/ Waves')
plt.xlabel('Pitch Angle (degrees)', fontsize = 16, fontweight = 'bold')
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xticks(fontsize = 14)
plt.yscale('log')
plt.ylim([1,100000000])

plt.tight_layout()

plt.show()


