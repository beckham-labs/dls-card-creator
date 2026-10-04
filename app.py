import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Custom Card Creator", page_icon="⚽", layout="centered")
st.title("⚽ DLS 26 Face Card Creator")
st.write("Design your card and go viral on TikTok!")

# --- MAIN SCREEN CONTROLS ---
st.header("👤 Player Customization")
player_name = st.text_input("Player Name", "BECKHAM")
card_type = st.selectbox("Card Tier", ["Legendary (Gold)", "Rare (Blue)", "Common (Grey)"])

# Photo Upload Box directly on center page
uploaded_file = st.file_uploader("📸 Upload Face Photo (Selfie or Player)", type=["jpg", "jpeg", "png"])

# Tier Colors Configuration
tier_colors = {
    "Legendary (Gold)": {"bg": "#D4AF37", "text": "#000000", "accent": "#FFFDD0"},
    "Rare (Blue)": {"bg": "#1E90FF", "text": "#FFFFFF", "accent": "#E0FFFF"},
    "Common (Grey)": {"bg": "#A9A9A9", "text": "#FFFFFF", "accent": "#F5F5F5"}
}

st.header("📊 Attributes (Max 99)")
speed = st.slider("Speed (SPE)", 1, 99, 95)
acceleration = st.slider("Acceleration (ACC)", 1, 99, 95)
stamina = st.slider("Stamina (STA)", 1, 99, 88)
control = st.slider("Control (CON)", 1, 99, 92)
strength = st.slider("Strength (STR)", 1, 99, 80)
tackling = st.sidebar.slider("Tackling (TAC)", 1, 99, 60) if 'st' in locals() else 60 # safe fallback
passing = st.slider("Passing (PAS)", 1, 99, 90)
shooting = st.slider("Shooting (SHO)", 1, 99, 94)

# Calculate dynamic overall rating
overall_rating = int((speed + acceleration + control + passing + shooting) / 5)

# --- IMAGE GENERATION ENGINE ---
def generate_dls_card(face_image):
    card_color = tier_colors[card_type]["bg"]
    text_color = tier_colors[card_type]["text"]
    
    # Create Card Base Canvas (Width: 400, Height: 550)
    card = Image.new("RGB", (400, 550), color=card_color)
    draw = ImageDraw.Draw(card)
    
    # Outer Border Line
    draw.rectangle([(10, 10), (390, 540)], outline=tier_colors[card_type]["accent"], width=5)
    
    # Paste User Photo if uploaded
    if face_image is not None:
        try:
            user_img = Image.open(face_image).convert("RGBA")
            user_img = user_img.resize((180, 200))
            card.paste(user_img, (180, 110), user_img if user_img.mode == 'RGBA' else None)
        except Exception:
            draw.rectangle([(180, 110), (360, 310)], fill="#333333")
    else:
        draw.rectangle([(180, 110), (360, 310)], fill="#555555")
        
    # Dark Stats Panel Background Box at Bottom
    draw.rectangle([(25, 340), (375, 520)], fill="#111111")
    
    try:
        font_name = ImageFont.load_default()
    except Exception:
        font_name = None

    # Draw Big Rating and Player Name Text
    draw.text((40, 50), f"{overall_rating}", fill=text_color, font=font_name, size=55)
    draw.text((40, 120), "OVR", fill=text_color, font=font_name, size=18)
    draw.text((40, 280), player_name.upper(), fill=text_color, font=font_name, size=28)
    
    # Render DLS Stats Grid Lines
    stats_data = [
        f"SPE: {speed}   ACC: {acceleration}",
        f"STA: {stamina}   CON: {control}",
        f"STR: {strength}   PAS: {passing}",
        f"SHO: {shooting}"
    ]
    
    y_pos = 360
    for line in stats_data:
        draw.text((45, y_pos), line, fill="#FFFFFF", font=font_name, size=22)
        y_pos += 36
        
    return card

# --- LIVE INTERFACE DISPLAY ---
st.header("🖼️ Your Live DLS 26 Card")
card_image = generate_dls_card(uploaded_file)
st.image(card_image, caption="Preview of download asset", use_container_width=True)

# --- DOWNLOAD BUTTON ---
buf = BytesIO()
card_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📥 Download Card Image",
    data=byte_im,
    file_name=f"dls26_{player_name.lower().replace(' ', '_')}.png",
    mime="image/png"
)

# Legal Footer
st.markdown("<br><hr><p style='text-align: center; color: gray; font-size: 11px;'>🛑 DISCLAIMER: Unofficial community fan tool. Not associated with First Touch Games.</p>", unsafe_allow_html=True)
