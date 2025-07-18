import streamlit as st
import pytesseract  # ✅ Missing in your original code
from utils import extract_text, explain_text

# Set default path for Windows if not provided by user
default_tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.set_page_config(page_title="RxDecoder Lite", layout="centered")

st.title("🧠 RxDecoder Lite")
st.caption(
    "Decode handwritten prescriptions with AI (fully local, beginner-friendly).")

uploaded_file = st.file_uploader(
    "📤 Upload Prescription Image", type=["png", "jpg", "jpeg"])

# Let user optionally provide custom tesseract path
tesseract_path = st.text_input(
    "📍 (Optional) Enter Tesseract Path if needed (Windows only):")

# Use default if empty
if not tesseract_path:
    tesseract_path = default_tesseract_path

# Apply path
pytesseract.pytesseract.tesseract_cmd = tesseract_path

if uploaded_file:
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.read())

    st.image("temp_image.png", caption="Uploaded Prescription",
             use_column_width=True)

    if st.button("🩺 Decode Prescription"):
        with st.spinner("🔍 Extracting medicine names..."):
            extracted_text = extract_text("temp_image.png", tesseract_path)
            st.success("✅ OCR Completed!")
            st.text_area("📃 Extracted Text:", extracted_text, height=150)

        with st.spinner("🧠 Generating Explanation..."):
            explanation = explain_text(extracted_text)
            st.success("✅ AI Explanation Ready!")
            st.text_area("📖 Explanation:", explanation, height=200)
