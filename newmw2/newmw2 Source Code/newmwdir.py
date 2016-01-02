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
from scipy import integrate

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
file13 = open('newmw2dirL=6.8.txt')
file14 = open('newmw2dirL=4.6.txt')

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
string13 = file13.read()
string14 = file14.read()

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
file13.close()
file14.close()

""" Find up data """

upData4_6ECHA = string1[string1.find('Upward fluxes')+113:string1.find('Downward')-3]
upData4_6ECHB = string2[string2.find('Upward fluxes')+113:string2.find('Downward')-3]
upData4_6LBCA = string3[string3.find('Upward fluxes')+113:string3.find('Downward')-3]
upData4_6LBCB = string4[string4.find('Upward fluxes')+113:string4.find('Downward')-3]
upData4_6UBCA = string5[string5.find('Upward fluxes')+113:string5.find('Downward')-3]
upData4_6UBCB = string6[string6.find('Upward fluxes')+113:string6.find('Downward')-3]
upData6_8ECHA = string7[string7.find('Upward fluxes')+113:string7.find('Downward')-3]
upData6_8ECHB = string8[string8.find('Upward fluxes')+113:string8.find('Downward')-3]
upData6_8LBCA = string9[string9.find('Upward fluxes')+113:string9.find('Downward')-3]
upData6_8LBCB = string10[string10.find('Upward fluxes')+113:string10.find('Downward')-3]
upData6_8UBCA = string11[string11.find('Upward fluxes')+113:string11.find('Downward')-3]
upData6_8UBCB = string12[string12.find('Upward fluxes')+113:string12.find('Downward')-3]
upData6_8newmw = string13[string13.find('Upward fluxes')+113:string13.find('Downward')-6]
upData4_6newmw = string14[string14.find('Upward fluxes')+113:string14.find('Downward')-6]
""" Find down data """

downData4_6ECHA = string1[string1.find('Downward')+115:len(string1)-3]
downData4_6ECHB = string2[string2.find('Downward')+115:len(string2)-3]
downData4_6LBCA = string3[string3.find('Downward')+115:len(string3)-3]
downData4_6LBCB = string4[string4.find('Downward')+115:len(string4)-3]
downData4_6UBCA = string5[string5.find('Downward')+115:len(string5)-3]
downData4_6UBCB = string6[string6.find('Downward')+115:len(string6)-3]
downData6_8ECHA = string7[string7.find('Downward')+115:len(string7)-3]
downData6_8ECHB = string8[string8.find('Downward')+115:len(string8)-3]
downData6_8LBCA = string9[string9.find('Downward')+115:len(string9)-3]
downData6_8LBCB = string10[string10.find('Downward')+115:len(string10)-3]
downData6_8UBCA = string11[string11.find('Downward')+115:len(string11)-3]
downData6_8UBCB = string12[string12.find('Downward')+115:len(string12)-3]
downData6_8newmw = string13[string13.find('Downward')+115:len(string13)-6]
downData4_6newmw = string14[string14.find('Downward')+115:len(string14)-6]

""" Rewrite with single spaces """

upData4_6ECHA = re.sub(' +', ' ', upData4_6ECHA)
upData4_6ECHB = re.sub(' +', ' ', upData4_6ECHB)
upData4_6LBCA = re.sub(' +', ' ', upData4_6LBCA)
upData4_6LBCB = re.sub(' +', ' ', upData4_6LBCB)
upData4_6UBCA = re.sub(' +', ' ', upData4_6UBCA)
upData4_6UBCB = re.sub(' +', ' ', upData4_6UBCB)
upData6_8ECHA = re.sub(' +', ' ', upData6_8ECHA)
upData6_8ECHB = re.sub(' +', ' ', upData6_8ECHB)
upData6_8LBCA = re.sub(' +', ' ', upData6_8LBCA)
upData6_8LBCB = re.sub(' +', ' ', upData6_8LBCB)
upData6_8UBCA = re.sub(' +', ' ', upData6_8UBCA)
upData6_8UBCB = re.sub(' +', ' ', upData6_8UBCB)
upData6_8newmw = re.sub(' +', ' ', upData6_8newmw)
upData4_6newmw = re.sub(' +', ' ', upData4_6newmw)


