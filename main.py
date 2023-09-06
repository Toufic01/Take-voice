import pyaudio
import wave
import os

# Configuration
output_folder = "recordings"
os.makedirs(output_folder, exist_ok=True)
output_filename = os.path.join(output_folder, "output.wav")
record_seconds = 5  # Adjust the duration of recording as needed

# Initialize the audio stream
audio = pyaudio.PyAudio()

# Open a microphone stream
stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

print("Recording...")

frames = []
for _ in range(0, int(44100 / 1024 * record_seconds)):
    data = stream.read(1024)
    frames.append(data)

print("Recording finished.")

# Close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the audio as a WAV file
with wave.open(output_filename, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))

print(f"Audio saved as {output_filename}")
