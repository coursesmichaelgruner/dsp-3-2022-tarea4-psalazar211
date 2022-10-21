#import pyaudio

filename = "audio.wav"

from pickle import TRUE
import wave
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as waves
from scipy import signal
import struct

def get_audio(filename, multi):
    Fs, sonido = waves.read(filename)
    k=int(multi*(Fs/1000))
    return k, Fs,sonido
      
def filter(k,alfa,original_signal):
    b = [(1-alfa)]
    a=[1]
    for i in range(k):
        if i == k-1:
            a.append(-1*alfa)
        else:
            a.append(0)   
    filter_singal = signal.filtfilt(b, a, original_signal)
    return filter_singal

def write_audio(filename,data):
    sampleRate = 44100.0 # hertz
    obj = wave.open(filename,'wb')
    obj.setnchannels(1) # mono
    obj.setsampwidth(2)
    obj.setframerate(sampleRate)
    for s in data:
        obj.writeframes(struct.pack('h', int(s*1)))
    obj.close()

#caso 1
multi = 50
alfa = 0.6
k,Fs,sonido = get_audio("audio.wav", multi)
filter_singal1 = filter(k,alfa,sonido)
write_audio("audio_filter1.wav",filter_singal1)
print("Signal filtered with k=Fsx50ms y alfa=0.6 in audio_filter1.wav")
#caso 2
multi = 250
alfa = 0.4
k,Fs,sonido = get_audio("audio.wav", multi)
filter_singal2 = filter(k,alfa,sonido)
write_audio("audio_filter2.wav",filter_singal2)
print("Signal filtered with k=Fsx250ms y alfa=0.4 in audio_filter2.wav")
#caso 3
multi = 500
alfa = 0.2
k,Fs,sonido = get_audio("audio.wav", multi)
filter_singal3 = filter(k,alfa,sonido)
write_audio("audio_filter3.wav",filter_singal3)
print("Signal filtered with k=Fsx500ms y alfa=0.2 in audio_filter3.wav")
#plot 
fig = plt.figure()
rows=2
columns= 2
fig.add_subplot(rows,columns,1)
plt.plot(sonido)
plt.plot(filter_singal1)
plt.legend(('original signal', 'filter signal'), loc='best')
plt.title("k=50msxFs y a=0.6")
plt.grid(True)
fig.add_subplot(rows,columns,2)
plt.figure
plt.plot(sonido)
plt.plot(filter_singal2)
plt.legend(('original signal', 'filter signal'), loc='best')
plt.title("k=250msxFs y a=0.4")
plt.grid(True)
fig.add_subplot(rows,columns,3)
plt.figure
plt.plot(sonido)
plt.plot(filter_singal1)
plt.plot(filter_singal2)
plt.plot(filter_singal3)
plt.legend(('original signal', 'filter signal'), loc='best')
plt.title("k=500msxFs y a=0.2")
plt.grid(True)

plt.show()


       
