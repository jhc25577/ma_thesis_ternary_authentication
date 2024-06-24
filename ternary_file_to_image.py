import os,glob
import random
from itertools import cycle,islice
from PIL import Image
import numpy as np      

# mapping trits to rgb values
def ternary_2_rgb(input):
    if input == 0:
        return [255,0,0]
    elif input == 1:
        return [0,255,0]
    else:
        return [0,0,255]

def ternary_2_gray(input):
    if input == 0:
        return [255,255,255]
    elif input == 1:
        return [122,122,122]
    else:
        return [0,0,0]
count = 0
path = "data_4_cloned"
for file in os.listdir(path):
    f = open(os.path.join(path,file), "r")
    # print("File being converted: ", file)
# f = open("data_0_cloned/data_0_0.txt", "r")
    s = f.read()
    f_data = [int(x) for x in s]
    #print(f_data)
    image_data = []
    for i in f_data:
        image_data.append(ternary_2_rgb(i))
    # print(image_data)
    image_data = np.array(image_data)
    length = int(len(image_data)/512)
    data_2_img = image_data.reshape((length,512,-1))

    image = Image.fromarray(data_2_img.astype('uint8'), mode="RGB")
    # print("Image made.")
    new_dir = f"C:/Users/Jo/Documents/ma_thesis_ternary_authentication/{path}_images"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    new_filename = f"{path}_{count}.png"
    image.save(os.path.join(new_dir,new_filename))
    # image.save("data_0.png")
    count = count + 1
    # print("Image saved.")
