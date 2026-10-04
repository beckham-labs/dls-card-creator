import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Premium Card Creator", page_icon="⚽", layout="centered")
st.title("⚽ NEXT-GEN DLS 26 CREATOR")
st.write("Design high-fidelity custom neon shield cards ready for TikTok trends!")

# --- MAIN SCREEN CONTROLS ---
st.header("👤 Player Customization")
player_name = st.text_input("Player Name", "BECKHAM")
card_type = st.selectbox("Card Tier Style", ["Legendary Neon Gold", "Cyberpunk Electric Blue", "Carbon Stealth Grey"])
player_position = st.selectbox("Field Position", ["ST", "CF", "LW", "RW", "CM", "CB", "GK"])

uploaded_file = st.file_uploader("📸 Upload Face Photo (Selfie or Pro)", type=["jpg", "jpeg", "png"])

# Modern High-End Color Palette Themes
theme_colors = {
    "Legendary Neon Gold": {"border": "#FFD700", "bg_dark": "#1A1400", "bg_light": "#4D3D00", "text": "#FFD700", "panel": "#0A0800"},
    "Cyberpunk Electric Blue": {"border": "#00E5FF", "bg_dark": "#001326", "bg_light": "#003366", "text": "#00E5FF", "panel": "#000A14"},
    "Carbon Stealth Grey": {"border": "#FFFFFF", "bg_dark": "#1A1A1A", "bg_light": "#333333", "text": "#FFFFFF", "panel": "#0D0D0D"}
}

current_theme = theme_colors[card_type]

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

# --- MODERN GEOMETRIC SHIELD GENERATOR ---
def generate_modern_card(face_image):
    # Create main crisp canvas block (400 width x 540 height)
    card = Image.new("RGB", (400, 540), color=current_theme["bg_dark"])
    draw = ImageDraw.Draw(card)
    
    # 1. Draw overlapping modern polygonal gradient shield structures
    outer_shield = [(30, 20), (370, 20), (390, 420), (200, 520), (10, 420)]
    inner_shield = [(36, 26), (364, 26), (382, 414), (200, 510), (18, 414)]
    shimmer_top = [(36, 26), (364, 26), (374, 240), (26, 240)]
    
    draw.polygon(outer_shield, fill=current_theme["border"])
    draw.polygon(inner_shield, fill=current_theme["bg_dark"])
    draw.polygon(shimmer_top, fill=current_theme["bg_light"]) # Light reflection effect on upper half
    
    # 2. Paste User Face Photo into a stylized right-justified frame window
    photo_poly = [(180, 80), (350, 80), (365, 290), (165, 290)]
    if face_image is not None:
        try:
            user_img = Image.open(face_image).convert("RGB")
            user_img = user_img.resize((180, 210))
            card.paste(user_img, (180, 80))
        except Exception:
            draw.polygon(photo_poly, fill=current_theme["panel"])
    else:
        draw.polygon(photo_poly, fill=current_theme["panel"])
        
    # 3. Draw Matte Dark Bottom Stats Container panel box
    stats_container = [(40, 320), (360, 320), (372, 400), (200, 495), (28, 400)]
    draw.polygon(stats_container, fill=current_theme["panel"])
    
    # 4. Draw Position Badge tag frame
    draw.rectangle([(45, 255), (105, 285)], fill=current_theme["border"])
    
    # Text rendering engine routines (safe system fonts mapping)
    try:
        f_style = ImageFont.load_default()
    except Exception:
        f_style = None

    # 5. Overlay Graphic text assets
    draw.text((45, 45), f"{overall_rating}", fill=current_theme["text"], font=f_style)
    draw.text((45, 105), "OVR", fill="#8a99ad", font=f_style)
    
    # Render selected player positions inside tag
    draw.text((55, 260), player_position, fill="#000000", font=f_style)
    
    # Render Player Name Label cleanly centered across line break paths
    draw.text((45, 290), player_name.upper(), fill="#FFFFFF", font=f_style)
    
    # Display 8 attributes in parallel grid strings inside base matte container panel
    stat_y = 335
    col1_strings = [f"SPE  {speed}", f"ACC  {acceleration}", f"STA  {stamina}", f"CON  {control}"]
    for entry in col1_strings:
        draw.text((55, stat_y), entry, fill="#FFFFFF", font=f_style)
        stat_y += 32
        
    stat_y = 335
    col2_strings = [f"STR  {strength}", f"TAC  {tackling}", f"PAS  {passing}", f"SHO  {shooting}"]
    for entry in col2_strings:
        draw.text((225, stat_y), entry, fill="#FFFFFF", font=f_style)
        stat_y += 32
        
    return card

# --- LIVE INTERFACE RENDERING ENGINE ---
st.header("🖼️ Your Live DLS 26 Card")
final_card_image = generate_modern_card(uploaded_file)
st.image(final_card_image, caption="Polished Neon Shield Asset", use_container_width=True)

# --- DIRECT MEMORY DOWNLOAD TRIGGERS ---
buf = BytesIO()
final_card_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📥 Download Card Image",
    data=byte_im,
    file_name=f"dls26_{player_name.lower().replace(' ', '_')}.png",
    mime="image/png"
)

st.markdown("<br><hr><p style='text-align: center; color: gray; font-size: 11px;'>🛑 DISCLAIMER: Unofficial fan tool. Not associated with First Touch Games.</p>", unsafe_allow_html=True)