downData4_6ECHA = re.sub(' +', ' ', downData4_6ECHA)
downData4_6ECHB = re.sub(' +', ' ', downData4_6ECHB)
downData4_6LBCA = re.sub(' +', ' ', downData4_6LBCA)
downData4_6LBCB = re.sub(' +', ' ', downData4_6LBCB)
downData4_6UBCA = re.sub(' +', ' ', downData4_6UBCA)
downData4_6UBCB = re.sub(' +', ' ', downData4_6UBCB)
downData6_8ECHA = re.sub(' +', ' ', downData6_8ECHA)
downData6_8ECHB = re.sub(' +', ' ', downData6_8ECHB)
downData6_8LBCA = re.sub(' +', ' ', downData6_8LBCA)
downData6_8LBCB = re.sub(' +', ' ', downData6_8LBCB)
downData6_8UBCA = re.sub(' +', ' ', downData6_8UBCA)
downData6_8UBCB = re.sub(' +', ' ', downData6_8UBCB)
downData6_8newmw = re.sub(' +', ' ', downData6_8newmw)
downData4_6newmw = re.sub(' +', ' ', downData4_6newmw)

""" Write up/down files """

file1 = open('upData4_6ECHA.txt', 'w')
file1.write(upData4_6ECHA)
file1.close()
file2 = open('upData4_6ECHB.txt', 'w')
file2.write(upData4_6ECHB)
file2.close()
file3 = open('upData4_6LBCA.txt', 'w')
file3.write(upData4_6LBCA)
file3.close()
file4 = open('upData4_6LBCB.txt', 'w')
file4.write(upData4_6LBCB)
file4.close()
file5 = open('upData4_6UBCA.txt', 'w')
file5.write(upData4_6UBCA)
file5.close()
file6 = open('upData4_6UBCB.txt', 'w')
file6.write(upData4_6UBCB)
file6.close()
file7 = open('upData6_8ECHA.txt', 'w')
file7.write(upData6_8ECHA)
file7.close()
file8 = open('upData6_8ECHB.txt', 'w')
file8.write(upData6_8ECHB)
file8.close()
file9 = open('upData6_8LBCA.txt', 'w')
file9.write(upData6_8LBCA)
file9.close()
file10 = open('upData6_8LBCB.txt', 'w')
file10.write(upData6_8LBCB)
file10.close()
file11 = open('upData6_8UBCA.txt', 'w')
file11.write(upData6_8UBCA)
file11.close()
file12 = open('upData6_8UBCB.txt', 'w')
file12.write(upData6_8UBCB)
file12.close()
file13 = open('upData6_8newmw.txt', 'w')
file13.write(upData6_8newmw)
file13.close()
file14 = open('upData4_6newmw.txt', 'w')
file14.write(upData4_6newmw)
file14.close()

