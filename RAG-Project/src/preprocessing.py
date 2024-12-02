import fitz 
import whisper
import pytesseract
from PIL import Image
import docx

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return " ".join([page.get_text() for page in doc])

def read_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([para.text for para in doc.paragraphs])

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    return model.transcribe(file_path)["text"]

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)
