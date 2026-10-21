# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:42:45 2024

@author: Hafiz Tayyeb Javed
"""

"""
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
plt.title("Cities in England")
 
# setting x-axis values and specifying rotation
# for the labels in degrees
plt.xticks(x, labels, rotation=45)
 
plt.show()
"""


import numpy as np 
import matplotlib.pyplot as plt 

# set width of bar 
barWidth = 0.21
fig = plt.subplots(figsize =(5, 3.5)) 
'''
# set height of bar 
C_Sim = [3.01, 82, 84, 87, 89, 90, 92, 94, 94, 94.5] 
S_sim = [1.02, 65, 67, 69, 70, 71, 71.5, 71.5, 72.5, 73.5]
#CSE = [29, 3, 24, 25, 17] 
'''
C_Sim = [72, 77, 81, 82, 87, 89, 91, 93, 94, 94.5] 
S_sim = [57, 59, 60, 61.5, 63.5, 64.5, 65.5, 66, 67.5, 69]
# Set position of bar on X axis 
br1 = np.arange(len(C_Sim)) 
br2 = [x + barWidth for x in br1] 
#br3 = [x + barWidth for x in br2] 



plt.ylim(0, 100)  # X-axis range from 0 to 


# Make the plot
plt.bar(br1, C_Sim, color ='r', width = barWidth, 
        edgecolor ='grey', label ='KG') 
plt.bar(br2, S_sim, color ='b', width = barWidth, 
        edgecolor ='grey', label ="KG'") 
#plt.bar(br3, CSE, color ='b', width = barWidth, 
 #       edgecolor ='grey', label ='CSE') 

# Adding Xticks 
plt.xlabel('Mean Computation (%age)', fontsize = 12) 
plt.ylabel('Similarity Threshold (% age)', fontsize = 12) 
plt.xticks([r + barWidth for r in range(len(C_Sim))], 
        ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'])

plt.title("Berlin", fontsize = 15)
plt.legend(loc=0, fontsize="8")

plt.show()