file1 = open('downData4_6ECHA.txt', 'w')
file1.write(downData4_6ECHA)
file1.close()
file2 = open('downData4_6ECHB.txt', 'w')
file2.write(downData4_6ECHB)
file2.close()
file3 = open('downData4_6LBCA.txt', 'w')
file3.write(downData4_6LBCA)
file3.close()
file4 = open('downData4_6LBCB.txt', 'w')
file4.write(downData4_6LBCB)
file4.close()
file5 = open('downData4_6UBCA.txt', 'w')
file5.write(downData4_6UBCA)
file5.close()
file6 = open('downData4_6UBCB.txt', 'w')
file6.write(downData4_6UBCB)
file6.close()
file7 = open('downData6_8ECHA.txt', 'w')
file7.write(downData6_8ECHA)
file7.close()
file8 = open('downData6_8ECHB.txt', 'w')
file8.write(downData6_8ECHB)
file8.close()
file9 = open('downData6_8LBCA.txt', 'w')
file9.write(downData6_8LBCA)
file9.close()
file10 = open('downData6_8LBCB.txt', 'w')
file10.write(downData6_8LBCB)
file10.close()
file11 = open('downData6_8UBCA.txt', 'w')
file11.write(downData6_8UBCA)
file11.close()
file12 = open('downData6_8UBCB.txt', 'w')
file12.write(downData6_8UBCB)
file12.close()
file13 = open('downData6_8newmw.txt', 'w')
file13.write(downData6_8newmw)
file13.close()
file14 = open('downData4_6newmw.txt', 'w')
file14.write(downData4_6newmw)
file14.close()

""" CSV reader """

csvrup1 = csv.reader(open('upData4_6ECHA.txt', 'rb'), delimiter = ' ')
csvrup2 = csv.reader(open('upData4_6ECHB.txt', 'rb'), delimiter = ' ')
csvrup3 = csv.reader(open('upData4_6LBCA.txt', 'rb'), delimiter = ' ')
csvrup4 = csv.reader(open('upData4_6LBCB.txt', 'rb'), delimiter = ' ')
csvrup5 = csv.reader(open('upData4_6UBCA.txt', 'rb'), delimiter = ' ')
csvrup6 = csv.reader(open('upData4_6UBCB.txt', 'rb'), delimiter = ' ')
csvrup7 = csv.reader(open('upData6_8ECHA.txt', 'rb'), delimiter = ' ')
csvrup8 = csv.reader(open('upData6_8ECHB.txt', 'rb'), delimiter = ' ')
csvrup9 = csv.reader(open('upData6_8LBCA.txt', 'rb'), delimiter = ' ')
csvrup10 = csv.reader(open('upData6_8LBCB.txt', 'rb'), delimiter = ' ')
csvrup11 = csv.reader(open('upData6_8UBCA.txt', 'rb'), delimiter = ' ')
csvrup12 = csv.reader(open('upData6_8UBCB.txt', 'rb'), delimiter = ' ')
csvrup13 = csv.reader(open('upData6_8newmw.txt', 'rb'), delimiter = ' ')
csvrup14 = csv.reader(open('upData4_6newmw.txt', 'rb'), delimiter = ' ')

csvrdown1 = csv.reader(open('downData4_6ECHA.txt', 'rb'), delimiter = ' ')
csvrdown2 = csv.reader(open('downData4_6ECHB.txt', 'rb'), delimiter = ' ')
csvrdown3 = csv.reader(open('downData4_6LBCA.txt', 'rb'), delimiter = ' ')
csvrdown4 = csv.reader(open('downData4_6LBCB.txt', 'rb'), delimiter = ' ')
csvrdown5 = csv.reader(open('downData4_6UBCA.txt', 'rb'), delimiter = ' ')
csvrdown6 = csv.reader(open('downData4_6UBCB.txt', 'rb'), delimiter = ' ')
csvrdown7 = csv.reader(open('downData6_8ECHA.txt', 'rb'), delimiter = ' ')
csvrdown8 = csv.reader(open('downData6_8ECHB.txt', 'rb'), delimiter = ' ')
csvrdown9 = csv.reader(open('downData6_8LBCA.txt', 'rb'), delimiter = ' ')
csvrdown10 = csv.reader(open('downData6_8LBCB.txt', 'rb'), delimiter = ' ')
csvrdown11 = csv.reader(open('downData6_8UBCA.txt', 'rb'), delimiter = ' ')
csvrdown12 = csv.reader(open('downData6_8UBCB.txt', 'rb'), delimiter = ' ')
csvrdown13 = csv.reader(open('downData6_8newmw.txt', 'rb'), delimiter = ' ')
csvrdown14 = csv.reader(open('downData4_6newmw.txt', 'rb'), delimiter = ' ')

