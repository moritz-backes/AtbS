#! python3
'''bullet_point_adder.py - Adds Wikipedia bullet points to the start
    of each line of text on the clipboard'''

import pyperclip
text = pyperclip.paste()
print(text + '\n\n\n')

# TODO: Seperate lines and add stars
text_as_list = text.split('\n')
for i in range(len(text_as_list)):
    text_as_list[i] = '* ' + text_as_list[i]
text = '\n'.join(text_as_list)
print(text)

pyperclip.copy(text)
