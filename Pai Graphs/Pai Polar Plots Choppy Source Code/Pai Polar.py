# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:11:50 2015

@author: Greg
"""

import os
import matplotlib.pyplot as plt
import csv
import re
import math
import numpy as np
import scipy
from scipy.interpolate import spline


def columns_to_list(num_cols, cols, csvr):
    """
    convert the columns of a csv and then return only the columns we are intersted in
    :param num_cols:  number of columns in the csv file
    :param cols:  a tuple of column indexes for the columns we want returned
    :param csvr:  csv file
    :return: tuple of column data
    """
    ret_list = []
    temp_tuple = ()
    # If you like Add a check her to make sure each of the columns in cols is less than num_cols.

    if num_cols == 2:
        c1, c2 = zip(*csvr)
        temp_tuple = (c1, c2)
    elif num_cols == 3:
        c1, c2, c3 = zip(*csvr)
        temp_tuple = (c1, c2, c3)
    elif num_cols == 4:
        c1, c2, c3, c4 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4)
    elif num_cols == 5:
        c1, c2, c3, c4, c5 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5)
    elif num_cols == 6:
        c1, c2, c3, c4, c5, c6 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6)
    elif num_cols == 7:
        c1, c2, c3, c4, c5, c6, c7 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7)
    elif num_cols == 8:
        c1, c2, c3, c4, c5, c6, c7, c8 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8)
    elif num_cols == 9:
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9)
    elif num_cols == 10:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
    elif num_cols == 11:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11)
    elif num_cols == 12:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12)
    elif num_cols == 13:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13)
    elif num_cols == 14:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14)
    elif num_cols == 15:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15)
    elif num_cols == 16:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16)
    elif num_cols == 17:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17)
    elif num_cols == 18:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18)
    elif num_cols == 19:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19)
    elif num_cols == 20:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20)
    elif num_cols == 21:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21)
    elif num_cols == 22:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22)
    elif num_cols == 23:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23 = zip(*csvr)
        temp_tuple = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23)

    for col in cols:
        ret_list.append(list(temp_tuple[col]))

    return list(ret_list)

""" Opening files """

file1 = open('4.6echmaApai.txt')
file2 = open('4.6lbcmaApai.txt')
file3 = open('4.6ubcmaApai.txt')
file4 = open('4.6ubcmaBpai.txt')
file5 = open('6.8echmaApai.txt')
file6 = open('6.8lbcmaApai.txt')
file7 = open('6.8lbcmaBpai.txt')
file8 = open('6.8ubcmaApai.txt')

""" Read files to strings """

string1 = file1.read()
string2 = file2.read()
string3 = file3.read()
string4 = file4.read()
string5 = file5.read()
string6 = file6.read()
string7 = file7.read()
string8 = file8.read()


""" Close files """

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()


""" Find up data """

Data4_6ECHA = string1[string1.find('80000000')+123:string1.find('Second ionosphere')-2]
Data4_6LBCA = string2[string2.find('80000000')+123:string2.find('Second ionosphere')-2]
Data4_6UBCA = string3[string3.find('80000000')+123:string3.find('Second ionosphere')-2]
Data4_6UBCB = string4[string4.find('80000000')+123:string4.find('Second ionosphere')-2]
Data6_8ECHA = string5[string5.find('80000000')+123:string5.find('Second ionosphere')-2]
Data6_8LBCA = string6[string6.find('80000000')+123:string6.find('Second ionosphere')-2]
Data6_8LBCB = string7[string7.find('80000000')+123:string7.find('Second ionosphere')-2]
Data6_8UBCA = string8[string8.find('80000000')+123:string8.find('Second ionosphere')-2]


""" Rewrite with single spaces """

Data4_6ECHA = re.sub(' +', ' ', Data4_6ECHA)
Data4_6LBCA = re.sub(' +', ' ', Data4_6LBCA)
Data4_6UBCA = re.sub(' +', ' ', Data4_6UBCA)
Data4_6UBCB = re.sub(' +', ' ', Data4_6UBCB)
Data6_8ECHA = re.sub(' +', ' ', Data6_8ECHA)
Data6_8LBCA = re.sub(' +', ' ', Data6_8LBCA)
Data6_8LBCB = re.sub(' +', ' ', Data6_8LBCB)
Data6_8UBCA = re.sub(' +', ' ', Data6_8UBCA)

""" Write up/down files """

file1 = open('Data4_6ECHA.txt', 'w')
file1.write(Data4_6ECHA)
file1.close()
file2 = open('Data4_6LBCA.txt', 'w')
file2.write(Data4_6LBCA)
file2.close()
file3 = open('Data4_6UBCA.txt', 'w')
file3.write(Data4_6UBCA)
file3.close()
file4 = open('Data4_6UBCB.txt', 'w')
file4.write(Data4_6UBCB)
file4.close()
file5 = open('Data6_8ECHA.txt', 'w')
file5.write(Data6_8ECHA)
file5.close()
file6 = open('Data6_8LBCA.txt', 'w')
file6.write(Data6_8LBCA)
file6.close()
file7 = open('Data6_8LBCB.txt', 'w')
file7.write(Data6_8LBCB)
file7.close()
file8 = open('Data6_8UBCA.txt', 'w')
file8.write(Data6_8UBCA)
file8.close()


""" CSV reader """

csvr1 = csv.reader(open('Data4_6ECHA.txt', 'rb'), delimiter = ' ')
csvr2 = csv.reader(open('Data4_6LBCA.txt', 'rb'), delimiter = ' ')
csvr3 = csv.reader(open('Data4_6UBCA.txt', 'rb'), delimiter = ' ')
csvr4 = csv.reader(open('Data4_6UBCB.txt', 'rb'), delimiter = ' ')
csvr5 = csv.reader(open('Data6_8ECHA.txt', 'rb'), delimiter = ' ')
csvr6 = csv.reader(open('Data6_8LBCA.txt', 'rb'), delimiter = ' ')
csvr7 = csv.reader(open('Data6_8LBCB.txt', 'rb'), delimiter = ' ')
csvr8 = csv.reader(open('Data6_8UBCA.txt', 'rb'), delimiter = ' ')

""" Zip """

"""4.6 ECHA"""
ECHA4_6 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr1)
"""4.6 LBCA"""
LBCA4_6 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr2) 
"""4.6 UBCA"""
UBCA4_6 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr3) 
"""4.6 UBCB"""
UBCB4_6 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr4)
"""6.8 ECHA"""
ECHA6_8 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr5) 
"""6.8 LBCA"""
LBCA6_8 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr6) 
"""6.8 LBCB"""
LBCB6_8 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr7)
"""6.8 UBCA"""
UBCA6_8 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvr8)

data = [ECHA4_6, LBCA4_6, UBCA4_6, UBCB4_6, ECHA6_8, LBCA6_8, LBCB6_8, UBCA6_8]


""" Convert to float """

for k in range(0,8):
    for j in range(0,9):
        for i in range(0,9):
            data[k][j][i] = float(data[k][j][i])
            
""" Append """
            
for i in range(0,8):
    data[0][0].append(180+180-data[0][0][7-i])
    
for k in range(0,8):
    for j in range(1,9):
        for i in range(0,8):
            data[k][j].append(data[k][j][7-i])
            
""" Divide by omni directional flux """

""" 4.6 No Waves """

""" 2 eV """

for i in range(0,17):
    data[3][2][i]=data[3][2][i]/1.237E+06
    
""" 5 eV """

for i in range(0,17):
    data[3][3][i]=data[3][3][i]/2.316E+06

""" 10 eV """

for i in range(0,17):
    data[3][4][i]=data[3][4][i]/1.792E+06
    
""" 20 eV """

for i in range(0,17):
    data[3][6][i]=data[3][6][i]/8.711E+05
    
""" 30 eV """

for i in range(0,17):
    data[3][7][i]=data[3][7][i]/5.046E+05
    
""" 50 eV """

for i in range(0,17):
    data[3][8][i]=data[3][8][i]/2.481E+05
    
""" 4.6 ECH """

""" 2 eV """

for i in range(0,17):
    data[0][2][i]=data[0][2][i]/1.154E+06
    
""" 5 eV """

for i in range(0,17):
    data[0][3][i]=data[0][3][i]/2.140E+06

""" 10 eV """

for i in range(0,17):
    data[0][4][i]=data[0][4][i]/1.569E+06
    
""" 20 eV """

for i in range(0,17):
    data[0][6][i]=data[0][6][i]/6.724E+05
    
""" 30 eV """

for i in range(0,17):
    data[0][7][i]=data[0][7][i]/3.626E+05
    
""" 50 eV """

for i in range(0,17):
    data[0][8][i]=data[0][8][i]/1.830E+05
    
""" 4.6 LBC """

""" 2 eV """

for i in range(0,17):
    data[1][2][i]=data[1][2][i]/1.238E+06
    
""" 5 eV """

for i in range(0,17):
    data[1][3][i]=data[1][3][i]/2.319E+06

""" 10 eV """

for i in range(0,17):
    data[1][4][i]=data[1][4][i]/1.795E+06
    
""" 20 eV """

for i in range(0,17):
    data[1][6][i]=data[1][6][i]/8.732E+05
    
""" 30 eV """

for i in range(0,17):
    data[1][7][i]=data[1][7][i]/5.062E+05
    
""" 50 eV """

for i in range(0,17):
    data[1][8][i]=data[1][8][i]/2.490E+05
    
""" 4.6 UBC """

""" 2 eV """

for i in range(0,17):
    data[2][2][i]=data[2][2][i]/9.374E+05
    
""" 5 eV """

for i in range(0,17):
    data[2][3][i]=data[2][3][i]/1.712E+06

""" 10 eV """

for i in range(0,17):
    data[2][4][i]=data[2][4][i]/1.147E+06
    
""" 20 eV """

for i in range(0,17):
    data[2][6][i]=data[2][6][i]/4.097E+05
    
""" 30 eV """

for i in range(0,17):
    data[2][7][i]=data[2][7][i]/1.962E+05
    
""" 50 eV """

for i in range(0,17):
    data[2][8][i]=data[2][8][i]/8.476E+04
    
""" 6.8 No Waves """

""" 2 eV """

for i in range(0,17):
    data[6][2][i]=data[6][2][i]/1.296E+06
    
""" 5 eV """

for i in range(0,17):
    data[6][3][i]=data[6][3][i]/2.357E+06

""" 10 eV """

for i in range(0,17):
    data[6][4][i]=data[6][4][i]/1.661E+06
    
""" 20 eV """

for i in range(0,17):
    data[6][6][i]=data[6][6][i]/7.348E+05
    
""" 30 eV """

for i in range(0,17):
    data[6][7][i]=data[6][7][i]/4.271E+05
    
""" 50 eV """

for i in range(0,17):
    data[6][8][i]=data[6][8][i]/2.182E+05
    
""" 6.8 ECH """

""" 2 eV """

for i in range(0,17):
    data[4][2][i]=data[4][2][i]/9.941E+05
    
""" 5 eV """

for i in range(0,17):
    data[4][3][i]=data[4][3][i]/1.785E+06

""" 10 eV """

for i in range(0,17):
    data[4][4][i]=data[4][4][i]/1.168E+06
    
""" 20 eV """

for i in range(0,17):
    data[4][6][i]=data[4][6][i]/4.186E+05
    
""" 30 eV """

for i in range(0,17):
    data[4][7][i]=data[4][7][i]/2.003E+05
    
""" 50 eV """

for i in range(0,17):
    data[4][8][i]=data[4][8][i]/8.336E+04
    
""" 6.8 LBC """

""" 2 eV """

for i in range(0,17):
    data[5][2][i]=data[5][2][i]/7.907E+05
    
""" 5 eV """

for i in range(0,17):
    data[5][3][i]=data[5][3][i]/1.434E+06

""" 10 eV """

for i in range(0,17):
    data[5][4][i]=data[5][4][i]/9.977E+05
    
""" 20 eV """

for i in range(0,17):
    data[5][6][i]=data[5][6][i]/4.365E+05
    
""" 30 eV """

for i in range(0,17):
    data[5][7][i]=data[5][7][i]/2.520E+05
    
""" 50 eV """

for i in range(0,17):
    data[5][8][i]=data[5][8][i]/1.274E+05
    
""" 6.8 UBC """

""" 2 eV """

for i in range(0,17):
    data[7][2][i]=data[7][2][i]/8.412E+05
    
""" 5 eV """

for i in range(0,17):
    data[7][3][i]=data[7][3][i]/1.504E+06

""" 10 eV """

for i in range(0,17):
    data[7][4][i]=data[7][4][i]/9.597E+05
    
""" 20 eV """

for i in range(0,17):
    data[7][6][i]=data[7][6][i]/3.323E+05
    
""" 30 eV """

for i in range(0,17):
    data[7][7][i]=data[7][7][i]/1.579E+05
    
""" 50 eV """

for i in range(0,17):
    data[7][8][i]=data[7][8][i]/6.705E+04
    

"""L = 4.6 """

""" ECH """
plt.figure(1)


data[0][0] = [math.radians(a) for a in data[0][0]]
ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][2], 'k', label = 'ECH')
plt.plot(data[0][0],data[3][2], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at 800 km for ECH at L = 4.6 ', fontsize = 18, fontweight = 'bold')
plt.ylim(0,3)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][3], 'k')
plt.plot(data[0][0],data[3][3], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][4], 'k')
plt.plot(data[0][0],data[3][4], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][6], 'k')
plt.plot(data[0][0],data[3][6], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][7], 'k')
plt.plot(data[0][0],data[3][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][8], 'k', label = 'ECH')
plt.plot(data[0][0],data[3][8], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.ylim(0,3)

""" LBC """
plt.figure(2)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[1][2], 'k', label = 'LBC')
plt.plot(data[0][0],data[3][2], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at 800 km for LBC at L = 4.6 ', fontsize = 18, fontweight = 'bold')
plt.ylim(0,3)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[1][3], 'k')
plt.plot(data[0][0],data[3][3], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[1][4], 'k')
plt.plot(data[0][0],data[3][4], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[1][6], 'k')
plt.plot(data[0][0],data[3][6], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[1][7], 'k')
plt.plot(data[0][0],data[3][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[1][8], 'k', label = 'LBC')
plt.plot(data[0][0],data[3][8], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.ylim(0,3)

""" UBC """
plt.figure(3)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][2], 'k', label = 'UBC')
plt.plot(data[0][0],data[3][2], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at 800 km for UBC at L = 4.6 ', fontsize = 18, fontweight = 'bold')
plt.ylim(0,3)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][3], 'k')
plt.plot(data[0][0],data[3][3], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][4], 'k')
plt.plot(data[0][0],data[3][4], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][6], 'k')
plt.plot(data[0][0],data[3][6], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][7], 'k')
plt.plot(data[0][0],data[3][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][8], 'k', label = 'UBC')
plt.plot(data[0][0],data[3][8], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.ylim(0,3)

"""L = 6.8 """

""" ECH """
plt.figure(4)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][2], 'k', label = 'ECH')
plt.plot(data[0][0],data[6][2], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at 800 km for ECH at L = 6.8 ', fontsize = 18, fontweight = 'bold')
plt.ylim(0,3)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][3], 'k')
plt.plot(data[0][0],data[6][3], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][4], 'k')
plt.plot(data[0][0],data[6][4], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][6], 'k')
plt.plot(data[0][0],data[6][6], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][7], 'k')
plt.plot(data[0][0],data[6][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][8], 'k', label = 'ECH')
plt.plot(data[0][0],data[6][8], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.ylim(0,3)

""" LBC """
plt.figure(5)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[5][2], 'k', label = 'LBC')
plt.plot(data[0][0],data[6][2], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at 800 km for LBC at L = 6.8 ', fontsize = 18, fontweight = 'bold')
plt.ylim(0,3)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[5][3], 'k')
plt.plot(data[0][0],data[6][3], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[5][4], 'k')
plt.plot(data[0][0],data[6][4], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[5][6], 'k')
plt.plot(data[0][0],data[6][6], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[5][7], 'k')
plt.plot(data[0][0],data[6][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[5][8], 'k', label = 'LBC')
plt.plot(data[0][0],data[6][8], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.ylim(0,3)

""" UBC """
plt.figure(6)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[7][2], 'k', label = 'UBC')
plt.plot(data[0][0],data[6][2], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at 800 km for UBC at L = 6.8 ', fontsize = 18, fontweight = 'bold')
plt.ylim(0,3)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[7][3], 'k')
plt.plot(data[0][0],data[6][3], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[7][4], 'k')
plt.plot(data[0][0],data[6][4], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[7][6], 'k')
plt.plot(data[0][0],data[6][6], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[7][7], 'k')
plt.plot(data[0][0],data[6][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[7][8], 'k', label = 'UBC')
plt.plot(data[0][0],data[6][8], 'r', label = 'No Waves')
plt.legend(loc = 'lower center', fontsize = 'small')
plt.ylim(0,3)

""" All three """

plt.figure(7)
plt.figtext(0.1,.77,'L = 4.6', fontsize = 14, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'L = 6.8', fontsize = 14, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.205,.03,'E = 20 eV', fontsize = 14, fontweight = 'bold')
plt.figtext(0.48,.03,'E = 30 eV', fontsize = 14, fontweight = 'bold')
plt.figtext(0.755,.03,'E = 50 eV', fontsize = 14, fontweight = 'bold')

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][6], 'k', label = 'ECH')
plt.plot(data[0][0],data[1][6], 'b', label = 'LBC')
plt.plot(data[0][0],data[2][6], 'g', label = 'UBC')
plt.plot(data[0][0],data[3][6], 'r', label = 'No Waves')
plt.suptitle('Normalized Pitch Angle Distribution at 800 km with the Influence of ECH, LBC, and UBC Waves', fontsize = 18, fontweight = 'bold')
plt.legend(loc= 'lower center', fontsize = 'small')
plt.ylim(0,3)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][7], 'k')
plt.plot(data[0][0],data[1][7], 'b')
plt.plot(data[0][0],data[2][7], 'g')
plt.plot(data[0][0],data[3][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][8], 'k')
plt.plot(data[0][0],data[1][8], 'b')
plt.plot(data[0][0],data[2][8], 'g')
plt.plot(data[0][0],data[3][8], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][6], 'k')
plt.plot(data[0][0],data[5][6], 'b')
plt.plot(data[0][0],data[7][6], 'g')
plt.plot(data[0][0],data[6][6], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][7], 'k')
plt.plot(data[0][0],data[5][7], 'b')
plt.plot(data[0][0],data[7][7], 'g')
plt.plot(data[0][0],data[6][7], 'r')
plt.ylim(0,3)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][8], 'k', label = 'ECH')
plt.plot(data[0][0],data[5][8], 'b', label = 'LBC')
plt.plot(data[0][0],data[7][8], 'g', label = 'UBC')
plt.plot(data[0][0],data[6][8], 'r', label = 'No Waves')
plt.legend(loc= 'lower center', fontsize = 'small')
plt.ylim(0,3)
    