""" Zip """

"""4.6 ECHA"""
u1_1,u1_2,u1_3,u1_4,u1_5,u1_6,u1_7,u1_8,u1_9,u1_10 = zip(*csvrup1) 
"""4.6 ECHB"""
u2_1,u2_2,u2_3,u2_4,u2_5,u2_6,u2_7,u2_8,u2_9,u2_10 = zip(*csvrup2)
"""4.6 LBCA"""
u3_1,u3_2,u3_3,u3_4,u3_5,u3_6,u3_7,u3_8,u3_9,u3_10 = zip(*csvrup3) 
"""4.6 LBCB"""
u4_1,u4_2,u4_3,u4_4,u4_5,u4_6,u4_7,u4_8,u4_9,u4_10 = zip(*csvrup4)
"""4.6 UBCA"""
u5_1,u5_2,u5_3,u5_4,u5_5,u5_6,u5_7,u5_8,u5_9,u5_10 = zip(*csvrup5) 
"""4.6 UBCB"""
u6_1,u6_2,u6_3,u6_4,u6_5,u6_6,u6_7,u6_8,u6_9,u6_10 = zip(*csvrup6)
"""6.8 ECHA"""
u7_1,u7_2,u7_3,u7_4,u7_5,u7_6,u7_7,u7_8,u7_9,u7_10 = zip(*csvrup7) 
"""6.8 ECHB"""
u8_1,u8_2,u8_3,u8_4,u8_5,u8_6,u8_7,u8_8,u8_9,u8_10 = zip(*csvrup8)
"""6.8 LBCA"""
u9_1,u9_2,u9_3,u9_4,u9_5,u9_6,u9_7,u9_8,u9_9,u9_10 = zip(*csvrup9) 
"""6.8 LBCB"""
u10_1,u10_2,u10_3,u10_4,u10_5,u10_6,u10_7,u10_8,u10_9,u10_10 = zip(*csvrup10)
"""6.8 UBCA"""
u11_1,u11_2,u11_3,u11_4,u11_5,u11_6,u11_7,u11_8,u11_9,u11_10 = zip(*csvrup11)
"""6.8 UBCB"""
u12_1,u12_2,u12_3,u12_4,u12_5,u12_6,u12_7,u12_8,u12_9,u12_10 = zip(*csvrup12) 
"""6.8 newmw"""
u13_1,u13_2,u13_3,u13_4,u13_5,u13_6,u13_7,u13_8,u13_9,u13_10 = zip(*csvrup13)
"""4.6 newmw"""
u14_1,u14_2,u14_3,u14_4,u14_5,u14_6,u14_7,u14_8,u14_9,u14_10 = zip(*csvrup14)

