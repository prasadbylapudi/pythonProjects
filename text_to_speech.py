from gtts import gTTS
import os

myText="prasad bylapudi how are you and i'm john and best of luck for you career"

language='en'

output=gTTS(text=myText,lang=language,slow=False)


output.save("output.mp3")

os.system("start output.mp3")
