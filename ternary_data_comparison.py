import numpy as np
import random

def hammingDist(str1, str2): 
    i = 0
    count = 0
  
    while(i < len(str1)): 
        if(str1[i] != str2[i]): 
            count += 1
        i += 1
    return count 

with open("data_1.txt", "r") as f:
    data_1 = f.read()

with open("data_3.txt", "r") as b:
    data_2 = b.read()

print(data_1 == data_2)

print(hammingDist(data_1, data_2)/len(data_1))
