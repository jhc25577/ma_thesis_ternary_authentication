import math
import pandas
import os

path = "data_0_cloned"
for file in os.listdir(path):
    f = open(os.path.join(path,file), "r")
    # print("File being converted: ", file)
# f = open("data_0_cloned/data_0_0.txt", "r")
    s = f.read()
    f_data = [int(x) for x in s]
    #print(f_data)
c_data = []
for i in range(0, len(f_data)):
    # print(i)
    if (i+1)%4 == 0:
        print(i)
        x = f_data[i-3]*(3**3) + f_data[i-2]*(3**2) + f_data[i-1]*(3) + f_data[i]
        c_data.append(x)

print(c_data)

    