"""4.6 ECHA"""
d1_1,d1_2,d1_3,d1_4,d1_5,d1_6,d1_7,d1_8,d1_9,d1_10 = zip(*csvrdown1) 
"""4.6 ECHB"""
d2_1,d2_2,d2_3,d2_4,d2_5,d2_6,d2_7,d2_8,d2_9,d2_10 = zip(*csvrdown2) 
"""4.6 LBCA"""
d3_1,d3_2,d3_3,d3_4,d3_5,d3_6,d3_7,d3_8,d3_9,d3_10 = zip(*csvrdown3) 
"""4.6 LBCB"""
d4_1,d4_2,d4_3,d4_4,d4_5,d4_6,d4_7,d4_8,d4_9,d4_10 = zip(*csvrdown4) 
"""4.6 UBCA"""
d5_1,d5_2,d5_3,d5_4,d5_5,d5_6,d5_7,d5_8,d5_9,d5_10 = zip(*csvrdown5)
"""4.6 UBCB"""
d6_1,d6_2,d6_3,d6_4,d6_5,d6_6,d6_7,d6_8,d6_9,d6_10 = zip(*csvrdown6) 
"""6.8 ECHA"""
d7_1,d7_2,d7_3,d7_4,d7_5,d7_6,d7_7,d7_8,d7_9,d7_10 = zip(*csvrdown7) 
"""6.8 ECHB"""
d8_1,d8_2,d8_3,d8_4,d8_5,d8_6,d8_7,d8_8,d8_9,d8_10 = zip(*csvrdown8) 
"""6.8 LBCA"""
d9_1,d9_2,d9_3,d9_4,d9_5,d9_6,d9_7,d9_8,d9_9,d9_10 = zip(*csvrdown9) 
"""6.8 LBCB"""
d10_1,d10_2,d10_3,d10_4,d10_5,d10_6,d10_7,d10_8,d10_9,d10_10 = zip(*csvrdown10) 
"""6.8 UBCA"""
d11_1,d11_2,d11_3,d11_4,d11_5,d11_6,d11_7,d11_8,d11_9,d11_10 = zip(*csvrdown11) 
"""6.8 UBCB"""
d12_1,d12_2,d12_3,d12_4,d12_5,d12_6,d12_7,d12_8,d12_9,d12_10 = zip(*csvrdown12)
"""6.8 newmw"""
d13_1,d13_2,d13_3,d13_4,d13_5,d13_6,d13_7,d13_8,d13_9,d13_10 = zip(*csvrdown13)
"""4.6 newmw"""
d14_1,d14_2,d14_3,d14_4,d14_5,d14_6,d14_7,d14_8,d14_9,d14_10 = zip(*csvrdown14)

u1_2 = list(u1_2)
u1_10 = list(u1_10)
u2_10 = list(u2_10)
u3_10 = list(u3_10)
u4_10 = list(u4_10)
u5_10 = list(u5_10)
u6_10 = list(u6_10)
u7_10 = list(u7_10)
u8_10 = list(u8_10)
u9_10 = list(u9_10)
u10_10 = list(u10_10)
u11_10 = list(u11_10)
u12_10 = list(u12_10)
u13_10 = list(u13_10)
u14_10 = list(u14_10)
d1_10 = list(d1_10)
d2_10 = list(d2_10)
d3_10 = list(d3_10)
d4_10 = list(d4_10)
d5_10 = list(d5_10)
d6_10 = list(d6_10)
d7_10 = list(d7_10)
d8_10 = list(d8_10)
d9_10 = list(d9_10)
d10_10 = list(d10_10)
d11_10 = list(d11_10)
d12_10 = list(d12_10)
d13_10 = list(d13_10)
d14_10 = list(d14_10)


""" Convert to float """

for i in range(0,10000):
    u1_2[i]=float(u1_2[i])
    
for i in range(0,10000):
    u1_10[i]=float(u1_10[i])
    
for i in range(0,10000):
    u2_10[i]=float(u2_10[i])
    
for i in range(0,10000):
    u3_10[i]=float(u3_10[i])
    
for i in range(0,10000):
    u4_10[i]=float(u4_10[i])
    
for i in range(0,10000):
    u5_10[i]=float(u5_10[i])
    
for i in range(0,10000):
    u6_10[i]=float(u6_10[i])
    
for i in range(0,10000):
    u7_10[i]=float(u7_10[i])
    
for i in range(0,10000):
    u8_10[i]=float(u8_10[i])
    
for i in range(0,10000):
    u9_10[i]=float(u9_10[i])
    
for i in range(0,10000):
    u10_10[i]=float(u10_10[i])
    
for i in range(0,10000):
    u11_10[i]=float(u11_10[i])
    
for i in range(0,10000):
    u12_10[i]=float(u12_10[i])
    
for i in range(0,10000):
    u13_10[i]=float(u13_10[i])
    
for i in range(0,10000):
    u14_10[i]=float(u14_10[i])
    
