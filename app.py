import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Custom Card Creator", page_icon="⚽", layout="centered")
st.title("⚽ Authentic DLS 26 Card Creator")
st.write("Design high-fidelity shield cards engineered to trend on TikTok!")

# --- MAIN SCREEN CONTROLS ---
st.header("👤 Player Customization")
player_name = st.text_input("Player Name", "BECKHAM")
card_type = st.selectbox("Card Tier", ["Legendary (Gold)", "Rare (Blue)", "Common (Grey)"])
player_position = st.selectbox("Position", ["CF", "ST", "LW", "RW", "AM", "CM", "DM", "CB", "LB", "RB", "GK"])

# Photo Upload Box
uploaded_file = st.file_uploader("📸 Upload Face Photo (Selfie or Player)", type=["jpg", "jpeg", "png"])

# Authentic Tier Themes (Background Gradients & Accent Colors matching real game styles)
tier_themes = {
    "Legendary (Gold)": {
        "border_outer": "#FFD700", "border_inner": "#B8860B", 
        "bg_top": "#FFE4E1", "bg_bottom": "#D4AF37", "text": "#000000", "panel_bg": "#141414"
    },
    "Rare (Blue)": {
        "border_outer": "#00BFFF", "border_inner": "#1E4620", 
        "bg_top": "#E0FFFF", "bg_bottom": "#1E90FF", "text": "#FFFFFF", "panel_bg": "#0D1B2A"
    },
    "Common (Grey)": {
        "border_outer": "#D3D3D3", "border_inner": "#555555", 
        "bg_top": "#F5F5F5", "bg_bottom": "#7F8C8D", "text": "#FFFFFF", "panel_bg": "#1C1C1C"
    }
}

st.header("📊 Attributes (Max 99)")
speed = st.slider("Speed (SPE)", 1, 99, 92)
acceleration = st.slider("Acceleration (ACC)", 1, 99, 93)
stamina = st.slider("Stamina (STA)", 1, 99, 85)
control = st.slider("Control (CON)", 1, 99, 90)
strength = st.slider("Strength (STR)", 1, 99, 78)
tackling = st.slider("Tackling (TAC)", 1, 99, 55)
passing = st.slider("Passing (PAS)", 1, 99, 88)
shooting = st.slider("Shooting (SHO)", 1, 99, 91)

# Calculate dynamic overall rating
overall_rating = int((speed + acceleration + control + passing + shooting) / 5)

# --- ADVANCED DLS SHIELD DRAWING ENGINE ---
def generate_dls_card(face_image):
    theme = tier_themes[card_type]
    
    # 1. Base Transparent Canvas (Width: 420, Height: 580)
    card = Image.new("RGBA", (420, 580), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    
    # Define exact geometry for a sharp DLS Shield structure
    # Top left, Top right, Mid right, Bottom center-point, Mid left
    outer_shield_points = [(40, 20), (380, 20), (400, 440), (210, 560), (20, 440)]
    inner_shield_points = [(45, 26), (375, 26), (394, 436), (210, 550), (26, 436)]
    
    # 2. Draw Shield Layers
    draw.polygon(outer_shield_points, fill=theme["border_outer"])
    draw.polygon(inner_shield_points, fill=theme["bg_bottom"])
    
    # Create subtle upper lighting gradient panel inside shield
    top_shimmer = [(45, 26), (375, 26), (385, 290), (35, 290)]
    draw.polygon(top_shimmer, fill=theme["bg_top"])
    
    # 3. Paste Face Image inside clean window frame
    photo_box = [(190, 100), (370, 100), (380, 310), (180, 310)]
    if face_image is not None:
        try:
            user_img = Image.open(face_image).convert("RGBA")
            user_img = user_img.resize((190, 210))
            
            # Mask photo neatly to match the right edge slant
            photo_mask = Image.new("L", (190, 210), 0)
            mask_draw = ImageDraw.Draw(photo_mask)
            mask_draw.rectangle([0, 0, 190, 210], fill=255)
            
            card.paste(user_img, (185, 100), photo_mask)
        except Exception:
            draw.polygon(photo_box, fill="#2c3e50")
    else:
        # Default placeholder shape matching real card layouts
        draw.polygon(photo_box, fill="#34495e")
        
    # 4. Matte Black Stats Panel Box at Bottom
    stats_panel_points = [(45, 340), (375, 340), (388, 430), (210, 535), (32, 430)]
    draw.polygon(stats_panel_points, fill=theme["panel_bg"])
    
    # 5. Position Badge Frame
    draw.rectangle([(45, 280), (110, 315)], fill=theme["border_outer"])
    
    # Fonts initialization
    try:
        font_main = ImageFont.load_default()
    except Exception:
        font_main = None

    # 6. Render Text Graphics (Ratings, Position, Name & Attributes)
    draw.text((50, 40), f"{overall_rating}", fill=theme["text"], font=font_main, size=65)
    draw.text((55, 120), "OVR", fill=theme["text"], font=font_main, size=16)
    
    # Position marker text
    draw.text((55, 285), player_position, fill="#000000" if "Gold" in card_type else "#FFFFFF", font=font_main, size=22)
    
    # Player Name Capitalized
    draw.text((45, 305), player_name.upper(), fill=theme["text"], font=font_main, size=26)
    
    # 8 Main Game Attributes formatted into structured Columns
    col1_y = 355
    col1_stats = [f"SPE  {speed}", f"ACC  {acceleration}", f"STA  {stamina}", f"CON  {control}"]
    for stat in col1_stats:
        draw.text((65, col1_y), stat, fill="#FFFFFF", font=font_main, size=20)
        col1_y += 34
        
    col2_y = 355
    col2_stats = [f"STR  {strength}", f"TAC  {tackling}", f"PAS  {passing}", f"SHO  {shooting}"]
    for stat in col2_stats:
        draw.text((230, col2_y), stat, fill="#FFFFFF", font=font_main, size=20)
        col2_y += 34
        
    return card.convert("RGB") # Convert back to standard image for downloading

# --- LIVE INTERFACE DISPLAY ---
st.header("🖼️ Your Live DLS 26 Card")
card_image = generate_dls_card(uploaded_file)
st.image(card_image, caption="Polished DLS Shield Asset", use_container_width=True)

# --- DOWNLOAD ACTION SYSTEM ---
buf = BytesIO()
card_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📥 Download Card Image",
    data=byte_im,
    file_name=f"dls26_{player_name.lower().replace(' ', '_')}.png",
    mime="image/png"
)

st.markdown("<br><hr><p style='text-align: center; color: gray; font-size: 11px;'>🛑 DISCLAIMER: Unofficial community fan tool. Not associated with First Touch Games.</p>", unsafe_allow_html=True)
