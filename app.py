import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="TikTok Football Caption Generator", page_icon="📱", layout="centered")

# Premium Neon Social Grid Custom Styling
st.markdown("""
    <style>
    .main { background-color: #090b16; color: #ffffff; }
    h1 { text-align: center; font-family: 'Arial Black', sans-serif; color: #ff007f; font-size: 32px; text-shadow: 0 0 15px rgba(255,0,127,0.4); }
    .caption-box {
        background: linear-gradient(145deg, #111424, #1b1f3b);
        border: 2px solid #ff007f;
        border-radius: 16px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 20px rgba(255, 0, 127, 0.2);
    }
    .box-title { font-size: 14px; font-weight: bold; color: #00ffcc; text-transform: uppercase; letter-spacing: 1px; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 TIKTOK VIRAL CAPTION GENERATOR")
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:15px;'>Generate high-hook descriptions and optimized hashtag grids to explode your views!</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- USER SELECTION CONTROLS ---
st.header("📝 Video Details")
video_topic = st.text_input("What is your video about? (e.g. Free-kick goal, Pack opening, Clan war):", "Insane Goal")
content_style = st.selectbox("Choose Content Mood/Tone:", ["🔥 High Hype & Shock", "😂 Funny / Meme Style", "👑 Pro-Gamer Challenge"])

st.write("<br>", unsafe_allow_html=True)

# --- ENGINE LOGIC MATH RESTRUCTURE ---
# Pre-coded high-performing TikTok hook elements
hype_hooks = [
    "Stop scrolling! You won't believe how this ended... 🤯⚽",
    "Is this the craziest moment of the week? Watch till the end! ⚡🔥",
    "Rate this out of 10 in the comments right now! 👇😱"
]
meme_hooks = [
    "My script went completely wrong... 😂💀",
    "Tell me why this always happens to me 😭 algorithm explain this!",
    "When you try to look pro but the game says NOPE 💀"
]
challenge_hooks = [
    "No shortcuts. Breaking the global leaderboards tonight! 🏆⚙️",
    "Only 1% of creators can pull off this execution. Challenge starting now! 🧠",
    "Tag a friend who needs to see this elite setup! 🎮👑"
]

tags_pool = ["#gaming", "#trending", "#viral", "#football", "#soccer", "#fyp", "#contentcreator"]

# Generate text matrix based on selected criteria
generated_caption = ""
if content_style == "🔥 High Hype & Shock":
    generated_caption = f"{random.choice(hype_hooks)}\n\nPOV: {video_topic}! This went completely viral on stream. Let me know your thoughts below! 👇\n\n"
elif content_style == "😂 Funny / Meme Style":
    generated_caption = f"{random.choice(meme_hooks)}\n\nContext: {video_topic}. Absolute comedy central 😭 sound on!\n\n"
else:
    generated_caption = f"{random.choice(challenge_hooks)}\n\nObjective accomplished: {video_topic}. The grind continues. ⚡\n\n"

# Append random optimized trending hashtags to clean up block layouts
selected_tags = random.sample(tags_pool, 4)
generated_caption += " ".join(selected_tags)

st.write("<hr>", unsafe_allow_html=True)

# --- LIVE OUTPUT PREVIEW PANEL ---
st.header("📋 Your Optimized Copy-Paste Asset")

st.markdown(f"""
    <div class="caption-box">
        <div class="box-title">📱 Copy this text directly into your TikTok Upload Window:</div>
        <br>
    </div>
""", unsafe_allow_html=True)

# Render inside an input text area field box for simple phone one-tap selection
st.text_area("Your Caption Code Block:", generated_caption, height=150, key="tiktok_final_output_box")

if st.button("✨ Roll Another Version"):
    st.rerun()

# Footnote
st.markdown("<br><hr><p style='text-align: center; color: #4b5563; font-size: 11px;'>⚙️ Unofficial creator utility platform. Optimized for general social text generation metrics.</p>", unsafe_allow_html=True)
