# python -m venv image-env   
# image-env\Scripts\activate.bat
# python -m pip install Pillow


from PIL import Image, ImageFilter

img = Image.open('Scripting\Image\pikachu.jpg')

print(dir(img))
print(img.format) # format == RGB
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("Scripting\Image\\blur.png",'png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("Scripting\Image\smooth.png",'png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("Scripting\Image\sharp.png",'png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("Scripting\Image\smooth.png",'png')

filtered_img = img.convert('L') # format == L, black and white and grey
filtered_img.save("Scripting\Image\grey.png",'png')