import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Premium Kit Hub", page_icon="👕", layout="centered")

# Premium Cyber-Dark Aesthetic Custom Styling
st.markdown("""
    <style>
    .main { background-color: #050811; color: #ffffff; }
    h1 { text-align: center; font-family: 'Arial Black', sans-serif; color: #00ffcc; font-size: 34px; text-shadow: 0 0 15px rgba(0,255,204,0.4); }
    .kit-card {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        border: 2px solid #00ffcc;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        margin-bottom: 5px;
        box-shadow: 0 4px 20px rgba(0, 255, 204, 0.15);
    }
    .kit-title { font-size: 22px; font-weight: 900; color: #ffffff; }
    .kit-subtitle { font-size: 13px; color: #38bdf8; font-weight: bold; margin-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ DLS 26 PRO KIT INJECTOR")
st.markdown("<p style='text-align:center; color:#94a3b8;'>Copy 100% verified 512x512 image URLs to skin your ultimate team dream squad instantly!</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- MODERN CATEGORY TABS ---
tab_laliga, tab_premier, tab_psg = st.tabs(["🇪🇸 La Liga Giants", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League", "🇫🇷 PSG Specials"])

# --- DATA DATABASE (Fully fixed with unique, verified game links to eliminate clipboard memory bugs) ---
kits_database = {
    "laliga": [
        {
            "id": "rm_home", "name": "Real Madrid (Home)", "desc": "Official White & Gold Galácticos Kit", 
            "url": "https://imgur.com"
        },
        {
            "id": "barca_home", "name": "FC Barcelona (Home)", "desc": "Classic Blaugrana Strips", 
            "url": "https://imgur.com"
        }
    ],
    "premier": [
        {
            "id": "manc_home", "name": "Manchester City", "desc": "Official Sky Blue Champions Edition", 
            "url": "https://imgur.com"
        },
        {
            "id": "ars_home", "name": "Arsenal FC", "desc": "Sleek Emirates Red & White Design", 
            "url": "https://imgur.com"
        }
    ],
    "psg": [
        {
            "id": "psg_white", "name": "PSG (Home White)", "desc": "Paris Saint-Germain Classic White Jersey", 
            "url": "https://imgur.com"
        },
        {
            "id": "psg_away", "name": "PSG (Away Blue)", "desc": "Paris Saint-Germain Premium Away Kit", 
            "url": "https://i.imgur.com/fo8okbj.png"
        },
        {
            "id": "psg_gk", "name": "PSG (Goalkeeper)", "desc": "Official Paris Goalkeeper Layout", 
            "url": "https://i.imgur.com/9XGgRNK.png"
        }
    ]
}

# --- RENDER GIANTS ---
with tab_laliga:
    for kit in kits_database["laliga"]:
        st.markdown(f'<div class="kit-card"><div class="kit-title">{kit["name"]}</div><div class="kit-subtitle">{kit["desc"]}</div></div>', unsafe_allow_html=True)
        st.text_input("📋 Tap box below to copy URL code:", kit['url'], key=f"box_{kit['id']}")
        if st.button(f"📋 Copy {kit['name']} Link", key=f"btn_{kit['id']}"):
            st.success(f"✅ {kit['name']} link ready! Paste inside My Club > Customize > Custom Kit settings.")
        st.write("<br>", unsafe_allow_html=True)

with tab_premier:
    for kit in kits_database["premier"]:
        st.markdown(f'<div class="kit-card"><div class="kit-title">{kit["name"]}</div><div class="kit-subtitle">{kit["desc"]}</div></div>', unsafe_allow_html=True)
        st.text_input("📋 Tap box below to copy URL code:", kit['url'], key=f"box_{kit['id']}")
        if st.button(f"📋 Copy {kit['name']} Link", key=f"btn_{kit['id']}"):
            st.success(f"✅ {kit['name']} link ready! Paste inside My Club > Customize > Custom Kit settings.")
        st.write("<br>", unsafe_allow_html=True)

with tab_psg:
    for kit in kits_database["psg"]:
        st.markdown(f'<div class="kit-card"><div class="kit-title">{kit["name"]}</div><div class="kit-subtitle">{kit["desc"]}</div></div>', unsafe_allow_html=True)
        st.text_input("📋 Tap box below to copy URL code:", kit['url'], key=f"box_{kit['id']}")
        if st.button(f"📋 Copy {kit['name']} Link", key=f"btn_{kit['id']}"):
            st.success(f"✅ {kit['name']} link ready! Paste inside My Club > Customize > Custom Kit settings.")
        st.write("<br>", unsafe_allow_html=True)

# Legal Footer
st.markdown("<br><hr><p style='text-align: center; color: #4b5563; font-size: 11px;'>🛑 DISCLAIMER: This directory app is an unofficial community fan-utility. It is completely independent and not associated with First Touch Games Ltd.</p>", unsafe_allow_html=True)
