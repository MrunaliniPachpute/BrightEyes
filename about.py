import streamlit.components.v1 as components

def show_about_page():
    components.html(
        """
        <div style="
            padding: 30px;
            font-family: Arial, sans-serif;
            line-height: 1.7;
            color: #EAEAEA;
            background-color: transparent;
        ">

            <!-- MAIN TITLE -->
            <h1 style="
                font-size: 48px;
                font-weight: 700;
                color: #ECF6FF;
                text-align: center;
                margin-bottom: 25px;
                letter-spacing: 1px;
            ">
                About OCR Reader for Visually Impaired
            </h1>

            <p style="font-size: 18px;">
                This application is designed to make reading accessible for
                <strong>visually impaired users</strong>.
                By scanning printed or handwritten pages, the app extracts text using
                <strong>OCR (Optical Character Recognition)</strong> and converts it into
                <strong>clear, natural audio output</strong>, allowing users to listen
                to content effortlessly.
            </p>

            <h2 style="color:#8FCBFF; margin-top:30px;">How It Helps</h2>
            <ul style="font-size: 17px;">
                <li>Capture printed or handwritten pages using your device camera</li>
                <li>Automatically detect and extract text from images</li>
                <li>Listen to extracted text using text-to-speech</li>
                <li>Summarize long text for faster understanding</li>
                <li>Combine text from multiple images into one audio stream</li>
            </ul>

            <h2 style="color:#8FCBFF; margin-top:30px;">Key Features</h2>
            <div style="display:flex; flex-wrap:wrap; gap:14px;">

                <div style="padding:14px; border:1px solid #5DADE2; border-radius:10px; flex:1; min-width:220px;">
                    Displays original captured frames
                </div>

                <div style="padding:14px; border:1px solid #5DADE2; border-radius:10px; flex:1; min-width:220px;">
                    Highlights detected words with OCR bounding boxes
                </div>

                <div style="padding:14px; border:1px solid #5DADE2; border-radius:10px; flex:1; min-width:220px;">
                    Shows clean extracted text
                </div>

                <div style="padding:14px; border:1px solid #5DADE2; border-radius:10px; flex:1; min-width:220px;">
                    Text-to-speech and summarization support
                </div>
            </div>

            <p style="margin-top: 30px; font-size: 18px;">
                This tool makes reading
                <strong style="color:#9FE2BF;">inclusive</strong>,
                <strong style="color:#9FE2BF;">simple</strong>,
                and
                <strong style="color:#9FE2BF;">independent</strong>
                for users with visual challenges.
            </p>

        </div>
        """,
        height=700,
        scrolling=True
    )