for i in range(0,10000):
    d1_10[i]=float(d1_10[i])
    
for i in range(0,10000):
    d2_10[i]=float(d2_10[i])
    
for i in range(0,10000):
    d3_10[i]=float(d3_10[i])
    
for i in range(0,10000):
    d4_10[i]=float(d4_10[i])
    
for i in range(0,10000):
    d5_10[i]=float(d5_10[i])
    
for i in range(0,10000):
    d6_10[i]=float(d6_10[i])
    
for i in range(0,10000):
    d7_10[i]=float(d7_10[i])
    
for i in range(0,10000):
    d8_10[i]=float(d8_10[i])
    
for i in range(0,10000):
    d9_10[i]=float(d9_10[i])
    
for i in range(0,10000):
    d10_10[i]=float(d10_10[i])
    
for i in range(0,10000):
    d11_10[i]=float(d11_10[i])
    
for i in range(0,10000):
    d12_10[i]=float(d12_10[i])
    
for i in range(0,10000):
    d13_10[i]=float(d13_10[i])
    
for i in range(0,10000):
    d14_10[i]=float(d14_10[i])

"""************************* PLOTTING ***************************"""
plt.figure(1)
plt.figtext(.25,.475,' Upward and Downward Electron Fluxes at 800 km at L = 6.8', fontsize = 18, fontweight = 'bold')
""" ECH Up and Down L = 4.6 """
plt.subplot(2,4,1)
plt.plot(u1_2,u1_10, 'k', label='Upward Fluxes With Waves')
plt.plot(u1_2,u2_10, 'r', label='Upward Fluxes No Waves')
plt.plot(u1_2,d1_10, 'k--', label='Downward Fluxes With Waves')
plt.plot(u1_2,d2_10, 'r--', label='Downward Fluxes No Waves')
plt.legend(loc='lower left', fontsize=10)
plt.title('ECH', fontsize = 18, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])
plt.suptitle('Upward and Downward Electron Fluxes at 800 km at L = 4.6', fontsize = 18, fontweight = 'bold')

