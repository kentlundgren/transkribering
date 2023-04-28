import os
import subprocess

# efter att blivit peppad av podden "Teknik i akademi" https://poddtoppen.se/podcast/1661532745/teknik-i-akademi
# gjordes detta försök att göra ett program som använder sig av OpenAI:s Whisper för att transkribera från ljud till text
         # https://openai.com/research/whisper
# se bakgrunden i konversation med ChatGPT https://chat.openai.com/c/07a229c1-c7ba-4a78-8acf-51c5d4fcf8fe 
# samt under 1 min "genomgång" https://drive.google.com/file/d/1NpZ6hMHPPeeBSdBNIcUOaeEH6D_hj182/view 
# ett (av flera...;>) problem med programmet nedan - är att den inte hittar ffmpeg

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
