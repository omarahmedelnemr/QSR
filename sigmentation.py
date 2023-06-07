from pydub import AudioSegment
import nltk
import matplotlib.pyplot as plt
import wave
import numpy as np
nltk.download('punkt')

# Load the audio file
audio_file = './TestData/10000047.wav'
sentence = 'فَصَلِّ لِرَبِّكَ وَانْحَرْ'

audio = AudioSegment.from_wav(audio_file)

# Convert the audio to raw data
raw_data = audio.raw_data

# Perform word segmentation using nltk
words = nltk.word_tokenize(sentence)

# Calculate the duration of each word segment
word_segments = []
current_start = 0
for word in words:
    duration = audio.duration_seconds * len(word) / len(sentence)
    current_end = current_start + duration
    word_segments.append((current_start, current_end))
    current_start = current_end


# Print the word segments
total_segments = []
for i, segment in enumerate(word_segments):
    word = words[i]
    start = segment[0] 
    end = segment[1]  
    print(f"Word {i+1}: {word}, Start: {start} s, End: {end} s")
    total_segments.append((start,end))


# Save Segments as new Files
obj = wave.open(audio_file)

signals_wave = obj.readframes(-1)
signals_array = np.frombuffer(signals_wave, dtype=np.int16)
channels = obj.getnchannels()
width    = obj.getsampwidth()
framrate = obj.getframerate()
duration_seconds = obj. getnframes() / obj. getframerate()

for i in range(len(total_segments)):
    # Get The Start and End in Frames
    start = round((total_segments[i][0] / duration_seconds ) * len(signals_array))
    end = round((total_segments[i][1] / duration_seconds ) * len(signals_array))


    # Create New File
    new_file_wave = signals_array[start:end]
    nw = wave.open(f"./sigmants/sigmant {i} Test.wav", 'wb')
    nw.setnchannels(channels)
    nw.setsampwidth(width)
    nw.setframerate(framrate)
    nw.writeframes(new_file_wave)
    nw.close()




print("Done... Look at Segments Folder")
# print(total_segments)
