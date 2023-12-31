#install wavio or scipy
#pip install wavio
#wavio 0.0.8

#pip install scipy
#scipy 1.11.4

import sounddevice as sd
from scipy.io.wavfile import write


print(sd.get_portaudio_version())

sampling_freq = 44100 #in fps

recording_duration = 5 #in seconds

#for repeated use
sd.default.samplerate = 44100 # type: ignore
sd.default.channels = 2 #type: ignore


# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(recording_duration * sampling_freq))

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", sampling_freq, recording)
