# a translator translate english into french
#  python3 -m pip install translate
from translate import Translator 

translator = Translator(to_lang="zh")

try:
    with open('input.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)

        with open('output-ja.txt', 'w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:
    print("check your file path silly!")
