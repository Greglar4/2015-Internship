# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:11:50 2015

@author: Greg
"""

import os
import matplotlib.pyplot as plt
import csv
import re

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

csvr1 = csv.reader(open('Data4_6ECHA.txt', 'rb'), delimiter = ' ')
csvr2 = csv.reader(open('Data4_6ECHB.txt', 'rb'), delimiter = ' ')
csvr3 = csv.reader(open('Data4_6LBCA.txt', 'rb'), delimiter = ' ')
csvr4 = csv.reader(open('Data4_6LBCB.txt', 'rb'), delimiter = ' ')
csvr5 = csv.reader(open('Data4_6UBCA.txt', 'rb'), delimiter = ' ')
csvr6 = csv.reader(open('Data4_6UBCB.txt', 'rb'), delimiter = ' ')
csvr7 = csv.reader(open('Data6_8ECHA.txt', 'rb'), delimiter = ' ')
csvr8 = csv.reader(open('Data6_8ECHB.txt', 'rb'), delimiter = ' ')
csvr9 = csv.reader(open('Data6_8LBCA.txt', 'rb'), delimiter = ' ')
csvr10 = csv.reader(open('Data6_8LBCB.txt', 'rb'), delimiter = ' ')
csvr11 = csv.reader(open('Data6_8UBCA.txt', 'rb'), delimiter = ' ')
csvr12 = csv.reader(open('Data6_8UBCB.txt', 'rb'), delimiter = ' ')

""" Zip """

"""4.6 ECHA"""
ECHA4_6 = columns_to_list(8, (1,2,3,4,5,6,7), csvr1)
"""4.6 ECHB"""
ECHB4_6 = columns_to_list(8, (1,2,3,4,5,6,7), csvr2)
"""4.6 LBCA"""
LBCA4_6 = columns_to_list(8, (1,2,3,4,5,6,7), csvr3) 
"""4.6 LBCB"""
LBCB4_6 = columns_to_list(8, (1,2,3,4,5,6,7), csvr4)
"""4.6 UBCA"""
UBCA4_6 = columns_to_list(8, (1,2,3,4,5,6,7), csvr5) 
"""4.6 UBCB"""
UBCB4_6 = columns_to_list(8, (1,2,3,4,5,6,7), csvr6)
"""6.8 ECHA"""
ECHA6_8 = columns_to_list(8, (1,2,3,4,5,6,7), csvr7) 
"""6.8 ECHB"""
ECHB6_8 = columns_to_list(8, (1,2,3,4,5,6,7), csvr8)
"""6.8 LBCA"""
LBCA6_8 = columns_to_list(8, (1,2,3,4,5,6,7), csvr9) 
"""6.8 LBCB"""
LBCB6_8 = columns_to_list(8, (1,2,3,4,5,6,7), csvr10)
"""6.8 UBCA"""
UBCA6_8 = columns_to_list(8, (1,2,3,4,5,6,7), csvr11)
"""6.8 UBCB"""
UBCB6_8 = columns_to_list(8, (1,2,3,4,5,6,7), csvr12)

data = [ECHA4_6, ECHB4_6, LBCA4_6, LBCB4_6, UBCA4_6, UBCB4_6, ECHA6_8, ECHB6_8, LBCA6_8, LBCB6_8, UBCA6_8, UBCB6_8]


""" Convert to float """

for k in range(0,12):
    for j in range(0,7):
        for i in range(0,136):
            data[k][j][i] = float(data[k][j][i])
            
""" Append """
            
for i in range(0,136):
    data[0][0].append(90+90-data[0][0][135-i])
    
for k in range(0,12):
    for j in range(1,7):
        for i in range(0,136):
            data[k][j].append(data[k][j][135-i])
            
    
plt.figure(1)

"""L = 4.6 """

""" ECH """
plt.subplot(2,3,1)
plt.plot(data[0][0],data[0][1], 'k', label = '2 eV')
plt.plot(data[0][0],data[0][2], 'k--', label = '5 eV')
plt.plot(data[0][0],data[0][3], 'k:', label = '10 eV')
plt.plot(data[0][0],data[1][1], 'r')
plt.plot(data[0][0],data[1][2], 'r--')
plt.plot(data[0][0],data[1][3], 'r:')
plt.legend(loc='upper center', fontsize=12)
plt.title('ECH', fontsize = 18, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.ylim(1,10000000)
plt.yscale('log')
plt.suptitle('Pitch Angle Distribution at the Equator at L = 4.6 ', fontsize = 18, fontweight = 'bold')

plt.subplot(2,3,4)
plt.plot(data[0][0],data[0][4], 'k', label = '20 eV')
plt.plot(data[0][0],data[0][5], 'k--', label = '30 eV')
plt.plot(data[0][0],data[0][6], 'k:', label = '50 eV')
plt.plot(data[0][0],data[1][4], 'r')
plt.plot(data[0][0],data[1][5], 'r--')
plt.plot(data[0][0],data[1][6], 'r:')
plt.legend(loc='upper center', fontsize=12)
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xlabel('Pitch Angle (degrees)', fontsize =16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

""" UBC """
plt.subplot(2,3,2)
plt.plot(data[0][0],data[4][1], 'k', label = '2 eV')
plt.plot(data[0][0],data[4][2], 'k--', label = '5 eV')
plt.plot(data[0][0],data[4][3], 'k:', label = '10 eV')
plt.plot(data[0][0],data[1][1], 'r')
plt.plot(data[0][0],data[1][2], 'r--')
plt.plot(data[0][0],data[1][3], 'r:')
plt.title('UBC', fontsize = 18, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

plt.subplot(2,3,5)
plt.plot(data[0][0],data[4][4], 'k', label = '20 eV')
plt.plot(data[0][0],data[4][5], 'k--', label = '30 eV')
plt.plot(data[0][0],data[4][6], 'k:', label = '50 eV')
plt.plot(data[0][0],data[1][4], 'r')
plt.plot(data[0][0],data[1][5], 'r--')
plt.plot(data[0][0],data[1][6], 'r:')
plt.xlabel('Pitch Angle (degrees)', fontsize =16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

""" LBC """
plt.subplot(2,3,3)
plt.plot(data[0][0],data[2][1], 'k')
plt.plot(data[0][0],data[2][2], 'k--')
plt.plot(data[0][0],data[2][3], 'k:')
plt.plot(data[0][0],data[1][1], 'r', label = '2 eV No Waves')
plt.plot(data[0][0],data[1][2], 'r--', label = '5 eV No Waves')
plt.plot(data[0][0],data[1][3], 'r:', label = '10 eV No Waves')
plt.title('LBC', fontsize = 18, fontweight = 'bold')
plt.legend(loc='upper center', fontsize=12)
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

plt.subplot(2,3,6)
plt.plot(data[0][0],data[2][4], 'k')
plt.plot(data[0][0],data[2][5], 'k--')
plt.plot(data[0][0],data[2][6], 'k:')
plt.plot(data[0][0],data[1][4], 'r', label = '20 eV No Waves')
plt.plot(data[0][0],data[1][5], 'r--', label = '30 eV No Waves')
plt.plot(data[0][0],data[1][6], 'r:', label = '50 eV No Waves')
plt.xlabel('Pitch Angle (degrees)', fontsize =16, fontweight = 'bold')
plt.legend(loc='upper center', fontsize=12)
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

"""L = 6.8 """
plt.figure(2)

""" ECH """
plt.subplot(2,3,1)
plt.plot(data[0][0],data[6][1], 'k', label = '2 eV')
plt.plot(data[0][0],data[6][2], 'k--', label = '5 eV')
plt.plot(data[0][0],data[6][3], 'k:', label = '10 eV')
plt.plot(data[0][0],data[7][1], 'r')
plt.plot(data[0][0],data[7][2], 'r--')
plt.plot(data[0][0],data[7][3], 'r:')
plt.legend(loc='upper center', fontsize=12)
plt.title('ECH', fontsize = 18, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)
plt.suptitle('Pitch Angle Distribution at the Equator at L = 6.8 ', fontsize = 18, fontweight = 'bold')

plt.subplot(2,3,4)
plt.plot(data[0][0],data[6][4], 'k', label = '20 eV')
plt.plot(data[0][0],data[6][5], 'k--', label = '30 eV')
plt.plot(data[0][0],data[6][6], 'k:', label = '50 eV')
plt.plot(data[0][0],data[7][4], 'r')
plt.plot(data[0][0],data[7][5], 'r--')
plt.plot(data[0][0],data[7][6], 'r:')
plt.legend(loc='upper center', fontsize=12)
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xlabel('Pitch Angle (degrees)', fontsize =16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)


""" UBC """
plt.subplot(2,3,2)
plt.plot(data[0][0],data[10][1], 'k', label = '2 eV')
plt.plot(data[0][0],data[10][2], 'k--', label = '5 eV')
plt.plot(data[0][0],data[10][3], 'k:', label = '10 eV')
plt.plot(data[0][0],data[7][1], 'r')
plt.plot(data[0][0],data[7][2], 'r--')
plt.plot(data[0][0],data[7][3], 'r:')
plt.title('UBC', fontsize = 18, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

plt.subplot(2,3,5)
plt.plot(data[0][0],data[10][4], 'k', label = '20 eV')
plt.plot(data[0][0],data[10][5], 'k--', label = '30 eV')
plt.plot(data[0][0],data[10][6], 'k:', label = '50 eV')
plt.plot(data[0][0],data[7][4], 'r')
plt.plot(data[0][0],data[7][5], 'r--')
plt.plot(data[0][0],data[7][6], 'r:')
plt.xlabel('Pitch Angle (degrees)', fontsize =16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

""" LBC """
plt.subplot(2,3,3)
plt.plot(data[0][0],data[8][1], 'k')
plt.plot(data[0][0],data[8][2], 'k--')
plt.plot(data[0][0],data[8][3], 'k:')
plt.plot(data[0][0],data[7][1], 'r', label = '2 eV No Waves')
plt.plot(data[0][0],data[7][2], 'r--', label = '5 eV No Waves')
plt.plot(data[0][0],data[7][3], 'r:', label = '10 eV No Waves')
plt.title('LBC', fontsize = 18, fontweight = 'bold')
plt.legend(loc='upper center', fontsize=12)
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)

plt.subplot(2,3,6)
plt.plot(data[0][0],data[8][4], 'k')
plt.plot(data[0][0],data[8][5], 'k--')
plt.plot(data[0][0],data[8][6], 'k:')
plt.plot(data[0][0],data[7][4], 'r', label = '20 eV No Waves')
plt.plot(data[0][0],data[7][5], 'r--', label = '30 eV No Waves')
plt.plot(data[0][0],data[7][6], 'r:', label = '50 eV No Waves')
plt.xlabel('Pitch Angle (degrees)', fontsize =16, fontweight = 'bold')
plt.legend(loc='upper center', fontsize=12)
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.yscale('log')
plt.ylim(1,10000000)



plt.show()