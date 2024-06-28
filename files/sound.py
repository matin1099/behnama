"""notification sound!
    WAV file downloaded from
    https://mixkit.co/free-sound-effects/notification/
    
"""
from pydub import AudioSegment
from pydub.playback import play
# for playing wav file

songscrap = AudioSegment.from_wav("files/notif.wav")
songspot = AudioSegment.from_wav("files/notif.wav")

def notification_scrap(repeat:int=1):
    for i in range(repeat):
        play(songscrap)

def notification_spot(repeat:int=1):
    for i in range(repeat):
        play(songspot)