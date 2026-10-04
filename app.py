import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Pro Card Creator", page_icon="⚽", layout="centered")

# Custom injection to give the page web app a dark midnight aesthetic
st.markdown("""
    <style>
    .main { background-color: #060913; color: #ffffff; }
    h1 { text-align: center; font-family: 'Arial Black', sans-serif; color: #00ffcc; }
    div.stSlider > div > div > div > div { background-color: #00ffcc !important; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ ELITE DLS 26 CARD ENGINE")
st.write("Clean, professional design framework engineered for maximum TikTok views.")

# --- MAIN SCREEN CONTROLS ---
st.header("👤 Card Customization")
player_name = st.text_input("Player Name", "BECKHAM")
card_type = st.selectbox("Select Card Premium Theme", ["Titanium Neon Gold", "Vortex Electric Blue", "Midnight Carbon Matte"])
player_position = st.selectbox("Field Position", ["ST", "CF", "LW", "RW", "CM", "CB", "GK"])

uploaded_file = st.file_uploader("📸 Upload Face Photo (Selfie or Player)", type=["jpg", "jpeg", "png"])

# Modern High-Contrast Color Presets
theme_configs = {
    "Titanium Neon Gold": {"accent": "#FFD700", "bg_main": "#151001", "bg_panel": "#261D02", "text_primary": "#FFD700"},
    "Vortex Electric Blue": {"accent": "#00E5FF", "bg_main": "#010F1C", "bg_panel": "#021A30", "text_primary": "#00E5FF"},
    "Midnight Carbon Matte": {"accent": "#FFFFFF", "bg_main": "#141414", "bg_panel": "#242424", "text_primary": "#FFFFFF"}
}
cfg = theme_configs[card_type]

st.header("📊 Attributes (Max 99)")
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

# --- THE PRO RENDERING ENGINE ---
def generate_pro_card(face_image):
    # Set Canvas Dimensions (420px width x 560px height)
    card = Image.new("RGB", (420, 560), color=cfg["bg_main"])
    draw = ImageDraw.Draw(card)
    
    # 1. Clean Neon Framed Inner Border
    draw.rectangle([(15, 15), (405, 545)], outline=cfg["accent"], width=4)
    
    # 2. Add Face Photo Layer inside a clean geometric box frame
    if face_image is not None:
        try:
            user_img = Image.open(face_image).convert("RGB")
            user_img = user_img.resize((190, 210))
            card.paste(user_img, (190, 75))
        except Exception:
            draw.rectangle([(190, 75), (380, 285)], fill=cfg["bg_panel"])
    else:
        # High contrast slate placeholder if empty
        draw.rectangle([(190, 75), (380, 285)], fill="#1A2436")

    # 3. Transparent High-Tech Attribute Box at the Bottom
    draw.rectangle([(35, 330), (385, 520)], fill=cfg["bg_panel"], outline="rgba(255,255,255,0.1)", width=1)
    
    # 4. Clean Position Badge Tag Frame
    draw.rectangle([(45, 245), (115, 280)], fill=cfg["accent"])
    
    try:
        f_style = ImageFont.load_default()
    except Exception:
        f_style = None

    # 5. Overlay Clean and Sized Typography Text
    # Big Bold Rating Layout
    draw.text((45, 40), f"{overall_rating}", fill=cfg["text_primary"], font=f_style)
    draw.text((45, 100), "OVR", fill="#6B7A90", font=f_style)
    
    # Position Tag Text
    draw.text((58, 252), player_position, fill="#000000", font=f_style)
    
    # Capitalized Player Name Centered Perfectly Above Stats Layout
    draw.text((45, 292), player_name.upper(), fill="#FFFFFF", font=f_style)
    
    # 8 Main Game Attributes Formatted into Balanced Dual Columns
    stat_y = 350
    col1_lines = [f"SPE   {speed}", f"ACC   {acceleration}", f"STA   {stamina}", f"CON   {control}"]
    for line_text in col1_lines:
        draw.text((60, stat_y), line_text, fill="#FFFFFF", font=f_style)
        stat_y += 36
        
    stat_y = 350
    col2_lines = [f"STR   {strength}", f"TAC   {tackling}", f"PAS   {passing}", f"SHO   {shooting}"]
    for line_text in col2_lines:
        draw.text((230, stat_y), line_text, fill="#FFFFFF", font=f_style)
        stat_y += 36
        
    return card

# --- LIVE PREVIEW GENERATION ---
st.header("🖼️ Your Live DLS 26 Card")
polished_card = generate_pro_card(uploaded_file)
st.image(polished_card, caption="Clean Next-Gen High Contrast Presentation Layout", use_container_width=True)

# --- DOWNLOAD BUFFER ACTION TRIGGER ---
buf = BytesIO()
polished_card.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📥 Download Card Image",
    data=byte_im,
    file_name=f"dls26_{player_name.lower().replace(' ', '_')}.png",
    mime="image/png"
)

st.markdown("<br><hr><p style='text-align: center; color: #4A5568; font-size: 11px;'>🛑 LEGAL DISCLAIMER: Unofficial community fan tool. Not associated with First Touch Games.</p>", unsafe_allow_html=True)
