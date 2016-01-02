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

for i in range(0,271):
    data[0][0].append(180+data[0][0][i+1])
    
for k in range(0,12):
    for j in range(1,7):
        for i in range(0,136):
            data[k][j].append(data[k][j][135-i])
            
            
""" Divide by omni directional flux """

""" 4.6 No Waves """

""" 2 eV """

for i in range(0,272):
    data[1][1][i]=data[1][1][i]/6.445E+03

""" 5 eV """

for i in range(0,272):
    data[1][2][i]=data[1][2][i]/1.138E+04

""" 10 eV """

for i in range(0,272):
    data[1][3][i]=data[1][3][i]/1.023E+04
    
""" 20 eV """

for i in range(0,272):
    data[1][4][i]=data[1][4][i]/4.704E+03
    
""" 30 eV """

for i in range(0,272):
    data[1][5][i]=data[1][5][i]/2.462E+03
    
""" 50 eV """

for i in range(0,272):
    data[1][6][i]=data[1][6][i]/1.083E+03
    
""" 4.6 ECH """

""" 2 eV """

for i in range(0,272):
    data[0][1][i]=data[0][1][i]/4.438E+03

""" 5 eV """

for i in range(0,272):
    data[0][2][i]=data[0][2][i]/7.286E+03

""" 10 eV """

for i in range(0,272):
    data[0][3][i]=data[0][3][i]/8.565E+03
    
""" 20 eV """

for i in range(0,272):
    data[0][4][i]=data[0][4][i]/4.355E+03
    
""" 30 eV """

for i in range(0,272):
    data[0][5][i]=data[0][5][i]/2.050E+03
    
""" 50 eV """

for i in range(0,272):
    data[0][6][i]=data[0][6][i]/918
    
""" 4.6 LBC """

""" 2 eV """

for i in range(0,272):
    data[2][1][i]=data[2][1][i]/6.452E+03

""" 5 eV """

for i in range(0,272):
    data[2][2][i]=data[2][2][i]/1.139E+04

""" 10 eV """

for i in range(0,272):
    data[2][3][i]=data[2][3][i]/1.024E+04
    
""" 20 eV """

for i in range(0,272):
    data[2][4][i]=data[2][4][i]/4.713E+03
    
""" 30 eV """

for i in range(0,272):
    data[2][5][i]=data[2][5][i]/2.468E+03
    
""" 50 eV """

for i in range(0,272):
    data[2][6][i]=data[2][6][i]/1.086E+03
    
""" 4.6 UBC """

""" 2 eV """

for i in range(0,272):
    data[4][1][i]=data[4][1][i]/4.734E+03

""" 5 eV """

for i in range(0,272):
    data[4][2][i]=data[4][2][i]/1.106E+04

""" 10 eV """

for i in range(0,272):
    data[4][3][i]=data[4][3][i]/1.126E+04
    
""" 20 eV """

for i in range(0,272):
    data[4][4][i]=data[4][4][i]/4.817E+03
    
""" 30 eV """

for i in range(0,272):
    data[4][5][i]=data[4][5][i]/2.465E+03
    
""" 50 eV """

for i in range(0,272):
    data[4][6][i]=data[4][6][i]/1.049E+03
    
""" 6.8 No Waves """

""" 2 eV """

for i in range(0,272):
    data[7][1][i]=data[7][1][i]/2.019E+03

""" 5 eV """

for i in range(0,272):
    data[7][2][i]=data[7][2][i]/3.340E+03

""" 10 eV """

for i in range(0,272):
    data[7][3][i]=data[7][3][i]/2.767E+03
    
""" 20 eV """

for i in range(0,272):
    data[7][4][i]=data[7][4][i]/1.263E+03
    
""" 30 eV """

for i in range(0,272):
    data[7][5][i]=data[7][5][i]/663
    
""" 50 eV """

for i in range(0,272):
    data[7][6][i]=data[7][6][i]/289
    
""" 6.8 ECH """

""" 2 eV """

for i in range(0,272):
    data[6][1][i]=data[6][1][i]/1.186E+03

""" 5 eV """

for i in range(0,272):
    data[6][2][i]=data[6][2][i]/2.242E+03

""" 10 eV """

for i in range(0,272):
    data[6][3][i]=data[6][3][i]/3.784E+03
    
""" 20 eV """

for i in range(0,272):
    data[6][4][i]=data[6][4][i]/1.064E+03
    
""" 30 eV """

for i in range(0,272):
    data[6][5][i]=data[6][5][i]/513
    
""" 50 eV """

for i in range(0,272):
    data[6][6][i]=data[6][6][i]/210
    
""" 6.8 LBC """

""" 2 eV """

for i in range(0,272):
    data[8][1][i]=data[8][1][i]/1.215E+03

""" 5 eV """

