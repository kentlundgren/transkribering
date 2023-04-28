ain3.py
import requests
import subprocess
import openai

# efter att blivit peppad av podden "Teknik i akademi" https://poddtoppen.se/podcast/1661532745/teknik-i-akademi
# gjordes detta försök att göra ett program som använder sig av OpenAI:s Whisper för att transkribera från ljud till text
         # https://openai.com/research/whisper
# Detta är tredje försöket, med ett program som går via OpenAI:s API
# MEN ett (av flera...;>) problem med programmet är fortfarande problem att den inte hittar ffmpeg på rad 29

# Användarens sökväg till ljudfilen på webben
audio_path = input("Ange sökväg till ljudfilen på webben: ")

# Hämta ljudfilen från webben
try:
    response = requests.get(audio_path)
    response.raise_for_status()
    with open("audio.mp3", "wb") as f:
        f.write(response.content)
    print("Ljudfilen har hämtats.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP-fel: {e}")
except requests.exceptions.RequestException as e:
    print(f"Fel vid hämtning av ljudfil: {e}")
    exit()

# Konvertera ljudfilen till WAV-format
try:
    subprocess.run(["ffmpeg", "-i", "audio.mp3", "audio.wav"])
    print("Ljudfilen har konverterats till WAV-format.")
except subprocess.CalledProcessError as e:
    print(f"Fel vid konvertering av ljudfil till WAV-format: {e}")
    exit()

# Transkribera ljudfilen med Whispers API
try:
    response = requests.post(
        "https://api.whisper.ai/v1/transcriptions",
        headers={"Authorization": "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"},
        json={"config": {"languageCode": "en-US", "audioChannelCount": 1}},
        files={"audio": ("audio.wav", open("audio.wav", "rb"), "audio/wav")},
    )
    response.raise_for_status()
    print("Transkribering klar.")
    print(response.json()["text"])
except requests.exceptions.HTTPError as e:
    print(f"HTTP-fel: {e}")
except requests.exceptions.RequestException as e:
    print(f"Fel vid anrop till Whispers API: {e}")
    exit()
