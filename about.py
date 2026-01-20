import streamlit as st
import streamlit.components.v1 as components

def show_about_page():
    components.html(
        """
        <div style="padding: 20px; font-family: Arial, sans-serif; line-height: 1.6; color: #eaeaea;">
            <h2 style="color:#2C3E50;">About OCR Reader for Visually Impaired</h2>

            <p>
                This application is designed to make reading accessible for
                <strong>visually impaired users</strong>.
            </p>

            <h3 style="color:#2C3E50;">How It Helps</h3>
            <ul>
                <li>Capture printed or handwritten pages</li>
                <li>Extract text using OCR</li>
                <li>Text-to-speech output</li>
                <li>Summarization support</li>
            </ul>

            <h3 style="color:#2C3E50;">Key Features</h3>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <div style="border:1px solid #3498DB; padding:10px; border-radius:8px;">OCR Bounding Boxes</div>
                <div style="border:1px solid #3498DB; padding:10px; border-radius:8px;">Clean Extracted Text</div>
                <div style="border:1px solid #3498DB; padding:10px; border-radius:8px;">Text to Speech</div>
            </div>
        </div>
        """,
        height=600,
        scrolling=True
    )