for i in range(0,272):
    data[8][2][i]=data[8][2][i]/2.007E+03

""" 10 eV """

for i in range(0,272):
    data[8][3][i]=data[8][3][i]/1.656E+03
    
""" 20 eV """

for i in range(0,272):
    data[8][4][i]=data[8][4][i]/751
    
""" 30 eV """

for i in range(0,272):
    data[8][5][i]=data[8][5][i]/392
    
""" 50 eV """

for i in range(0,272):
    data[8][6][i]=data[8][6][i]/171
    
""" 6.8 UBC """

""" 2 eV """

for i in range(0,272):
    data[10][1][i]=data[10][1][i]/87.3

""" 5 eV """

for i in range(0,272):
    data[10][2][i]=data[10][2][i]/361

""" 10 eV """

for i in range(0,272):
    data[10][3][i]=data[10][3][i]/1.586E+03
    
""" 20 eV """

for i in range(0,272):
    data[10][4][i]=data[10][4][i]/1.512E+03
    
""" 30 eV """

for i in range(0,272):
    data[10][5][i]=data[10][5][i]/887
    
""" 50 eV """

for i in range(0,272):
    data[10][6][i]=data[10][6][i]/331
    
for k in range(0,12):
    for j in range(1,7):
        for i in range(0,271):
            data[k][j].append(data[k][j][271-i])



"""L = 4.6 """

""" ECH """
plt.figure(1)

data[0][0] = [math.radians(a) for a in data[0][0]]
ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][1], 'k', label = 'ECH')
plt.plot(data[0][0],data[1][1], 'r', label = 'No Waves')
plt.legend(loc='center left', fontsize='small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at the Equator for ECH at L = 4.6 ', fontsize = 18, fontweight = 'bold')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][2], 'k')
plt.plot(data[0][0],data[1][2], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][3], 'k')
plt.plot(data[0][0],data[1][3], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][4], 'k')
plt.plot(data[0][0],data[1][4], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][5], 'k')
plt.plot(data[0][0],data[1][5], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[0][6], 'k', label = 'ECH')
plt.plot(data[0][0],data[1][6], 'r', label = 'No Waves')
plt.legend(loc='center right', fontsize = 'small')
plt.yscale('log')
plt.ylim(1,1000)

""" UBC """
plt.figure(2)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][1], 'k', label = 'UBC')
plt.plot(data[0][0],data[1][1], 'r', label = 'No Waves')
plt.legend(loc='center left', fontsize='small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at the Equator for UBC at L = 4.6 ', fontsize = 18, fontweight = 'bold')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][2], 'k')
plt.plot(data[0][0],data[1][2], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][3], 'k')
plt.plot(data[0][0],data[1][3], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][4], 'k')
plt.plot(data[0][0],data[1][4], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][5], 'k')
plt.plot(data[0][0],data[1][5], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[4][6], 'k', label = 'UBC')
plt.plot(data[0][0],data[1][6], 'r', label = 'No Waves')
plt.legend(loc='center right', fontsize = 'small')
plt.yscale('log')
plt.ylim(1,1000)

""" LBC """
plt.figure(3)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][1], 'k', label = 'LBC')
plt.plot(data[0][0],data[1][1], 'r', label = 'No Waves')
plt.legend(loc='center left', fontsize='small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at the Equator for LBC at L = 4.6 ', fontsize = 18, fontweight = 'bold')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][2], 'k')
plt.plot(data[0][0],data[1][2], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][3], 'k')
plt.plot(data[0][0],data[1][3], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][4], 'k')
plt.plot(data[0][0],data[1][4], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][5], 'k')
plt.plot(data[0][0],data[1][5], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[2][6], 'k', label = 'LBC')
plt.plot(data[0][0],data[1][6], 'r', label = 'No Waves')
plt.legend(loc='center right', fontsize = 'small')
plt.yscale('log')
plt.ylim(1,1000)

"""L = 6.8 """

""" ECH """
plt.figure(4)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[6][1], 'k', label = 'ECH')
plt.plot(data[0][0],data[7][1], 'r', label = 'No Waves')
plt.legend(loc='center left', fontsize='small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at the Equator for ECH at L = 6.8 ', fontsize = 18, fontweight = 'bold')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[6][2], 'k')
plt.plot(data[0][0],data[7][2], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[6][3], 'k')
plt.plot(data[0][0],data[7][3], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[6][4], 'k')
plt.plot(data[0][0],data[7][4], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[6][5], 'k')
plt.plot(data[0][0],data[7][5], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[6][6], 'k', label = 'ECH')
plt.plot(data[0][0],data[7][6], 'r', label = 'No Waves')
plt.legend(loc='center right', fontsize = 'small')
plt.yscale('log')
plt.ylim(1,1000)

