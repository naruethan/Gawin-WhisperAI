import whisper

# Load the model
model = whisper.load_model("tiny")

# Path to your audio file
audio_file = "C:/kawin/work test/Whisper AI/voip.wav"  # Use full path if needed

# Process the audio
result = model.transcribe(audio_file, fp16=False)

# Output the transcription
print(result["text"])