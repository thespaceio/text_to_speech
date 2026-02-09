# This program turns Text to Speech


from gtts import gTTS
import os

print("================ READING FILE =======================")
file = open("abc.txt", 'r').read()

speech = gTTS(text=file, lang='en', slow=False)

print("=============== SAVING FILE ========================")
speech.save("voice.mp3")

os.system("voice.mp3")

# remember to enhance code 