""" UBC """
plt.figure(5)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[10][1], 'k', label = 'UBC')
plt.plot(data[0][0],data[7][1], 'r', label = 'No Waves')
plt.legend(loc='center left', fontsize='small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at the Equator for UBC at L = 6.8 ', fontsize = 18, fontweight = 'bold')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[10][2], 'k')
plt.plot(data[0][0],data[7][2], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[10][3], 'k')
plt.plot(data[0][0],data[7][3], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[10][4], 'k')
plt.plot(data[0][0],data[7][4], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[10][5], 'k')
plt.plot(data[0][0],data[7][5], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[10][6], 'k', label = 'UBC')
plt.plot(data[0][0],data[7][6], 'r', label ='No Waves')
plt.legend(loc='center right', fontsize = 'small')
plt.yscale('log')
plt.ylim(1,1000)

""" LBC """
plt.figure(6)

ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[8][1], 'k', label = 'LBC')
plt.plot(data[0][0],data[7][1], 'r', label = 'No Waves')
plt.legend(loc='center left', fontsize='small')
plt.figtext(0.1,.78,'E = 2 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'E = 20 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.78,'E = 5 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.38,.33,'E = 30 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.78,'E = 10 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.66,.33,'E = 50 eV', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.suptitle('Normalized Pitch Angle Distribution at the Equator for LBC at L = 6.8 ', fontsize = 18, fontweight = 'bold')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[8][2], 'k')
plt.plot(data[0][0],data[7][2], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[8][3], 'k')
plt.plot(data[0][0],data[7][3], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[8][4], 'k')
plt.plot(data[0][0],data[7][4], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[8][5], 'k')
plt.plot(data[0][0],data[7][5], 'r')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
ax.set_theta_direction(-1)
plt.plot(data[0][0],data[8][6], 'k', label = 'LBC')
plt.plot(data[0][0],data[7][6], 'r', label = 'No Waves')
plt.legend(loc='center right', fontsize = 'small')
plt.yscale('log')
plt.ylim(1,1000)

""" All three """

plt.figure(7)
plt.figtext(0.1,.77,'L = 4.6', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.1,.33,'L = 6.8', fontsize = 18, fontweight = 'bold', rotation = 'vertical')
plt.figtext(0.20,.03,'E = 20 eV', fontsize = 18, fontweight = 'bold')
plt.figtext(0.47,.03,'E = 30 eV', fontsize = 18, fontweight = 'bold')
plt.figtext(0.75,.03,'E = 50 eV', fontsize = 18, fontweight = 'bold')
ax = plt.subplot(2,3,1, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
plt.plot(data[0][0],data[0][4], 'k', label='ECH')
plt.plot(data[0][0],data[4][4], 'g', label='UBC')
plt.plot(data[0][0],data[2][4], 'b', label='LBC')
plt.plot(data[0][0],data[1][4], 'r', label='No Waves')
plt.legend(loc='center left', fontsize='small')
plt.suptitle('Normalized Pitch Angle Distribution of Electrons at the Equator with the Influence ECH, LBC, and UBC Waves', fontsize = 18, fontweight = 'bold')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,2, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
plt.plot(data[0][0],data[0][5], 'k', label='ECH')
plt.plot(data[0][0],data[4][5], 'g', label='UBC')
plt.plot(data[0][0],data[2][5], 'b', label='LBC')
plt.plot(data[0][0],data[1][5], 'r', label='No Waves')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,3, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
plt.plot(data[0][0],data[0][6], 'k', label='ECH')
plt.plot(data[0][0],data[4][6], 'g', label='UBC')
plt.plot(data[0][0],data[2][6], 'b', label='LBC')
plt.plot(data[0][0],data[1][6], 'r', label='No Waves')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,4, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
plt.plot(data[0][0],data[6][4], 'k', label='ECH')
plt.plot(data[0][0],data[10][4], 'g', label='UBC')
plt.plot(data[0][0],data[8][4], 'b', label='LBC')
plt.plot(data[0][0],data[7][4], 'r', label='No Waves')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,5, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
plt.plot(data[0][0],data[6][5], 'k', label='ECH')
plt.plot(data[0][0],data[10][5], 'g', label='UBC')
plt.plot(data[0][0],data[8][5], 'b', label='LBC')
plt.plot(data[0][0],data[7][5], 'r', label='No Waves')
plt.yscale('log')
plt.ylim(1,1000)

ax = plt.subplot(2,3,6, polar = True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.thetagrids([0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345])
plt.plot(data[0][0],data[6][6], 'k', label='ECH')
plt.plot(data[0][0],data[10][6], 'g', label='UBC')
plt.plot(data[0][0],data[8][6], 'b', label='LBC')
plt.plot(data[0][0],data[7][6], 'r', label='No Waves')
plt.legend(loc='center right', fontsize = 'small')
plt.yscale('log')
plt.ylim(1,1000)