import streamlit as st
def show_about_page():
    st.markdown("""
<div style="padding: 20px; font-family: Arial, sans-serif; line-height: 1.6;">
    <h2 style="color: #2C3E50;">About OCR Reader for Visually Impaired</h2>

    <p>
        This application is designed to make reading accessible for
        <strong>visually impaired users</strong>.
    </p>

    <h3 style="color: #2C3E50;">How It Helps</h3>
    <ul>
        <li>Capture printed or handwritten pages.</li>
        <li>Extract text using OCR.</li>
        <li>Text-to-speech support.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
