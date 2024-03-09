from PIL import Image
from itertools import product
import os

def tile(dir_in):
    filename = "split.jpg"
    dir_out = "./blockImage/blocks"
    h_d = 60
    w_d = 70
    name, ext = os.path.splitext(filename)
    img = Image.open(dir_in)
    w, h = img.size
    
    grid = product(range(0, h-h%h_d, h_d), range(0, w-w%w_d, w_d))
    k = 0
    for i, j in grid:
        box = (j, i, j+w_d, i+h_d)
        # out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        out = os.path.join(dir_out, f'{k}{ext}')
        img.crop(box).save(out)
        k = k + 1