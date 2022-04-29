# library
import lib  # di ambil dari lib.py, berisi beberapa library yang dibutuhkan
import tifffile
import os
from skimage.io import imread
from termcolor import colored

print(colored("\n[ Kelompok 7 - C ]", "yellow"))
print(colored("\n1. Khoirul Ummam (1197050059)\n2. Muhammad Taopik (1197050081)\n", "blue"))

# lokasi folder yang di compress
input_images = "/home/mr94t3z/Documents/python/exercise/input"
# lokasi folder hasil compress
output_images = "/home/mr94t3z/Documents/python/exercise/output"
# proses compress .tiff
for image in os.listdir(input_images):
    prediction_stack_16 = imread(input_images+"/"+image)
    os.chdir(output_images)
    tifffile.imwrite("compressed_" + image, prediction_stack_16,
                     metadata={'axes': 'XYZC'}, compression='zlib')
    # pesan selesainya proses compress
    print(image + ' - ' + colored("Berhasil di compress!", "green"))
