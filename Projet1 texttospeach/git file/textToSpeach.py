from gtts import gTTS
import os

input_text = open('sample.txt')
text = input_text.read()

language = 'en'

obj = gTTS(text = text, lang= language, slow= False)
obj.save("sample.mp3")

os.system("sample.mp3")
