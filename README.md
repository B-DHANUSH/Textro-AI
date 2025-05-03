# 📄 PDF to Structured Markdown Converter

This project provides an end-to-end solution for converting PDF documents into clean, structured Markdown format. It includes a Flask-based REST API, a minimal HTML frontend, and a Python backend for processing and formatting content.

---

## 🚀 Features

- 🧠 Accurate PDF text extraction  
- 🛠️ Markdown conversion with formatting  
- 🔗 REST API with Flask  
- 🌐 Simple frontend UI  
- 📬 Postman test collection  
- 🧪 Error handling for invalid inputs  

---

## ⚙️ Project Structure
pdf-to-md-converter/
│
├── app.py # Flask app
├── converter/
│ ├── init.py
│ ├── pdf_to_text.py # PDF text extraction logic
│ └── text_to_md.py # Markdown formatting logic
│
├── static/
│ └── style.css # Optional styles
├── templates/
│ └── index.html # Upload interface
│
├── test/
│ └── sample.pdf
├── postman_collection.json
└── README.md


---

## 🧰 Tech Stack

- Python 3  
- Flask  
- pdfminer.six / PyMuPDF  
- HTML 
- Postman  

---

## 📦 Modules Overview

### ✅ Module 1: PDF Text Extraction
- Libraries: `pdfminer.six`, `PyMuPDF`
- Removes headers, footers, and unwanted elements
- Extracts and cleans raw text

### ✅ Module 2: Markdown Structuring
- Parses extracted content
- Adds Markdown syntax like `#`, `-`, `**`
- Structures text into sections, lists, headers

### ✅ Module 3: Flask API Integration
- `/convert` – Accepts a PDF and returns Markdown
- `/health` – Checks server status
- Frontend UI for user uploads

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/pdf-to-md-converter.git
   cd pdf-to-md-converter
## Install dependencies
 - pip install -r requirements.txt
## Run the Flask app
-python app.py
## Open in your browser
-http://localhost:5000
## 🔌   API Endpoints

| Method | Endpoint   | Description                   |
| ------ | ---------- | ----------------------------- |
| POST   | `/convert` | Upload a PDF and get Markdown |
| GET    | `/health`  | Returns API status (up/down)  |


## 📬 Postman Example
Request

POST /convert
Content-Type: multipart/form-data
File: sample.pdf
Response
markdown

# Introduction

This document explains...

## Section 1: Overview

- Bullet Point 1
- Bullet Point 2

**Bold Text**


## 🚧 Limitations
No multi-column layout handling

Limited formatting (no images/tables)

Header/footer removal is heuristic-based

## 🔮 Future Enhancements
AI-based layout detection

Export to HTML, DOCX, JSON

Drag-and-drop frontend with live preview

Table and image parsing support
