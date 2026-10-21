# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 01:57:17 2024

@author: Hafiz Tayyeb Javed
"""

# Python program to set x-axis values in matplotlib
 
import matplotlib.pyplot as plt
from operator import add, mul 
a = [2, 2, 2, 2, 2, 2,2,2,2,2]
# x-axis and y-axis values for plotting

x = [10, 20, 30, 40, 50, 60,70,80,90,100]
y = [0.21, 0.27, 0.35, 0.42, 0.51, 0.59,0.73, 0.84, 0.94, 0.99]
y1 =[0.10, 0.16, 0.22, 0.30, 0.41, 0.55,0.69, 0.81, 0.91, 0.96]
type1FP = [0.8, 0.6, 0.42, 0.31, 0.25, 0.195,0.165, 0.14, 0.12, 0.11]







y2=list( map(add, y, y1) )
y3=list( map(mul, y, y1) )
y4=list( map(mul, y3,a ) )
F1 = [i / j for i, j in zip(y4, y2)]
print(y4)
type2FN = [0.2, 0.23, 0.34, 0.42, 0.56, 0.67,0.79, 0.87, 0.97, 0.989]


#defining range
plt.xlim(0, 100)  # X-axis range from 0 to 5
plt.ylim(0.1, 1.0,0.2) # Y-axis range from 0 to 20

# labels for x-asix
labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6']
 
# Plotting x-axis and y-axis
plt.plot(x, y, ':3', label='Precision')

plt.plot(x, y1, '--4', label='Recall')
plt.plot(x, F1, '-*', label='F1-Score')



plt.plot(x, type1FP, '-*', label='Type-1 Error')
#plt.plot(range(10), '--bo', label='line with marker')
plt.legend(loc=7, fontsize="8")
# naming of x-axis and y-axis
plt.xlabel("Similarity Threshold in %age")
plt.ylabel("Probability")
 
# naming the title of the plot
plt.title("Berlin")
 
# setting x-axis values and specifying rotation
# for the labels in degrees
plt.xticks(x, labels, rotation=45)
 
plt.show()