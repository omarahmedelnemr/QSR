from pydub import AudioSegment
import nltk
import matplotlib.pyplot as plt
# nltk.download('punkt')

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
print(f"Duration = {audio.duration_seconds}")
print(f"Duration = {audio.duration_seconds}")


# Print the word segments
final = []
for i, segment in enumerate(word_segments):
    word = words[i]
    start = segment[0]   # Convert milliseconds to seconds
    end = segment[1]   # Convert milliseconds to seconds
    print(f"Word {i+1}: {word}, Start: {start} s, End: {end} s")
    final.append((start,end))

print(final)
