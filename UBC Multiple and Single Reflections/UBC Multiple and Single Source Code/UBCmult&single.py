# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:13:34 2015

@author: Greg
"""

import os
import matplotlib.pyplot as plt
import csv
import re
import scipy
import scipy.integrate

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

file1 = open('ubcmaBdir.txt')
file2 = open('ubcmaCdir.txt')
file3 = open('ubcmaDdir.txt')
file4 = open('ubcmaEdir.txt')


""" Read files to strings """

string1 = file1.read()
string2 = file2.read()
string3 = file3.read()
string4 = file4.read()


""" Close files """

file1.close()
file2.close()
file3.close()
file4.close()


""" Find up and down data """

upDataUBCB = string1[string1.find('Upward')+113:string1.find('Downward')-6]
upDataUBCC = string2[string2.find('Upward')+113:string2.find('Downward')-6]
upDataUBCD = string3[string3.find('Upward')+113:string3.find('Downward')-6]
upDataUBCE = string4[string4.find('Upward')+113:string4.find('Downward')-6]
downDataUBCB = string1[string1.find('Downward')+115:len(string1)-6]
downDataUBCC = string2[string2.find('Downward')+115:len(string2)-6]
downDataUBCD = string3[string3.find('Downward')+115:len(string3)-6]
downDataUBCE = string4[string4.find('Downward')+115:len(string4)-6]



""" Rewrite with single spaces """

upDataUBCB = re.sub(' +', ' ', upDataUBCB)
upDataUBCC = re.sub(' +', ' ', upDataUBCC)
upDataUBCD = re.sub(' +', ' ', upDataUBCD)
upDataUBCE = re.sub(' +', ' ', upDataUBCE)
downDataUBCB = re.sub(' +', ' ', downDataUBCB)
downDataUBCC = re.sub(' +', ' ', downDataUBCC)
downDataUBCD = re.sub(' +', ' ', downDataUBCD)
downDataUBCE = re.sub(' +', ' ', downDataUBCE)

""" Write data files """

file1 = open('upDataUBCB.txt', 'w')
file1.write(upDataUBCB)
file1.close()
file2 = open('upDataUBCC.txt', 'w')
file2.write(upDataUBCC)
file2.close()
file3 = open('upDataUBCD.txt', 'w')
file3.write(upDataUBCD)
file3.close()
file4 = open('upDataUBCE.txt', 'w')
file4.write(upDataUBCE)
file4.close()
file5 = open('downDataUBCB.txt', 'w')
file5.write(downDataUBCB)
file5.close()
file6 = open('downDataUBCC.txt', 'w')
file6.write(downDataUBCC)
file6.close()
file7 = open('downDataUBCD.txt', 'w')
file7.write(downDataUBCD)
file7.close()
file8 = open('downDataUBCE.txt', 'w')
file8.write(downDataUBCE)
file8.close()

""" CSV reader """

csvr1 = csv.reader(open('upDataUBCB.txt', 'rb'), delimiter = ' ')
csvr2 = csv.reader(open('upDataUBCC.txt', 'rb'), delimiter = ' ')
csvr3 = csv.reader(open('upDataUBCD.txt', 'rb'), delimiter = ' ')
csvr4 = csv.reader(open('upDataUBCE.txt', 'rb'), delimiter = ' ')
csvr5 = csv.reader(open('downDataUBCB.txt', 'rb'), delimiter = ' ')
csvr6 = csv.reader(open('downDataUBCC.txt', 'rb'), delimiter = ' ')
csvr7 = csv.reader(open('downDataUBCD.txt', 'rb'), delimiter = ' ')
csvr8 = csv.reader(open('downDataUBCE.txt', 'rb'), delimiter = ' ')

""" Zip """

UBCBup = columns_to_list(10, (1,9), csvr1)
UBCCup = columns_to_list(10, (1,9), csvr2)
UBCDup = columns_to_list(10, (1,9), csvr3) 
UBCEup = columns_to_list(10, (1,9), csvr4)
UBCBdown = columns_to_list(10, (1,9), csvr5) 
UBCCdown = columns_to_list(10, (1,9), csvr6)
UBCDdown = columns_to_list(10, (1,9), csvr7) 
UBCEdown = columns_to_list(10, (1,9), csvr8)

data = [UBCBup, UBCCup, UBCDup, UBCEup, UBCBdown, UBCCdown, UBCDdown, UBCEdown]

""" Convert to float """

for k in range(0,8):
    for j in range(0,2):
        for i in range(0,10000):
            data[k][j][i] = float(data[k][j][i])
            
""" Upward Plot """

plt.figure(1)

plt.subplot(1,2,1)
plt.plot(data[0][0],data[0][1], 'k', label='B')
plt.plot(data[0][0],data[1][1], 'r', label='C')
plt.plot(data[0][0],data[2][1], 'b', label='D')
plt.plot(data[0][0],data[3][1], 'g', label='E')
plt.legend(loc='lower left', fontsize=12)
plt.title('Upward Fluxes', fontsize = 18, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])
plt.suptitle('Upward and Downward FLuxes for UBC B, C, D, E at L = 4.6', fontsize = 18, fontweight = 'bold')

plt.subplot(1,2,2)
plt.plot(data[0][0],data[4][1], 'k', label='B')
plt.plot(data[0][0],data[5][1], 'r', label='C')
plt.plot(data[0][0],data[6][1], 'b', label='D')
plt.plot(data[0][0],data[7][1], 'g', label='E')
plt.legend(loc='lower left', fontsize=12)
plt.title('Downward Fluxes', fontsize = 18, fontweight = 'bold')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])

plt.show()