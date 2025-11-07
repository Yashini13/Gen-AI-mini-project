# # import speech_recognition as sr

# # def get_voice_input(file_path='sample_audio.wav'):
# #     recognizer = sr.Recognizer()

# #     try:
# #         if file_path:  # read from audio file
# #             print(f"📂 Trying to open file: {file_path}")
# #             with sr.AudioFile(file_path) as source:
# #                 print("🎧 Reading audio...")
# #                 audio = recognizer.record(source)
# #         else:
# #             print("🎤 Listening from microphone...")
# #             with sr.Microphone() as source:
# #                 recognizer.adjust_for_ambient_noise(source)
# #                 audio = recognizer.listen(source)

# #         print("🌀 Sending audio to Google Speech API...")
# #         text = recognizer.recognize_google(audio)
# #         print("🗣 Recognized:", text)
# #         return text

# #     except sr.UnknownValueError:
# #         print("❌ Could not understand audio")
# #         return ""
# #     except sr.RequestError as e:
# #         print("⚠️ API error:", e)
# #         return ""
# #     except Exception as e:
# #         print(f"🔥 Unexpected error: {e}")
# #         return ""

# import openai
# import speech_recognition as sr



# def get_voice_input(file_path='sample_audio.wav'):
#     recognizer = sr.Recognizer()

#     try:
#         if file_path:  # read from audio file
#             print(f"📂 Trying to open file: {file_path}")
#             with sr.AudioFile(file_path) as source:
#                 print("🎧 Reading audio...")
#                 audio = recognizer.record(source)

#             # save temporary WAV to send to OpenAI
#             temp_file = "temp_audio.wav"
#             with open(temp_file, "wb") as f:
#                 f.write(audio.get_wav_data())

#             print("🌀 Sending audio to OpenAI Whisper API...")
#             with open(temp_file, "rb") as f:
#                 transcript = openai.audio.transcriptions.create(
#                     model="whisper-1",
#                     file=f
#                 )
#             print("🗣 Recognized:", transcript.text)
#             return transcript.text

#         else:
#             print("🎤 Listening from microphone...")
#             with sr.Microphone() as source:
#                 recognizer.adjust_for_ambient_noise(source)
#                 audio = recognizer.listen(source)

#             temp_file = "temp_mic_audio.wav"
#             with open(temp_file, "wb") as f:
#                 f.write(audio.get_wav_data())

#             print("🌀 Sending audio to OpenAI Whisper API...")
#             with open(temp_file, "rb") as f:
#                 transcript = openai.audio.transcriptions.create(
#                     model="whisper-1",
#                     file=f
#                 )
#             print("🗣 Recognized:", transcript.text)
#             return transcript.text

#     except Exception as e:
#         print(f"🔥 Error: {e}")
#         return ""

import sounddevice as sd
import wavio
import openai
import speech_recognition as sr


# 🎤 Live mic transcription
def get_live_audio_transcription(duration=5, fs=16000):
    print(f"🎤 Recording {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    filename = "mic_audio.wav"
    wavio.write(filename, audio, fs, sampwidth=2)
    print(f"✅ Saved audio to {filename}")

    with open(filename, "rb") as f:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    print("🗣 Recognized:", transcript.text)
    return transcript.text


# 🎵 File transcription
def get_voice_input(file_path="sample_audio.wav"):
    try:
        with open(file_path, "rb") as f:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=f
            )
        print("🗣 Recognized (file):", transcript.text)
        return transcript.text
    except Exception as e:
        print(f"🔥 Error reading file: {e}")
        return ""

