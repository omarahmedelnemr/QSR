import wave
import numpy as np



# obj = wave.open('./arabmyname1.wav')
# segamnts = [(0,0.29024943310657597),(0.29024943310657597,0.6772486772486772),(0.6772486772486772,0.9674981103552531)]
# segamnts = [(0, 1.1071899529042386), (1.1071899529042386, 2.7679748822605967), (2.7679748822605967, 3.3215698587127163), (3.3215698587127163, 4.705557299843014), (4.705557299843014, 5.812747252747252), (5.812747252747252, 7.19673469387755), (7.19673469387755, 7.47353218210361), (7.47353218210361, 8.30392464678179), (8.30392464678179, 9.411114599686028), (9.411114599686028, 10.518304552590267), (10.518304552590267, 11.625494505494506)]
segamnts = [(0, 1.0565079365079366), (1.0565079365079366, 2.414875283446712), (2.414875283446712, 3.7732426303854876)]
# signals_wave = obj.readframes(-1)
# signals_array = np.frombuffer(signals_wave, dtype=np.int16)
# channels = obj.getnchannels()
# width    = obj.getsampwidth()
# framrate = obj.getframerate()
# print(len(signals_array)/framrate)


import wave
import numpy as np
# audio_file = 'arabmyname1.wav'
# audio_file = './Cut/CutSample.wav'
audio_file = '10000047.wav'
obj = wave.open(audio_file)
import librosa

signals_wave = obj.readframes(-1)
signals_array = np.frombuffer(signals_wave, dtype=np.int16)
channels = obj.getnchannels()
width    = obj.getsampwidth()
framrate = obj.getframerate()
duration_seconds = obj. getnframes() / obj. getframerate()
print(f"Duration {duration_seconds}")
print(f"Duration {librosa.get_duration(path=audio_file)}")
print(len(signals_array))
import math

for i in range(len(segamnts)):
    start = round((segamnts[i][0] / duration_seconds ) * len(signals_array))
    end = round((segamnts[i][1] / duration_seconds ) * len(signals_array))

    print(f"Start: {start}, Ends: {end}")

    
    t = signals_array[start:end]

    nw = wave.open(f"./sigmants/sigmant {i} Test.wav", 'wb')
    nw.setnchannels(channels)
    nw.setsampwidth(width)
    nw.setframerate(framrate)
    nw.writeframes(t)
    nw.close()

