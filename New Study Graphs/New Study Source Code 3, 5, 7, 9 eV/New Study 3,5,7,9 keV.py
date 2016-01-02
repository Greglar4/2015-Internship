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

file1 = open('newmw3dir.txt')
file2 = open('newmw5dir.txt')
file3 = open('newmw7dir.txt')
file4 = open('newmw9dir.txt')


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


""" Find up data """

upData3000 = string1[string1.find('Upward fluxes')+113:string1.find('Downward')-6]
upData5000 = string2[string2.find('Upward fluxes')+113:string2.find('Downward')-6]
upData7000 = string3[string3.find('Upward fluxes')+113:string3.find('Downward')-6]
upData9000 = string4[string4.find('Upward fluxes')+113:string4.find('Downward')-6]


""" Find down data """

downData3000 = string1[string1.find('Downward')+115:len(string1)-3]
downData5000 = string2[string2.find('Downward')+115:len(string2)-3]
downData7000 = string3[string3.find('Downward')+115:len(string3)-3]
downData9000 = string4[string4.find('Downward')+115:len(string4)-3]

""" Rewrite with single spaces """

upData3000 = re.sub(' +', ' ', upData3000)
upData5000 = re.sub(' +', ' ', upData5000)
upData7000 = re.sub(' +', ' ', upData7000)
upData9000 = re.sub(' +', ' ', upData9000)


downData3000 = re.sub(' +', ' ', downData3000)
downData5000 = re.sub(' +', ' ', downData5000)
downData7000 = re.sub(' +', ' ', downData7000)
downData9000 = re.sub(' +', ' ', downData9000)


""" Write up/down files """

file1 = open('upData3000.txt', 'w')
file1.write(upData3000)
file1.close()
file2 = open('upData5000.txt', 'w')
file2.write(upData5000)
file2.close()
file3 = open('upData7000.txt', 'w')
file3.write(upData7000)
file3.close()
file4 = open('upData9000.txt', 'w')
file4.write(upData9000)
file4.close()

file1 = open('downData3000.txt', 'w')
file1.write(downData3000)
file1.close()
file2 = open('downData5000.txt', 'w')
file2.write(downData5000)
file2.close()
file3 = open('downData7000.txt', 'w')
file3.write(downData7000)
file3.close()
file4 = open('downData9000.txt', 'w')
file4.write(downData9000)
file4.close()

""" CSV reader """

csvrup1 = csv.reader(open('upData3000.txt', 'rb'), delimiter = ' ')
csvrup2 = csv.reader(open('upData5000.txt', 'rb'), delimiter = ' ')
csvrup3 = csv.reader(open('upData7000.txt', 'rb'), delimiter = ' ')
csvrup4 = csv.reader(open('upData9000.txt', 'rb'), delimiter = ' ')


csvrdown1 = csv.reader(open('downData3000.txt', 'rb'), delimiter = ' ')
csvrdown2 = csv.reader(open('downData5000.txt', 'rb'), delimiter = ' ')
csvrdown3 = csv.reader(open('downData7000.txt', 'rb'), delimiter = ' ')
csvrdown4 = csv.reader(open('downData9000.txt', 'rb'), delimiter = ' ')


""" Zip """


up3000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrup1)
up5000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrup2)
up7000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrup3) 
up9000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrup4)
down3000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrdown1) 
down5000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrdown2)
down7000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrdown3) 
down9000 = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrdown4)

Data = [up3000, up5000, up7000, up9000, down3000, down5000, down7000, down9000]

""" Convert to float """

for k in range(0,8):
    for j in range(0,8):
        for i in range(0,len(Data[k][j])):
            Data[k][j][i] = float(Data[k][j][i])
            
"""************************* PLOTTING ***************************"""
plt.figure(1)
""" Upward """
plt.subplot(1,2,1)
plt.plot(Data[0][0],Data[0][8], 'k', label='1-3000 eV')
plt.plot(Data[1][0],Data[1][8], 'r', label='1-5000 eV')
plt.plot(Data[2][0],Data[2][8], 'g', label='1-7000 eV')
plt.plot(Data[3][0],Data[3][8], 'b', label='1-9000 eV')
plt.legend(loc='lower left', fontsize=12)
plt.title('Upward Fluxes')
plt.ylabel('Flux [eV$^-$$^1$ cm$^-$$^2$ s$^-$$^1$]', fontsize = 16, fontweight = 'bold')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])
plt.suptitle('Upward and Downward Electron Fluxes at 800 km at L = 4.6', fontsize = 18, fontweight = 'bold')

""" Downward """
plt.subplot(1,2,2)
plt.plot(Data[4][0],Data[4][8], 'k', label='1-3000 eV')
plt.plot(Data[5][0],Data[5][8], 'r', label='1-5000 eV')
plt.plot(Data[6][0],Data[6][8], 'g', label='1-7000 eV')
plt.plot(Data[7][0],Data[7][8], 'b', label='1-9000 eV')
plt.legend(loc='lower left', fontsize=12)
plt.title('Downward Fluxes')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])



plt.show()





