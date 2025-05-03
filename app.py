import os
from flask import Flask, request, jsonify, render_template
from converter import convert_pdf_to_markdown



app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file provided."}), 400
    file = request.files['file']
    if file.filename == '' or not file.filename.endswith('.pdf'):
        return jsonify({"success": False, "message": "Invalid file format. Please upload a PDF."}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        convert_pdf_to_markdown(filepath, "output.md")
        with open("output.md", "r", encoding="utf-8") as f:
            md_content = f.read()
        return jsonify({"success": True, "markdown": md_content})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
