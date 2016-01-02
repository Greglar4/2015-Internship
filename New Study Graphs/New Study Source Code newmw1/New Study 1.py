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

file1 = open('newmw1dir.txt')



""" Read files to strings """

string1 = file1.read()

""" Close files """

file1.close()


""" Find up data """

upData = string1[string1.find('Upward fluxes')+113:string1.find('Downward')-6]



""" Find down data """

downData = string1[string1.find('Downward')+115:len(string1)-3]


""" Rewrite with single spaces """

upData = re.sub(' +', ' ', upData)

downData = re.sub(' +', ' ', downData)

""" Write up/down files """

file1 = open('upData.txt', 'w')
file1.write(upData)
file1.close()

file1 = open('downData.txt', 'w')
file1.write(downData)
file1.close()

""" CSV reader """

csvrup = csv.reader(open('upData.txt', 'rb'), delimiter = ' ')

csvrdown = csv.reader(open('downData.txt', 'rb'), delimiter = ' ')

""" Zip """


up = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrup)
down = columns_to_list(10, (1,2,3,4,5,6,7,8,9), csvrdown) 

Data = [up, down]

f = open('SUMmax_DOWN.txt', 'r')
y=f.readlines()
f.close()

for i in range(0,10000):
    y[i]=float(y[i])
    
f = open('SUMmax_UP.txt', 'r')
y2=f.readlines()
f.close()

for i in range(0,10000):
    y2[i]=float(y2[i])

""" Convert to float """

for k in range(0,2):
    for j in range(0,8):
        for i in range(0,len(Data[k][j])):
            Data[k][j][i] = float(Data[k][j][i])
            
"""************************* PLOTTING ***************************"""
plt.figure(1)
""" Upward """
plt.subplot(1,2,1)
plt.plot(Data[0][0],Data[0][8], 'k', label='1-10000 eV')
plt.plot(Data[0][0],y2,'r', label = 'Sum')
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
plt.plot(Data[0][0],Data[1][8], 'k', label='1-10000 eV')
plt.plot(Data[0][0], y ,'r', label = 'Sum')
plt.legend(loc='lower left', fontsize=12)
plt.title('Downward Fluxes')
plt.xlabel('Energy [eV]', fontsize = 16, fontweight = 'bold')
plt.xticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.yticks([0.4,0.14,0.2,0.2], fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim([10,100000000])



plt.show()






