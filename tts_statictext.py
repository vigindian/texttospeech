#google text-to-speech engine
from gtts import gTTS

#tempfile to store mp3
from tempfile import TemporaryFile as TF

#to play mp3
from pygame import mixer

olang='en-au'

#initialise the player
mixer.init()

def Play(process):
    try:
      tts = gTTS(process, lang=olang)
      #initiate a temp file, to store the audio
      tf=TF()
      tts.write_to_fp(tf)
      tf.seek(0)
      mixer.music.load(tf)
      mixer.music.play()
    except ValueError:
      print("Sorry, the language is not supported")

#MAIN
text="I'm happy. I like blue color. I love Gayanthikha. Kanmani is the love of my life" 
Play(text)


