import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def clean_text(text):
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line or line.isdigit():
            continue
        if "Company:" in line or "Version:" in line or "Date:" in line:
            continue
        cleaned.append(line)
    return cleaned

def structure_to_markdown(lines):
    md_lines = []
    for line in lines:
        if line.startswith("•"):
            md_lines.append(f"- {line[1:].strip()}")
        elif line.endswith(":"):
            md_lines.append(f"## {line}")
        elif line.istitle():
            md_lines.append(f"# {line}")
        else:
            md_lines.append(line)
    return "\n".join(md_lines)

def convert_pdf_to_markdown(pdf_path, md_path):
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_lines = clean_text(raw_text)
    markdown = structure_to_markdown(cleaned_lines)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown)
