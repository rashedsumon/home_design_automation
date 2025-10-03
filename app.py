import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.floorplan_to_json import floorplan_to_json
import os

st.title("🏠 Floorplan to JSON POC")

uploaded_file = st.file_uploader("Upload a PDF Floorplan", type="pdf")

if uploaded_file:
    st.info("Processing PDF...")
    # Save temporarily
    temp_path = os.path.join("data", "temp.pdf")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())
    
    # Extract text
    texts = extract_text_from_pdf(temp_path)
    
    # Convert to JSON
    output_file = os.path.join("output", uploaded_file.name.replace(".pdf", ".json"))
    floorplan_to_json(texts, output_file)
    
    st.success(f"✅ JSON created: {output_file}")
    st.download_button("Download JSON", output_file)
