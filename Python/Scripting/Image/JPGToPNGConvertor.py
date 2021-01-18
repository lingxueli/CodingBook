# python Scripting\Image\JPGToPNGConvertor.py Scripting\Image\image\ Scripting\Image\new\
import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through origin/, convert image to png
# save to /new
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')

    # not saving it as charmander.jpg.png -> charmander.png
    clean_name = os.path.splitext(filename)[0]

    img.save(f'{output_folder}{clean_name}.png','png')

print("done")