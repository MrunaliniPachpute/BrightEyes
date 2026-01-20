import streamlit as st
import glob
import cv2
import pytesseract
import summarize
import azure_tts
import time

from about import show_about_page

# Page config
st.set_page_config(page_title="OCR Reader", layout="wide")

# SIDEBAR
st.sidebar.markdown(
    """
    <style>
    .sidebar-title {
        font-size: 32px;
        font-weight: 600;
        color: #ff4e5b;
        margin-bottom: 12px;
        text-align: center;
        letter-spacing: 0.5px;
    }
    </style>
    <div class="sidebar-title">OCR App Menu</div>
    """,
    unsafe_allow_html=True
)

def animated_title(text, delay=0.05, color="#FFD700"):  # Deep blue color
    placeholder = st.empty()
    display_text = ""
    for char in text:
        display_text += char
        placeholder.markdown(
            f"<b><p style='color: {color}; font-family: Arial, sans-serif;'>{display_text}</p></b>", 
            unsafe_allow_html=True
        )
        time.sleep(delay)


page = st.sidebar.radio("Go to", ["Home", "About"])

if page == "About":
    show_about_page()
    st.stop()

# Homepage
st.title("📷 Captured Frames & Readable Text")
animated_title("View frames captured from your device and their extracted text.")


# Load saved frames
image_files = sorted(glob.glob("frames/*.jpg"))

if len(image_files) == 0:
    st.warning("No captured frames found. Run main.py to capture frames first.")
    st.stop()

# Set Tesseract command
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

final_text = ""

# Display frames and OCR text
for idx, img_path in enumerate(image_files):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert to grayscale and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Get OCR data (including word bounding boxes)
    data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
    text = " ".join([data['text'][i] for i in range(len(data['text'])) if int(data['conf'][i]) > 50]).strip()

    # Draw rectangles around detected words
    img_ocr = img_rgb.copy()
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 50:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            cv2.rectangle(img_ocr, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangles

    final_text += f"\n{text}"

    st.markdown(f"### Frame {idx+1}")
    col1, col2, col3 = st.columns([1, 1, 1.2])

    with col1:
        st.image(img_rgb, caption=f"Original Frame {idx+1}", use_container_width=True)
    with col2:
        st.image(img_ocr, caption=f"OCR Detected Frame {idx+1}", use_container_width=True)
    with col3:
        st.text_area("Detected Text", value=text, height=150, key=f"text_{idx}")

st.markdown("---")
st.subheader("🔊 Combined Text from All Frames")
st.text_area("Combined Text", value=final_text.strip(), height=250, key="final_text")

# Audio options
st.markdown("### 🎧 Text-to-Speech Options")
choice = st.radio("Select Option:", ["Listen Full Text", "Summarize + Listen"])

if st.button("Play Audio"):
    if choice == "Listen Full Text":
        text_to_speak = final_text
    else:
        with st.spinner("Generating summary..."):
            text_to_speak = summarize.summarize_text(final_text)
        st.success("Summary generated!")

    # Azure TTS
    audio_file = azure_tts.speak_text_azure(text_to_speak)
    st.audio(audio_file, start_time=0)

# Extra styling
st.markdown("""
<style>
    .stTextArea textarea {background-color:#f9f9f9; color:#222; font-size:14px;}
    .stButton>button {background-color:#4CAF50; color:white; font-weight:bold;}
    .stRadio>div {flex-direction: row;}
</style>
""", unsafe_allow_html=True)
