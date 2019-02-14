# Accepts given input file and reads it out
# Vignesh Narasimhulu

#google text-to-speech engine
from gtts import gTTS

#tempfile to store mp3
from tempfile import TemporaryFile as TF

#to load & play mp3
from pygame import mixer

#define the speech language
olang='en-au'

#define the input file
ifile="input.txt"

###########
# FUNCTIONS
###########
#function to play the given input
def Play(process):
    try:
      tts = gTTS(process, lang=olang)
      #initiate a temp file, to store the audio
      tf=TF()
      tts.write_to_fp(tf)
      tf.seek(0)
      #load and play the file
      mixer.music.load(tf)
      mixer.music.play()
    except ValueError:
      print("Sorry, the language is not supported")

#####
#MAIN
#####
#initialise the player
mixer.init()

try:
    #read the given file in utf-8 (ensure special chars are processed) mode
    file = open(ifile, mode='r', encoding='utf-8') #default.mode=ascii
    entire_file_contents = file.read()
    Play(entire_file_contents)
except:
    print("Unable to open file " + str(file) + " for reading")
    exit()
    


