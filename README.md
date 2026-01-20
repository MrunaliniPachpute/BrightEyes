# OCR Reader for Visually Impaired

An accessible application designed to help **visually impaired users** read printed or handwritten text effortlessly. The app captures images, extracts text using **OCR (Optical Character Recognition)**, and converts it into **natural audio output**, enabling an interactive reading experience.

---

## 🌟 Features

- **Capture & Scan**: Take photos of printed or handwritten pages.
- **Text Extraction**: Automatically detect and extract text from images.
- **Audio Output**: Listen to the extracted text with **text-to-speech** functionality.
- **Summarization**: Summarize long texts for faster understanding.
- **Multi-Page Support**: Combine text from multiple images into a single seamless audio stream.
- **OCR Highlights**: Highlights detected words in captured images for visual reference (if needed).

---

## 🎯 How It Helps

This tool empowers users with visual challenges to:  
- Access printed content independently  
- Listen to books, notes, or documents on the go  
- Reduce reliance on external help for reading  

---

## 🖥️ Screenshots

<img width="500" height="717" alt="Screenshot (1442)" src="https://github.com/user-attachments/assets/eae36a03-b07f-4e93-b5ce-69ac7fa4319c" />

<img width="500" height="704" alt="Screenshot (1443)" src="https://github.com/user-attachments/assets/e6fa5280-7cf9-49dd-a4f1-9fe3f320f004" />

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/BrightEyes.git
cd BrightEyes.git
```

2. Create a virtual environment and activate it:
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run the app:
```
streamlit run app.py
```
---

## 🛠️ Technologies Used

- **Python**  
- **Streamlit** for the interactive UI  
- **OpenCV** for image processing  
- **Pytesseract** for OCR  
- **gTTS / pyttsx3** for Text-to-Speech  
- **Summarization Library** (optional, e.g., `transformers`)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:  
- Report bugs  
- Suggest new features  
- Improve UI/UX or audio experience  

---

## 🙏 Acknowledgements

Special thanks to the communities behind:  
- [Streamlit](https://streamlit.io/)  
- [Pytesseract](https://pypi.org/project/pytesseract/)  
- [OpenCV](https://opencv.org/)  

---

> **Note:** This application is primarily aimed at assisting visually impaired users by converting printed text into audio, making reading inclusive and interactive.
