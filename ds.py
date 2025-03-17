import numpy as np 
import pandas as pd

data = pd.read_csv('enjoysport.csv')

output = data['enjoysport'].values  

data = data.drop(columns='enjoysport').values 

# Initialize hypothesis to the first positive example
hypothesis = None
for i in range(len(data)):
    if output[i] == 'yes':
        hypothesis = data[i].copy()
        break

# Refine the hypothesis based on the remaining positive examples
for i in range(len(data)):
    if output[i] == 'yes':
        for j in range(len(data[0])):
            if data[i][j] != hypothesis[j]:
                hypothesis[j] = '?'  

print("Final Hypothesis:", hypothesis)
