import math
import pandas
import os

def to_binary(ternary_data):
    b_data = ""
    for i in range(0, len(ternary_data)):
        if (i+1)%4 == 0:
            x = ternary_data[i-3]*(3**3) + ternary_data[i-2]*(3**2) + ternary_data[i-1]*(3) + ternary_data[i]
            b_data = b_data + f'{x:08b}'

    return b_data

path = "data_4_test_data"

new_dir = f"{path}_bit_data"
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    
for file in os.listdir(path):
    f = open(os.path.join(path,file), "r")
    # print("File being converted: ", file)
# f = open("data_0_cloned/data_0_0.txt", "r")
    s = f.read()
    f_data = [int(x) for x in s]
    #print(f_data)
    b_data = to_binary(f_data)

    with open(f"{new_dir}\{file}", "w+") as f:
        f.write(b_data)


    

