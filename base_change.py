import math
import pandas

path = "data_4_cloned"
for file in os.listdir(path):
    f = open(os.path.join(path,file), "r")
    # print("File being converted: ", file)
# f = open("data_0_cloned/data_0_0.txt", "r")
    s = f.read()
    f_data = [int(x) for x in s]
    #print(f_data)
for i in f_data:
    