""" ECH Up and DOWN L = 6.8 """
plt.subplot(2,4,5)
plt.plot(u1_2,u7_10, 'k', label='Upward Fluxes With Waves')
plt.plot(u1_2,u8_10, 'r', label='Upward Fluxes No Waves')
plt.plot(u1_2,d7_10, 'k--', label='Downward Fluxes With Waves')
plt.plot(u1_2,d8_10, 'r--', label='Downward Fluxes No Waves')
plt.legend(loc='lower left', fontsize=10)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" UBC UP and Down L = 4.6 """
plt.subplot(2,4,2)
plt.plot(u1_2,u6_10, 'r', label='Upward Fluxes w/ No Waves')
plt.plot(u1_2,u5_10, 'k', label='Upward Fluxes w/ Waves')
plt.plot(u1_2,d6_10, 'r--', label='Downward Fluxes w/ No Waves')
plt.plot(u1_2,d5_10, 'k--', label='Downward Fluxes w/ Waves')
plt.title('UBC', fontsize = 18, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

"""" UBC Up and DOWN L = 6.8 """
plt.subplot(2,4,6)
plt.plot(u1_2,u12_10, 'r', label='Upward Fluxes w/ No Waves')
plt.plot(u1_2,u11_10, 'k', label='Upward Fluxes w/ Waves')
plt.plot(u1_2,d12_10, 'r--', label='Downward Fluxes w/ No Waves')
plt.plot(u1_2,d11_10, 'k--', label='Downward Fluxes w/ Waves')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" LBC UP and Down L = 4.6 """
plt.subplot(2,4,3)
plt.plot(u1_2,u4_10, 'r', label='Upward Fluxes w/ No Waves')
plt.plot(u1_2,u3_10, 'k', label='Upward Fluxes w/ Waves')
plt.plot(u1_2,d4_10, 'r--', label='Downward Fluxes w/ No Waves')
plt.plot(u1_2,d3_10, 'k--', label='Downward Fluxes w/ Waves')
plt.title('LBC', fontsize = 18, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

"""" LBC up and DOWN L = 6.8 """
plt.subplot(2,4,7)
plt.plot(u1_2,u10_10, 'r', label='Upward Fluxes w/ No Waves')
plt.plot(u1_2,u9_10, 'k', label='Upward Fluxes w/ Waves')
plt.plot(u1_2,d10_10, 'r--', label='Downward Fluxes w/ No Waves')
plt.plot(u1_2,d9_10, 'k--', label='Downward Fluxes w/ Waves')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" newmw up and down L = 4.6 """
plt.subplot(2,4,4)
plt.title('New Sum', fontsize = 18, fontweight = 'bold')
plt.plot(u1_2,u2_10, 'r', label='Upward Fluxes w/ No Waves')
plt.plot(u1_2,u14_10, 'k', label='Upward Fluxes w/ Waves')
plt.plot(u1_2,d2_10, 'r--', label='Downward Fluxes w/ No Waves')
plt.plot(u1_2,d14_10, 'k--', label='Downward Fluxes w/ Waves')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" newmw up and down L = 6.8 """
plt.subplot(2,4,8)
plt.plot(u1_2,u10_10, 'r', label='Upward Fluxes w/ No Waves')
plt.plot(u1_2,u13_10, 'k', label='Upward Fluxes w/ Waves')
plt.plot(u1_2,d10_10, 'r--', label='Downward Fluxes w/ No Waves')
plt.plot(u1_2,d13_10, 'k--', label='Downward Fluxes w/ Waves')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

""" Sum Comparison """

sumup=[0]*10000
for i in range(0,10000):
    sumup[i] = u1_10[i] + u3_10[i] + u5_10[i]

sumdown=[0]*10000
for i in range(0,10000):
    sumdown[i] = d1_10[i] + d3_10[i] + d5_10[i]

sumup2=[0]*10000
for i in range(0,10000):
    sumup2[i] = u7_10[i] + u9_10[i] + u11_10[i]

sumdown2=[0]*10000
for i in range(0,10000):
    sumdown2[i] = d7_10[i] + d9_10[i] + d11_10[i]


""" 6.8 Comparison """

plt.figure(2)
plt.subplot(1,2,1)
plt.title('Upward Fluxes')
plt.plot(u1_2,u10_10, 'r', label='No Waves')
plt.plot(u1_2,u13_10, 'k', label='New File')
plt.plot(u1_2,sumup2, 'g', label='Old Sum')
plt.legend(loc='lower left', fontsize=12)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])
plt.suptitle('Electron Fluxes at 800 km at L = 6.8', fontsize = 18, fontweight = 'bold')



plt.subplot(1,2,2)
plt.title('Downward Fluxes')
plt.plot(u1_2,d10_10, 'r', label='No Waves')
plt.plot(u1_2,d13_10, 'k', label='New File')
plt.plot(u1_2,sumdown2, 'g', label='Old Sum')
plt.legend(loc='lower left', fontsize=12)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

plt.tight_layout()

""" 4.6 Comparison """

plt.figure(3)
plt.subplot(1,2,1)
plt.title('Upward Fluxes')
plt.plot(u1_2,u2_10, 'r', label='No Waves')
plt.plot(u1_2,u14_10, 'k', label='New File')
plt.plot(u1_2,sumup, 'g', label='Old Sum')
plt.legend(loc='lower left', fontsize=12)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])
plt.suptitle('Electron Fluxes at 800 km at L = 4.6', fontsize = 18, fontweight = 'bold')



plt.subplot(1,2,2)
plt.title('Downward Fluxes')
plt.plot(u1_2,d2_10, 'r', label='No Waves')
plt.plot(u1_2,d14_10, 'k', label='New File')
plt.plot(u1_2,sumdown, 'g', label='Old Sum')
plt.legend(loc='lower left', fontsize=12)
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

