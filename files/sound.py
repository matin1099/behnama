"""notification sound!
    WAV file downloaded from
    https://mixkit.co/free-sound-effects/notification/
    
"""
from pydub import AudioSegment
from pydub.playback import play
# for playing wav file

song = AudioSegment.from_wav("files/notif.wav")

def notification():
    play(song)
    