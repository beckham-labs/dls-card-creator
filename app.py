import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Foreign Elite Kit Hub", page_icon="👕", layout="centered")

# Advanced Premium Dark-Aesthetic Styling
st.markdown("""
    <style>
    .main { background-color: #060913; color: #ffffff; }
    h1 { text-align: center; font-family: 'Arial Black', sans-serif; color: #00ffcc; font-size: 36px; text-shadow: 0 0 15px rgba(0,255,204,0.3); }
    .kit-card {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        border: 2px solid #334155;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }
    .kit-title { font-size: 22px; font-weight: 800; color: #ffffff; margin-top: 10px; }
    .kit-subtitle { font-size: 14px; color: #38bdf8; margin-bottom: 10px; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ DLS 26 ELITE KIT INJECTOR")
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:16px;'>Copy official high-resolution 512x512 uniform URLs for the world's biggest clubs instantly!</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- MODERN CATEGORY TABS ---
tab_laliga, tab_premier, tab_ucl_special = st.tabs(["🇪🇸 La Liga Giants", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League Heavyweights", "🌟 Special UCL Concepts"])

# --- DATA DATABASE (High-Quality Foreign Images and Working Links) ---
kits_database = {
    "laliga": [
        {
            "name": "Real Madrid (Home Gold)", "desc": "Official White & Metallic Gold Galácticos Edition", 
            "img": "https://unsplash.com", 
            "url": "https://imgur.com"
        },
        {
            "name": "FC Barcelona (Classic Retro)", "desc": "Blaugrana Spotify Special Anniversary Kit", 
            "img": "https://unsplash.com", 
            "url": "https://imgur.com"
        }
    ],
    "premier": [
        {
            "name": "Manchester City (Sky Blue)", "desc": "Official Etihad Champions Edition Kit", 
            "img": "https://unsplash.com", 
            "url": "https://imgur.com"
        },
        {
            "name": "Arsenal FC (Gunners Red)", "desc": "Sleek Emirates Red & White Gold Trim Jersey", 
            "img": "https://unsplash.com", 
            "url": "https://imgur.com"
        }
    ],
    "concepts": [
        {
            "name": "Paris Saint-Germain (Jordan Pink)", "desc": "Hyper-Trending Neon Purple & Pink Fusion Kit", 
            "img": "https://unsplash.com", 
            "url": "https://imgur.com"
        },
        {
            "name": "Chelsea FC (Carbon Stealth)", "desc": "Matte Black & Electric Blue Cyberpunk Uniform", 
            "img": "https://unsplash.com", 
            "url": "https://imgur.com"
        }
    ]
}

# --- RENDER TAB 1: LA LIGA GIANTS ---
with tab_laliga:
    for kit in kits_database["laliga"]:
        st.markdown(f'<div class="kit-card"><div class="kit-title">{kit["name"]}</div><div class="kit-subtitle">{kit["desc"]}</div></div>', unsafe_allow_html=True)
        st.image(kit["img"], use_container_width=True)
        st.text_input("📋 Tap below & copy URL to paste inside DLS game settings:", kit['url'], key=kit['name'])
        st.write("<br><br>", unsafe_allow_html=True)

# --- RENDER TAB 2: PREMIER LEAGUE HEAVYWEIGHTS ---
with tab_premier:
    for kit in kits_database["premier"]:
        st.markdown(f'<div class="kit-card"><div class="kit-title">{kit["name"]}</div><div class="kit-subtitle">{kit["desc"]}</div></div>', unsafe_allow_html=True)
        st.image(kit["img"], use_container_width=True)
        st.text_input("📋 Tap below & copy URL to paste inside DLS game settings:", kit['url'], key=kit['name'])
        st.write("<br><br>", unsafe_allow_html=True)

# --- RENDER TAB 3: SPECIAL UCL CONCEPTS ---
with tab_ucl_special:
    for kit in kits_database["concepts"]:
        st.markdown(f'<div class="kit-card"><div class="kit-title">{kit["name"]}</div><div class="kit-subtitle">{kit["desc"]}</div></div>', unsafe_allow_html=True)
        st.image(kit["img"], use_container_width=True)
        st.text_input("📋 Tap below & copy URL to paste inside DLS game settings:", kit['url'], key=kit['name'])
        st.write("<br><br>", unsafe_allow_html=True)

# Footer Disclaimer
st.markdown("<br><hr><p style='text-align: center; color: #64748b; font-size: 11px;'>🛑 LEGAL DISCLAIMER: Unofficial foreign fan directory. All assets belong to their respective football clubs and First Touch Games Ltd.</p>", unsafe_allow_html=True)
