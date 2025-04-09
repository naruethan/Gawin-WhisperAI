from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)

# Load the Whisper model once when the server starts
model = whisper.load_model("tiny")  # You can change to "base", "small", etc.

@app.route('/transcribe', methods=['GET'])
def transcribe_audio():
    # Get audio file path from the query parameters
    file_path = request.args.get('file_path')

    model = whisper.load_model("tiny")

# Path to your audio file
    audio_file = "C:/kawin/work test/Whisper AI/voip.wav"  # Use full path if needed

# Process the audio
    result = model.transcribe(audio_file, fp16=False)
    return jsonify({"transcription": result["text"]})
    
    # if not file_path:
    #     return jsonify({"error": "No file_path provided"}), 400
    
    # try:
    #     # Check if file exists
    #     if not os.path.exists(file_path):
    #         return jsonify({"error": f"File not found: {file_path}"}), 404
        
    #     # Transcribe the audio
    #     result = model.transcribe(file_path, fp16=False)
        
    #     # Return the transcription
    #     return jsonify({"transcription": result["text"]})
    
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500


@app.route('/' ,methods=['GET'])
def Hello():
    return "HElloword"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)