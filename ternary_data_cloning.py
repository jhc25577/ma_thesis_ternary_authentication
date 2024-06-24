import numpy as np
import random
import math
import os

# function for variating bits: 0 changes to 1, 1 can change to 0 or 2, and 2 changes to 1
def variation_rule(num): 
    if num == 0:
        num = 1
    elif num == 1:
        choice = random.randint(0, 1)
        if choice == 0:
            num = 0
        else:
            num = 2
    else:
        num = 1
    return num

# function for randomly variating 3% of the data
def randomized_variation(data_list):
    data_size = len(data_list)
    num_variations = math.floor(data_size*0.03)
    index_change = random.sample(range(0, data_size), num_variations)

    data_var = []
    i = 0
    for x in data_list:
        if i in index_change:
            data_var.append(variation_rule(x))
        else:
            data_var.append(x)
        i = i + 1
    return data_var

random.seed(42)
# open a file with data
file_name = "data_4.txt"
with open(f"data/{file_name}", "r") as f:
    r_data = list(f.read())
    
f_data = [int(x) for x in r_data]
# count_0 = f_data.count(0)
# count_1 = f_data.count(1)
# count_2 = f_data.count(2)
# total = count_0 + count_1 + count_2

# # checking bias of data
# print("Bias of 0: ", count_0/total)
# print("Bias of 1: ", count_1/total)
# print("Bias of 2: ", count_2/total)

new_file_name = file_name.replace(".txt", "")

new_dir = f"C:/Users/Jo/Documents/ma_thesis_ternary_authentication/{new_file_name}_test_data"
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

for i in range(0, 50):
    with open(f"{new_dir}\{new_file_name}_{i}.txt", "w+") as f:
        a = randomized_variation(f_data)
        s = ''.join(str(x) for x in a)
        f.write(s)
        