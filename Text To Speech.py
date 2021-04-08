# Importing Modules
import pyttsx3

# Initializing A Function For Getting An Engine Instance For The Speech
engine = pyttsx3.init()

# Passing Text To Be Spoken In The Say Method On Engine
engine.say("Hello World")

# Run And Wait Method To Process The Voice Commands
engine.runAndWait()