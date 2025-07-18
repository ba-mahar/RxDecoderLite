from PIL import Image
import pytesseract
from transformers import pipeline

# 1. Extract text (OCR)


def extract_text(image_path, tesseract_path=None):
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

# 2. Explain medicine names using local model


def explain_text(text):
    pipe = pipeline("text2text-generation", model="google/flan-t5-base")
    prompt = f"Explain the following medicine(s) in simple terms:\n{text}"
    output = pipe(prompt, max_new_tokens=150)[0]['generated_text']
    return output
