# Importing Modules
import pyttsx3

# Initializing A Function For Getting An Engine Instance For The Speech
engine = pyttsx3.init()

# Getting And Setting Speed Of The Voice
engine.getProperty('rate')
engine.setProperty('rate',120)

# Writing Phrase To Be Spoken
string = "Hello Sir! How Are You?"

# Passing Text To Be Spoken In The Say Method On Engine
engine.say(string)

# Saving Voice In A File
engine.save_to_file(string, 'voice.mp3')

# Run And Wait Method To Process The Voice Commands
engine.runAndWait()