plt.tight_layout()

plt.show()

""" Integration """

Enewmw2_4_6up = np.array(u1_2)*np.array(u14_10)
Enewmw2_4_6down = np.array(u1_2)*np.array(d14_10)
Enewmw2_6_8up = np.array(u1_2)*np.array(u13_10)
Enewmw2_6_8down = np.array(u1_2)*np.array(d13_10)

print "4.6newmw2up low Energy"
a = scipy.integrate.simps(Enewmw2_4_6up[0:598], u1_2[0:598])
print a

print "4.6newmw2up high Energy"
b = scipy.integrate.simps(Enewmw2_4_6up[599:10000], u1_2[599:10000])
print b

print "4.6newmw2up tot Energy"
c = scipy.integrate.simps(Enewmw2_4_6up[0:10000], u1_2[0:10000])
print c

print "4.6newmw2down low Energy"
d = scipy.integrate.simps(Enewmw2_4_6down[0:598], u1_2[0:598])
print d

print "4.6newmw2down high Energy"
e = scipy.integrate.simps(Enewmw2_4_6down[599:10000], u1_2[599:10000])
print e

print "4.6newmw2down tot Energy"
f = scipy.integrate.simps(Enewmw2_4_6down[0:10000], u1_2[0:10000])
print f

print "6.8newmw2up low Energy"
g = scipy.integrate.simps(Enewmw2_6_8up[0:598], u1_2[0:598])
print g

print "6.8newmw2up high Energy"
h = scipy.integrate.simps(Enewmw2_6_8up[599:10000], u1_2[599:10000])
print h

print "6.8newmw2up tot Energy"
i = scipy.integrate.simps(Enewmw2_6_8up[0:10000], u1_2[0:10000])
print i

print "6.8newmw2down low Energy"
j = scipy.integrate.simps(Enewmw2_6_8down[0:598], u1_2[0:598])
print j

print "6.8newmw2down high Energy"
k = scipy.integrate.simps(Enewmw2_6_8down[599:10000], u1_2[599:10000])
print k

print "6.8newmw2down tot Energy"
l = scipy.integrate.simps(Enewmw2_6_8down[0:10000], u1_2[0:10000])
print l

print "4.6newmw2up low Particle"
m = scipy.integrate.simps(u14_10[0:598], u1_2[0:598])
print m

print "4.6newmw2up high Particle"
n = scipy.integrate.simps(u14_10[599:10000], u1_2[599:10000])
print n

print "4.6newmw2up tot Particle"
o = scipy.integrate.simps(u14_10[0:10000], u1_2[0:10000])
print o

print "4.6newmw2down low Particle"
p = scipy.integrate.simps(d14_10[0:598], u1_2[0:598])
print p

print "4.6newmw2down high Particle"
q = scipy.integrate.simps(d14_10[599:10000], u1_2[599:10000])
print q

print "4.6newmw2down tot Particle"
r = scipy.integrate.simps(d14_10[0:10000], u1_2[0:10000])
print r

print "6.8newmw2up low Particle"
s = scipy.integrate.simps(u13_10[0:598], u1_2[0:598])
print s

print "6.8newmw2up high Particle"
t = scipy.integrate.simps(u13_10[599:10000], u1_2[599:10000])
print t

print "6.8newmw2up tot Particle"
u = scipy.integrate.simps(u13_10[0:10000], u1_2[0:10000])
print u

print "6.8newmw2down low Particle"
v = scipy.integrate.simps(d13_10[0:598], u1_2[0:598])
print v

print "6.8newmw2down high Particle"
w = scipy.integrate.simps(d13_10[599:10000], u1_2[599:10000])
print w

print "6.8newmw2down tot Particle"
x = scipy.integrate.simps(d13_10[0:10000], u1_2[0:10000])
print x


