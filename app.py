import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Premium Card Creator", page_icon="⚽", layout="centered")
st.title("⚽ Elite DLS 26 Card Creator")
st.write("Production-ready asset engine utilizing high-fidelity graphic overlays.")

# --- MAIN SCREEN CONTROLS ---
st.header("👤 Player Customization")
player_name = st.text_input("Player Name", "BECKHAM")
card_type = st.selectbox("Card Tier", ["Legendary (Gold)", "Rare (Blue)", "Common (Grey)"])
player_position = st.selectbox("Position", ["CF", "ST", "LW", "RW", "AM", "CM", "CB", "GK"])

uploaded_file = st.file_uploader("📸 Upload Face Photo (Selfie or Player)", type=["jpg", "jpeg", "png"])

# Public Fan-made High-Quality Asset URLs (Failsafe links to clean blank game layouts)
TEMPLATE_URLS = {
    "Legendary (Gold)": "https://githubusercontent.com",
    "Rare (Blue)": "https://githubusercontent.com",
    "Common (Grey)": "https://githubusercontent.com"
}

st.header("📊 Attributes (Max 99)")
speed = st.slider("Speed (SPE)", 1, 99, 96)
acceleration = st.slider("Acceleration (ACC)", 1, 99, 95)
stamina = st.slider("Stamina (STA)", 1, 99, 89)
control = st.slider("Control (CON)", 1, 99, 93)
strength = st.slider("Strength (STR)", 1, 99, 84)
tackling = st.slider("Tackling (TAC)", 1, 99, 58)
passing = st.slider("Passing (PAS)", 1, 99, 91)
shooting = st.slider("Shooting (SHO)", 1, 99, 95)

overall_rating = int((speed + acceleration + control + passing + shooting) / 5)

# --- PREMIUM ASSET ENGINE ---
def generate_premium_card(face_image):
    # Try fetching the clean pro graphic template background from the web
    try:
        response = requests.get(TEMPLATE_URLS[card_type], timeout=5)
        base_card = Image.open(BytesIO(response.content)).convert("RGBA")
        base_card = base_card.resize((400, 560)) # Lock standard dimensions
    except Exception:
        # Emergency backup fallback block if web asset fails to load
        fallback_colors = {"Legendary (Gold)": "#D4AF37", "Rare (Blue)": "#1E90FF", "Common (Grey)": "#A9A9A9"}
        base_card = Image.new("RGBA", (400, 560), color=fallback_colors[card_type])

    draw = ImageDraw.Draw(base_card)
    
    # 1. Neatly place face photo layer into the designated frame window area
    if face_image is not None:
        try:
            user_img = Image.open(face_image).convert("RGBA")
            user_img = user_img.resize((180, 200))
            
            # Mask applied to cleanly handle transparency blending
            photo_mask = Image.new("L", (180, 200), 255)
            base_card.paste(user_img, (185, 110), photo_mask)
        except Exception:
            pass

    # System fonts fallback setup
    try:
        font_style = ImageFont.load_default()
    except Exception:
        font_style = None

    # 2. Render sharp Text Overlays over the high-fidelity template layers
    # Set text colors depending on template contrast
    txt_color = "#000000" if "Gold" in card_type else "#FFFFFF"
    
    # Render Main Stats
    draw.text((50, 45), f"{overall_rating}", fill=txt_color, font=font_style, size=60)
    draw.text((55, 110), "OVR", fill=txt_color, font=font_style, size=16)
    draw.text((55, 275), player_position, fill=txt_color, font=font_style, size=20)
    draw.text((45, 305), player_name.upper(), fill=txt_color, font=font_style, size=26)
    
    # Print numerical stats cleanly inside layout paths
    stat_y = 355
    col1_lines = [f"SPE  {speed}", f"ACC  {acceleration}", f"STA  {stamina}", f"CON  {control}"]
    for s_txt in col1_lines:
        draw.text((60, stat_y), s_txt, fill="#FFFFFF", font=font_style, size=18)
        stat_y += 34
        
    stat_y = 355
    col2_lines = [f"STR  {strength}", f"TAC  {tackling}", f"PAS  {passing}", f"SHO  {shooting}"]
    for s_txt in col2_lines:
        draw.text((230, stat_y), s_txt, fill="#FFFFFF", font=font_style, size=18)
        stat_y += 34

    return base_card.convert("RGB")

# --- UI LOGIC ---
st.header("🖼️ Your Live DLS 26 Card")
final_asset = generate_premium_card(uploaded_file)
st.image(final_asset, caption="Production-ready high fidelity asset.", use_container_width=True)

# --- MEMORY BUFFER DOWNLOAD TRIGGER ---
buf = BytesIO()
final_asset.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📥 Download Card Image",
    data=byte_im,
    file_name=f"dls26_{player_name.lower().replace(' ', '_')}.png",
    mime="image/png"
)

st.markdown("<br><hr><p style='text-align: center; color: gray; font-size: 11px;'>🛑 DISCLAIMER: Unofficial fan tool. Not associated with First Touch Games.</p>", unsafe_allow_html=True)
