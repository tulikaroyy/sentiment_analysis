import streamlit as st
from transformers import pipeline

# Initialize BERT sentiment classifier
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Desktop and mobile backgrounds
desktop_bg_url = "https://images8.alphacoders.com/939/939716.png"
mobile_bg_url = "https://wallpapercave.com/wp/wp14270778.png"

st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&family=Orbitron:wght@700&display=swap" rel="stylesheet">
<style>
body, .stApp {{
    background-image: url('{desktop_bg_url}');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    min-height: 100vh;
    image-rendering: pixelated;
}}
@media only screen and (max-width: 650px) {{
    body, .stApp {{
        background-image: url('{mobile_bg_url}');
    }}
}}
.main-content-wrapper {{
    margin-top: 60px; /* Shifts content down by ~1-2 lines */
}}
.pixel-title {{
    font-family: 'Press Start 2P', 'VT323', monospace;
    color: #f2e9e4;
    font-size: 2.1rem;
    text-align: center;
    margin-top: 38px;
    margin-bottom: 12px;
    text-shadow: 2px 2px 0 #9a8c98, 0 0 14px #c9ada7;
    letter-spacing: 2px;
    filter: drop-shadow(2px 2px 1px #23223b);
}}
.pixel-label {{
    font-family: 'Press Start 2P', 'VT323', monospace;
    color: #f2e9e4;
    font-size: 0.97rem;
    margin-bottom: 10px;
    margin-top: 10px;
    display: block;
    letter-spacing: 1px;
}}
[data-testid="stTextArea"] label {{
    display:none !important;
}}
[data-testid="stTextArea"] textarea {{
    font-family: 'Press Start 2P', 'VT323', monospace;
    background: #f2e9e4;
    color: #22223b;
    font-size: 1.07rem;
    border: 4px solid #9a8c98;
    border-radius: 0px;
    box-shadow: 0 0 0 4px #4a4e69;
    padding: 16px;
    margin-top: 4px;
    margin-bottom: 18px;
    outline: none !important;
    image-rendering: pixelated;
    caret-color: #c9ada7;
    cursor: text;
}}
.stButton > button {{
    font-family: 'Orbitron', 'Press Start 2P', 'VT323', monospace !important;
    font-size: 1.16rem !important;
    color: #22223b;
    background: linear-gradient(90deg, #f2e9e4 0%, #c9ada7 100%);
    border: 4px solid #22223b;
    border-radius: 0;
    box-shadow: 0 3px 0 #9a8c98, 0 0 14px #22223b;
    padding: 12px 32px;
    margin-top: 14px;
    letter-spacing: 1.5px;
    transition: all 0.12s;
    outline: none;
    position: relative;
    overflow: hidden;
    image-rendering: pixelated;
    cursor: pointer;
}}
.stButton > button:active {{
    top: 3px;
    left: 2px;
    background: linear-gradient(90deg, #c9ada7 0%, #9a8c98 100%);
    box-shadow: 0 1px 0 #22223b;
    outline: 2px solid #f2e9e4;
    animation: pixel-press 0.09s;
}}
@keyframes pixel-press {{
    0% {{ transform: translate(0px, 0px); }}
    40% {{ transform: translate(2px, 2px) scale(0.98);}}
    100% {{ transform: translate(0px, 0px); }}
}}
.pixel-result {{
    font-family: 'Press Start 2P', 'VT323', monospace;
    color: #f2e9e4;
    font-size: 1.2rem;
    text-align: center;
    margin-top: 28px;
    margin-bottom: 24px;
    text-shadow: 2px 2px 0 #4a4e69, 0 0 8px #c9ada7;
    border-radius: 8px;
    border: 4px double #9a8c98;
    background: #22223bcc;
    padding: 18px;
    box-shadow: 0 0 14px #4a4e69, 0 0 2px #fff;
    letter-spacing: 1.2px;
}}
.stAlert {{
    border-radius: 8px !important;
    font-family: 'VT323', monospace;
    font-size: 1.08rem;
    background: #9a8c98 !important;
    color: #22223b !important;
    text-shadow: 0 1px 2px #f2e9e4;
}}
.pixel-footer {{
    font-family: 'VT323', monospace;
    color: #c9ada7;
    font-size: 1.05rem;
    margin-top: 42px;
    padding-top: 10px;
    text-align: center;
    letter-spacing: 1px;
}}
/* Responsive font sizes for mobile */
@media only screen and (max-width: 650px) {{
    .pixel-title {{ font-size: 1.2rem !important; }}
    .pixel-label {{ font-size: 0.7rem !important; }}
    .pixel-result {{ font-size: 1rem !important; padding: 10px !important; }}
    .pixel-footer {{ font-size: 0.95rem !important; }}
    .main-content-wrapper {{ margin-top: 35px !important; }}
}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="pixel-title">Your fav Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<label class="pixel-label" for="pixel-textarea">Type your indie thought:</label>', unsafe_allow_html=True)
user_input = st.text_area("", key="pixel-textarea", height=110)
if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = classifier(user_input)[0]
        label = result['label']
        score = result['score']
        st.markdown(
            f'<div class="pixel-result">'
            f'Sentiment: <b>{label.capitalize()}</b><br>'
            f'Confidence: <b>{score:.2f}</b></div>',
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter something to analyze! 🎮")
st.markdown(
    """
    <div class="pixel-footer">
        Made by Tulika with &#x2764; | 
        <a href="https://www.linkedin.com/in/tulikaroyy" target="_blank" style="color:#f2e9e4;text-decoration:underline;">LinkedIn</a> | 
        <a href="https://open.spotify.com/playlist/605WnshSvUcVRN3qt85z0b?si=y760TsGETwGU_E-d4-xZMA&pi=iO2yveS3Sc6Pe&nd=1&dlsi=f8d7d9a6987d4bdf" target="_blank" style="color:#f2e9e4;text-decoration:underline;">Playlist</a>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)