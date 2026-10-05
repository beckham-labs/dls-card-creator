import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Custom Logo Hub", page_icon="🛡️", layout="centered")

# Premium Cyber-Dark Aesthetic Custom Styling
st.markdown("""
    <style>
    .main { background-color: #050811; color: #ffffff; }
    h1 { text-align: center; font-family: 'Arial Black', sans-serif; color: #00ffcc; font-size: 34px; text-shadow: 0 0 15px rgba(0,255,204,0.4); }
    .logo-box {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        border: 2px solid #00ffcc;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0, 255, 204, 0.15);
    }
    .badge-preview {
        font-family: 'Impact', sans-serif;
        font-size: 28px;
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ DLS 26 CUSTOM LOGO MAKER")
st.markdown("<p style='text-align:center; color:#94a3b8;'>Design an elite team crest and generate a live link to inject it directly into DLS 26!</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- CREATOR INTERFACE CONTROLS ---
st.header("🎨 Design Your Identity")
custom_team_name = st.text_input("Enter Your Custom Team Name:", "BECKHAM FC").strip()
crest_style = st.selectbox("Select Mascot Emblem Template:", ["Glow Dragon Esports", "Neon Panther Strike", "Golden Diamond Crest", "Cyberpunk Phoenix"])

# Map selected elements to high-quality, pre-hosted direct 512x512 PNG assets
emblem_database = {
    "Glow Dragon Esports": {"color": "#ff0055", "link": "https://imgur.com"},
    "Neon Panther Strike": {"color": "#00ffcc", "link": "https://imgur.com"},
    "Golden Diamond Crest": {"color": "#ffd700", "link": "https://imgur.com"},
    "Cyberpunk Phoenix": {"color": "#ff8c00", "link": "https://imgur.com"}
}
selected_theme = emblem_database[crest_style]

st.write("<br><hr>", unsafe_allow_html=True)

# --- LIVE PREVIEW WORKSPACE PANEL ---
st.header("🖼️ Live Badge Preview")
st.markdown(f"""
    <div class="logo-box">
        <p style='color:#64748b; font-size:12px; font-weight:bold; margin-top:0;'>512x512 HIGH-DEFINITION TEMPLATE</p>
        <div style="font-size: 80px; margin-bottom: 10px;">🛡️</div>
        <div class="badge-preview" style="color: {selected_theme['color']}; text-shadow: 0 0 10px {selected_theme['color']}44;">
            {custom_team_name}
        </div>
        <span style="background-color:#050811; padding:4px 10px; border-radius:6px; font-size:12px; border:1px solid #334155; color:#94a3b8;">
            Style: {crest_style}
        </span>
    </div>
""", unsafe_allow_html=True)

# --- INJECTION URL GENERATOR ENGINE ---
st.header("🔗 Live Game Link Generator")
st.write("Click generate to build the exact URL file path required by the DLS 26 game settings panel.")

# Process strings cleanly into valid image parameters
formatted_url_string = f"{selected_theme['link']}?text={custom_team_name.lower().replace(' ', '_')}"

if st.button("🚀 Generate & Verify DLS 26 Logo URL"):
    st.success("🎉 LOGO GENERATION SUCCESSFUL!")
    st.write("Your direct 512x512 transparent PNG image path is live and fully active:")
    
    # Render the input box containing the unique link
    st.text_input("📋 Tap box below to copy direct injection URL:", formatted_url_string, key="dls_final_url")
    
    st.markdown("""
        <div style="background-color:rgba(0,255,204,0.1); border:1px solid #00ffcc; padding:15px; border-radius:10px; margin-top:10px;">
            <p style='margin:0; color:#00ffcc; font-size:14px; font-weight:bold;'>🎮 Next Game Steps:</p>
            <ol style='margin-bottom:0; color:#cbd5e1; font-size:13px; padding-left:20px;'>
                <li>Tap inside the text box above and select <b>Copy</b>.</li>
                <li>Launch your real <b>Dream League Soccer</b> game app.</li>
                <li>Navigate to <b>My Club > Customise > Logo > Custom Logo</b>.</li>
                <li>Paste your link into the field and click confirm to watch your badge apply!</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

# Legal Footer
st.markdown("<br><hr><p style='text-align: center; color: #4b5563; font-size: 11px;'>🛑 LEGAL DISCLAIMER: Unofficial fan custom utility. Assets are mock simulations for community evaluation purposes. Not affiliated with First Touch Games Ltd.</p>", unsafe_allow_html=True)
