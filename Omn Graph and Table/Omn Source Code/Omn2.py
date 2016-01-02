# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 09:21:22 2015

@author: Greg
"""
import numpy as np
import os
import scipy
import scipy.integrate
import matplotlib.pyplot as plt
import csv
import re
import math
import copy

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

file1 = open('4.6echmaAomn.txt')
file2 = open('4.6echmaBomn.txt')
file3 = open('4.6lbcmaAomn.txt')
file4 = open('4.6lbcmaBomn.txt')
file5 = open('4.6ubcmaAomn.txt')
file6 = open('4.6ubcmaBomn.txt')
file7 = open('6.8echmaAomn.txt')
file8 = open('6.8echmaBomn.txt')
file9 = open('6.8lbcmaAomn.txt')
file10 = open('6.8lbcmaBomn.txt')
file11 = open('6.8ubcmaAomn.txt')
file12 = open('6.8ubcmaBomn.txt')

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

""" Find data range"""

Data4_6ECHA = string1[string1.find('(KE)')+247:len(string1)-3]
Data4_6ECHB = string2[string2.find('(KE)')+247:len(string2)-3]
Data4_6LBCA = string3[string3.find('(KE)')+247:len(string3)-3]
Data4_6LBCB = string4[string4.find('(KE)')+247:len(string4)-3]
Data4_6UBCA = string5[string5.find('(KE)')+247:len(string5)-3]
Data4_6UBCB = string6[string6.find('(KE)')+247:len(string6)-3]
Data6_8ECHA = string7[string7.find('(KE)')+247:len(string7)-3]
Data6_8ECHB = string8[string8.find('(KE)')+247:len(string8)-3]
Data6_8LBCA = string9[string9.find('(KE)')+247:len(string9)-3]
Data6_8LBCB = string10[string10.find('(KE)')+247:len(string10)-3]
Data6_8UBCA = string11[string11.find('(KE)')+247:len(string11)-3]
Data6_8UBCB = string12[string12.find('(KE)')+247:len(string12)-3]

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

""" Write new data files """

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
ECHA4_6 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr1)
"""4.6 ECHB"""
ECHB4_6 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr2)
"""4.6 LBCA"""
LBCA4_6 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr3) 
"""4.6 LBCB"""
LBCB4_6 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr4)
"""4.6 UBCA"""
UBCA4_6 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr5) 
"""4.6 UBCB"""
UBCB4_6 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr6)
"""6.8 ECHA"""
ECHA6_8 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr7) 
"""6.8 ECHB"""
ECHB6_8 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr8)
"""6.8 LBCA"""
LBCA6_8 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr9) 
"""6.8 LBCB"""
LBCB6_8 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr10)
"""6.8 UBCA"""
UBCA6_8 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr11)
"""6.8 UBCB"""
UBCB6_8 = columns_to_list(23, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), csvr12) 

data = [ECHA4_6, ECHB4_6, LBCA4_6, LBCB4_6, UBCA4_6, UBCB4_6, ECHA6_8, ECHB6_8, LBCA6_8, LBCB6_8, UBCA6_8, UBCB6_8]

""" Convert lists to arrays of floats """

for k in range(0,12):
    for j in range(1,23):
        data[k][j] = np.array(data[k][j],dtype=float)
        
dataA = copy.deepcopy(data)
dataB = copy.deepcopy(data)
data2 = copy.deepcopy(data)

""" Coefficient of Integration """

A = (4*math.pi*data[0][1]**(0.5))/(59309697.4)
B = (4*math.pi)/(data[0][1]**(0.5)*59309697.4)

"""Integrands for Energy Density"""

for i in range(0,12):
    for j in range(2,23):
        dataA[i][j] = A*data[i][j]
            
"""Integrands for Density """

for i in range(0,12):
    for j in range(2,23):
        dataB[i][j] = B*data[i][j]
        
file1=open('Energy_Density_Integrations.txt', 'w')
file1.write('8.000E+07\t2.229E+08\t3.745E+08\t5.336E+08\t6.990E+08\t8.693E+08\t1.043E+09\t1.220E+09\t1.398E+09\t1.577E+09\t1.754E+09\t1.931E+09\t2.105E+09\t2.276E+09\t2.444E+09\t2.610E+09\t2.772E+09\t2.931E+09\t3.088E+09\t3.244E+09\t3.398E+09\n') 

for i in range(0,12):
    file1.write("\n")
    for j in range(2,23):
        file1.write(str(scipy.integrate.simps(dataA[i][j],data[0][1])))
        file1.write('\t')

file1.close()

file2=open('Particle_Density_Integrations.txt', 'w')
file2.write('8.000E+07\t2.229E+08\t3.745E+08\t5.336E+08\t6.990E+08\t8.693E+08\t1.043E+09\t1.220E+09\t1.398E+09\t1.577E+09\t1.754E+09\t1.931E+09\t2.105E+09\t2.276E+09\t2.444E+09\t2.610E+09\t2.772E+09\t2.931E+09\t3.088E+09\t3.244E+09\t3.398E+09\n')

for i in range(0,12):
    file2.write('\n')
    for j in range(2,23):
        file2.write(str(scipy.integrate.simps(dataB[i][j],data[0][1])))
        file2.write('\t')
        
file2.close()

file3=open('Energy_Density_Integrations(1-600).txt', 'w')
file3.write('8.000E+07\t2.229E+08\t3.745E+08\t5.336E+08\t6.990E+08\t8.693E+08\t1.043E+09\t1.220E+09\t1.398E+09\t1.577E+09\t1.754E+09\t1.931E+09\t2.105E+09\t2.276E+09\t2.444E+09\t2.610E+09\t2.772E+09\t2.931E+09\t3.088E+09\t3.244E+09\t3.398E+09\n')

for i in range(0,12):
    file3.write('\n')
    for j in range(2,23):
        file3.write(str(scipy.integrate.simps(dataA[i][j][0:600],data[0][1][0:600])))
        file3.write('\t')
        data2[i][j] = scipy.integrate.simps(dataA[i][j][0:600],data[0][1][0:600])
    

file3.close()

file4=open('Particle_Density_Integrations(1-600).txt', 'w')
file4.write('8.000E+07\t2.229E+08\t3.745E+08\t5.336E+08\t6.990E+08\t8.693E+08\t1.043E+09\t1.220E+09\t1.398E+09\t1.577E+09\t1.754E+09\t1.931E+09\t2.105E+09\t2.276E+09\t2.444E+09\t2.610E+09\t2.772E+09\t2.931E+09\t3.088E+09\t3.244E+09\t3.398E+09\n')

for i in range(0,12):
    file4.write('\n')
    for j in range(2,23):
        file4.write(str(scipy.integrate.simps(dataB[i][j][0:600],data[0][1][0:600])))
        file4.write('\t')
        
file4.close()

file5=open('Energy_Density_Integrations(600-10000).txt', 'w')
file5.write('8.000E+07\t2.229E+08\t3.745E+08\t5.336E+08\t6.990E+08\t8.693E+08\t1.043E+09\t1.220E+09\t1.398E+09\t1.577E+09\t1.754E+09\t1.931E+09\t2.105E+09\t2.276E+09\t2.444E+09\t2.610E+09\t2.772E+09\t2.931E+09\t3.088E+09\t3.244E+09\t3.398E+09\n')

for i in range(0,12):
    file5.write('\n')
    for j in range(2,23):
        file5.write(str(scipy.integrate.simps(dataA[i][j][600:10000],data[0][1][600:10000])))
        file5.write('\t')

file5.close()

file6=open('Particle_Density_Integrations(600-10000).txt', 'w')
file6.write('8.000E+07\t2.229E+08\t3.745E+08\t5.336E+08\t6.990E+08\t8.693E+08\t1.043E+09\t1.220E+09\t1.398E+09\t1.577E+09\t1.754E+09\t1.931E+09\t2.105E+09\t2.276E+09\t2.444E+09\t2.610E+09\t2.772E+09\t2.931E+09\t3.088E+09\t3.244E+09\t3.398E+09\n')

for i in range(0,12):
    file6.write('\n')
    for j in range(2,23):
        file6.write(str(scipy.integrate.simps(dataB[i][j][600:10000],data[0][1][600:10000])))
        file6.write('\t')
        
file6.close()

a = [0]*21
b = [0]*21
c = [0]*21
d = [0]*21
e = [0]*21
f = [0]*21
g = [0]*21
h = [0]*21
i = [0]*21
j = [0]*21
k = [0]*21
l = [0]*21

m = [a,b,c,d,e,f,g,h,i,j,k,l]

n = [8.000E+07,2.229E+08,3.745E+08,5.336E+08,6.990E+08,8.693E+08,1.043E+09,1.220E+09,1.398E+09,1.577E+09,1.754E+09,1.931E+09,2.105E+09,2.276E+09,2.444E+09,2.610E+09,2.772E+09,2.931E+09,3.088E+09,3.244E+09,3.398E+09]

for i in range(0,12):
    for j in range(2,23):
       m[i][j-2] = data2[i][j]
       

plt.figure(1)

""" ECH Up and Down L = 4.6 """
plt.subplot(1,2,1)
plt.plot(m[0],n, 'k', label = 'ECH')
plt.plot(m[2],n, 'r', label = 'LBC')
plt.plot(m[4],n, 'g', label = 'UBC')
plt.plot(m[1],n, 'c', label = 'No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.title('L = 4.6', fontsize = 18, fontweight = 'bold')
plt.ylabel('Altitude (cm)', fontsize = 16, fontweight = 'bold')
plt.xlabel('Energy Density (eV/cm$^-$$^3$)', fontsize =16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim(80000000,4000000000)
plt.suptitle('Energy Density of Omni-directional Fluxes with respect to Altitude ', fontsize = 18, fontweight = 'bold')

plt.subplot(1,2,2)
plt.plot(m[6],n, 'k', label = 'ECH')
plt.plot(m[8],n, 'r', label = 'LBC')
plt.plot(m[10],n, 'g', label = 'UBC')
plt.plot(m[7],n, 'c', label = 'No Waves')
plt.legend(loc='upper right', fontsize=12)
plt.title('L = 6.8', fontsize = 18, fontweight = 'bold')
plt.ylabel('Altitude (cm)', fontsize = 16, fontweight = 'bold')
plt.xlabel('Energy Density (eV/cm$^-$$^3$)', fontsize =16, fontweight = 'bold')
plt.xticks( fontsize = 14)
plt.yticks( fontsize = 14)
plt.xscale('log')
plt.yscale('log')
plt.ylim(80000000,4000000000)


plt.show()