import os
import subprocess

# Install Whisper package using pip
subprocess.run(["pip", "install", "--upgrade", "--no-deps", "--force-reinstall", "git+https://github.com/openai/whisper.git"])

# Prompt user to enter path to the audio file
audio_path = input("Enter path to the audio file: ")

# Convert audio file to wav format using ffmpeg
output_path = os.path.splitext(audio_path)[0] + ".wav"
subprocess.run(["ffmpeg", "-i", audio_path, output_path])

# Transcribe the audio using Whisper
with open(output_path, "rb") as f:
    audio_bytes = f.read()

response = subprocess.run(["whisper", "transcribe"], input=audio_bytes, capture_output=True)

# Print the transcription result
print(response.stdout.decode("utf-8"))
