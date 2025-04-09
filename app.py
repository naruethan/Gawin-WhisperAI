from flask import Flask, request, jsonify
import whisper
import os


app = Flask(__name__)




# Load the Whisper model once when the server starts
model = whisper.load_model("tiny")  # You can change to "base", "small", etc.

@app.route('/transcribe2', methods=['GET'])
def transcribe_audio():
    
    file_path = request.args.get('file_path')
    print(file_path)
    import subprocess

    # 🎩 Monkey patch subprocess.Popen เพื่อซ่อน CMD window
    _original_popen = subprocess.Popen
    def _hidden_popen(*args, **kwargs):
        kwargs.setdefault("creationflags", subprocess.CREATE_NO_WINDOW)
        return _original_popen(*args, **kwargs)
    subprocess.Popen = _hidden_popen


    
    if not file_path:
        return jsonify({"error": "No file_path provided"}), 400
    
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            return jsonify({"error": f"File not found: {file_path}"}), 404
        
        # Transcribe the audio
        result = model.transcribe(file_path, fp16=False)
        
        # Return the transcription
        return jsonify({"transcription": result["text"]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route('/' ,methods=['GET'])
def Hello():
    return "HElloword"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)