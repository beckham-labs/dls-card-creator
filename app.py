import streamlit as st
import base64
from io import BytesIO
from PIL import Image

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Next-Gen Card Creator", page_icon="⚽", layout="centered")

# --- STYLING THE USER INTERFACE ---
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #ffffff; }
    h1 { text-align: center; font-family: 'Arial Black', sans-serif; color: #00ffcc; letter-spacing: 2px; }
    p { text-align: center; color: #8a99ad; }
    div.stSlider > div > div > div > div { background-color: #00ffcc !important; }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ NEXT-GEN DLS 26 CREATOR")
st.write("Futuristic ultra-modern card engine optimized for viral social media content.")

# --- USER CONTROLS ---
st.header("👤 Customize Attributes")
player_name = st.text_input("Player Name", "BECKHAM")
card_type = st.selectbox("Card Tier Style", ["Legendary Gold Neon", "Cyberpunk Blue Glow", "Carbon Stealth Grey"])
player_position = st.selectbox("Field Position", ["ST", "CF", "LW", "RW", "CM", "CB", "GK"])

uploaded_file = st.file_uploader("📸 Upload Player Face (Selfie or Pro)", type=["jpg", "jpeg", "png"])

# Multi-column slider structure for smooth mobile scrolling
col1, col2 = st.columns(2)
with col1:
    speed = st.slider("Speed (SPE)", 1, 99, 95)
    acceleration = st.slider("Acceleration (ACC)", 1, 99, 94)
    stamina = st.slider("Stamina (STA)", 1, 99, 88)
    control = st.slider("Control (CON)", 1, 99, 92)
with col2:
    strength = st.slider("Strength (STR)", 1, 99, 82)
    tackling = st.slider("Tackling (TAC)", 1, 99, 65)
    passing = st.slider("Passing (PAS)", 1, 99, 90)
    shooting = st.slider("Shooting (SHO)", 1, 99, 93)

overall_rating = int((speed + acceleration + control + passing + shooting) / 5)

# --- MODERN THEME STYLE ENGINE ---
theme_styles = {
    "Legendary Gold Neon": {
        "border": "linear-gradient(135deg, #ffd700, #ff8c00)", "glow": "0 0 25px rgba(255, 215, 0, 0.6)",
        "card_bg": "linear-gradient(180deg, rgba(40,30,0,0.95) 0%, rgba(15,10,0,0.98) 100%)", "text": "#ffd700"
    },
    "Cyberpunk Blue Glow": {
        "border": "linear-gradient(135deg, #00bfff, #0022ff)", "glow": "0 0 25px rgba(0, 191, 255, 0.6)",
        "card_bg": "linear-gradient(180deg, rgba(0,20,40,0.95) 0%, rgba(0,5,15,0.98) 100%)", "text": "#00bfff"
    },
    "Carbon Stealth Grey": {
        "border": "linear-gradient(135deg, #8e9eab, #eef2f3)", "glow": "0 0 25px rgba(255, 255, 255, 0.2)",
        "card_bg": "linear-gradient(180deg, rgba(28,28,28,0.95) 0%, rgba(10,10,10,0.98) 100%)", "text": "#ffffff"
    }
}

current_theme = theme_styles[card_type]

# Convert uploaded image to string format so it can load smoothly inside the design frame
img_base64 = ""
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    img_base64 = f"data:image/png;base64,{base64.b64encode(bytes_data).decode()}"
else:
    # High-tech glowing placeholder if empty
    img_base64 = "https://unsplash.com"

# --- THE ADVANCED HIGH-TECH HTML/CSS IMAGE DESIGN ---
html_card_layout = f"""
<div style="display: flex; justify-content: center; padding: 20px; background-color: #0b0f19;">
    <div style="
        width: 320px; height: 480px;
        background: {current_theme['card_bg']};
        border-radius: 24px;
        padding: 4px;
        background-origin: border-box;
        background-image: {current_theme['border']};
        box-shadow: {current_theme['glow']};
        position: relative;
        font-family: 'Segoe UI', Roboto, sans-serif;
        overflow: hidden;
    ">
        <!-- Top Stats Row -->
        <div style="position: absolute; top: 25px; left: 25px; display: flex; flex-direction: column; align-items: center;">
            <span style="font-size: 54px; font-weight: 900; color: {current_theme['text']}; line-height: 1; text-shadow: 0 0 10px rgba(0,0,0,0.5);">{overall_rating}</span>
            <span style="font-size: 14px; font-weight: 700; color: #8a99ad; margin-top: 4px; letter-spacing: 1px;">OVR</span>
            <div style="background: {current_theme['border']}; color: #000; font-size: 12px; font-weight: 900; padding: 3px 10px; border-radius: 6px; margin-top: 12px;">
                {player_position}
            </div>
        </div>

        <!-- Futuristic Glow Image Frame -->
        <div style="
            position: absolute; top: 25px; right: 25px;
            width: 140px; height: 160px;
            border-radius: 16px;
            background-image: url('{img_base64}');
            background-size: cover;
            background-position: center;
            border: 2px solid rgba(255,255,255,0.1);
            box-shadow: inset 0 0 20px rgba(0,0,0,0.6);
        "></div>

        <!-- Name Display Panel -->
        <div style="position: absolute; top: 215px; width: 100%; text-align: center;">
            <h2 style="margin: 0; font-size: 26px; font-weight: 900; color: #ffffff; letter-spacing: 1.5px; text-transform: uppercase; text-shadow: 0 2px 4px rgba(0,0,0,0.8); font-family: 'Impact', sans-serif;">
                {player_name}
            </h2>
        </div>

        <!-- Modern Technical Attributes Grid -->
        <div style="
            position: absolute; bottom: 25px; left: 15px; right: 15px;
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 15px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px 20px;
            border: 1px solid rgba(255,255,255,0.05);
        ">
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">SPE</span><span style="color:#00ffcc;">{speed}</span></div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">STR</span><span style="color:#00ffcc;">{strength}</span></div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">ACC</span><span style="color:#00ffcc;">{acceleration}</span></div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">TAC</span><span style="color:#00ffcc;">{tackling}</span></div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">STA</span><span style="color:#00ffcc;">{stamina}</span></div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">PAS</span><span style="color:#00ffcc;">{passing}</span></div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">CON</span><span style="color:#00ffcc;">{control}</span></div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700;"><span style="color:#8a99ad;">SHO</span><span style="color:#00ffcc;">{shooting}</span></div>
        </div>
    </div>
</div>
"""

# Render the beautiful next-gen card interface live
st.markdown(html_card_layout, unsafe_allow_html=True)

st.info("💡 Pro-Tip: To save this new high-definition design layout on your mobile phone, simply press down on the card and tap 'Save Image' or take a quick screenshot to post directly to TikTok!")
st.markdown("<br><hr><p style='font-size: 11px;'>🛑 LEGAL DISCLAIMER: Unofficial community fan utility. Not affiliated with First Touch Games.</p>", unsafe_allow_html=True)
