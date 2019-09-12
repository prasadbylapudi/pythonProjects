from gtts import gTTS
import os

fh=open("test.txt","r")

myText=fh.read().replace("\n"," ")#this is to reaplace the new line with the spaces.

language='te'#here you can put your own language code like for english en and for tamil ta and for telugu te and so on .

output=gTTS(text=myText,lang=language,slow=False)


output.save("output.mp3")

fh.close()
 
os.system("start output.mp3")
