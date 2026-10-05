import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="DLS 26 Secret Scout", page_icon="🔍", layout="centered")

# Premium Cyber-Dark Scout Styling
st.markdown("""
    <style>
    .main { background-color: #060913; color: #ffffff; }
    h1 { text-align: center; font-family: 'Arial Black', sans-serif; color: #00ffcc; font-size: 32px; text-shadow: 0 0 15px rgba(0,255,204,0.3); }
    .scout-card {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        border-left: 5px solid #00ffcc;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .guide-card {
        background: linear-gradient(145deg, #1e1b4b, #311042);
        border: 1px solid #818cf8;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
    }
    .player-name { font-size: 20px; font-weight: 800; color: #ffffff; }
    .player-meta { font-size: 14px; color: #38bdf8; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 DLS 26 SECRET GEMS SCOUT")
st.markdown("<p style='text-align:center; color:#94a3b8;'>Find hidden beast players, official prices, and simulate max upgrades instantly!</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- DLS 26 PLAYER DATABASE (Includes Ultra-Cheap Starters) ---
dls_database = [
    {"name": "Kylian Mbappé", "pos": "CF", "rating": 86, "max": 96, "price": 2650, "tier": "Legendary Gold", "gem": "No", "desc": "Highest base speed in the entire DLS 26 database."},
    {"name": "Lamine Yamal", "pos": "RW", "rating": 81, "max": 91, "price": 1820, "tier": "Legendary Gold", "gem": "Yes", "desc": "Hidden Gem! Upgrades incredibly fast in stamina and ball control."},
    {"name": "Erling Haaland", "pos": "CF", "rating": 86, "max": 96, "price": 2650, "tier": "Legendary Gold", "gem": "No", "desc": "Maximum physical strength block. Unstoppable in corner kicks."},
    {"name": "Nico Williams", "pos": "LW", "rating": 79, "max": 89, "price": 1450, "tier": "Rare Blue", "gem": "Yes", "desc": "Secret Beast! Costs half the price of gold wingers but reaches 95+ speed easily."},
    {"name": "Amad Diallo", "pos": "RM", "rating": 74, "max": 85, "price": 950, "tier": "Common Grey", "gem": "Ultimate Budget Gem", "desc": "Insane acceleration breakdown for a cheap grey tier player."},
    {"name": "Ernest Nuamah", "pos": "RW", "rating": 71, "max": 83, "price": 680, "tier": "Common Grey", "gem": "Bargain Starter", "desc": "Ultra-cheap option! Amazing pace parameters for players building their very first squad."},
    {"name": "Fatawu Issahaku", "pos": "RW", "rating": 69, "max": 81, "price": 450, "tier": "Common Grey", "gem": "Bargain Starter", "desc": "Lowest cost speed merchant. Perfect starting winger for low coin balances."}
]

# --- MODE SELECTOR ---
mode = st.radio("⚡ Select Scout Feature Mode:", ["🔍 Search Player Database", "💰 Coin Budget Optimizer"])
st.write("<hr>", unsafe_allow_html=True)

# --- FEATURE 1: SEARCH DATABASE ---
if mode == "🔍 Search Player Database":
    search_query = st.text_input("Type player name to scout:", "").strip().lower()
    filter_gem = st.checkbox("Show Hidden Budget Gems Only")
    
    st.write("<br>", unsafe_allow_html=True)
    
    for player in dls_database:
        if search_query and search_query not in player["name"].lower():
            continue
        if filter_gem and "Yes" not in player["gem"] and "Ultimate" not in player["gem"] and "Bargain" not in player["gem"]:
            continue
            
        st.markdown(f"""
            <div class="scout-card">
                <div class="player-name">{player['name']}</div>
                <div class="player-meta">Position: {player['pos']} | Tier: {player['tier']}</div>
                <p style='margin-top:8px; margin-bottom:8px; color:#cbd5e1; font-size:14px;'>{player['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Base OVR", f"{player['rating']}")
        col2.metric("Maxed Rating", f"{player['max']} ⚡")
        col3.metric("Game Cost", f"{player['price']} Coins")
        st.write("<br>", unsafe_allow_html=True)

# --- FEATURE 2: BUDGET OPTIMIZER (With Safe Guide Fallback) ---
else:
    st.header("🪙 Smart Transfer Budget Calculator")
    st.write("Input your current coin balance to see the best options for your squad.")
    
    user_coins = st.number_input("Enter your DLS Coins:", min_value=0, max_value=50000, value=500, step=50)
    
    st.write("<br><h3>📋 Scout Evaluation Results:</h3>", unsafe_allow_html=True)
    
    found_any = False
    for player in dls_database:
        if user_coins >= player["price"]:
            found_any = True
            is_gem_badge = "🔥 [BUDGET TARGET]" if "Yes" in player["gem"] or "Bargain" in player["gem"] else ""
            st.markdown(f"""
                <div class="scout-card">
                    <div class="player-name">{player['name']} {is_gem_badge}</div>
                    <div class="player-meta">Position: {player['pos']} | Price: {player['price']} Coins</div>
                    <p style='color:#94a3b8; font-size:13px; margin-top:5px;'>Guaranteed Potential: <b>{player['max']} OVR</b></p>
                </div>
            """, unsafe_allow_html=True)
            
    # If the user enters a balance that is too small for premium cards
    if user_coins < 450:
        st.error("⚠️ Your coin balance is too low to purchase established players right now.")
        st.markdown("""
            <div class="guide-card">
                <h3 style='margin-top:0; color:#818cf8;'>📈 EMERGENCE COIN GRIND GUIDE</h3>
                <p style='color:#cbd5e1; font-size:14px;'>Don't worry, Beckham! Follow these fast in-game steps to unlock your first 1,000 coins in less than an hour:</p>
                <ul style='color:#cbd5e1; font-size:14px; padding-left:20px;'>
                    <li style='margin-bottom:8px;'><b>Stadium Bonus Loop:</b> Invest your initial free gems only into upgrading your Stadium Capacity. This multiplies your home game coin earnings automatically!</li>
                    <li style='margin-bottom:8px;'><b>The Live Challenge Check:</b> Navigate to DLS Live daily. Complete the entry tier event tasks to unlock instant 300+ coin rewards.</li>
                    <li style='margin-bottom:8px;'><b>Post-Match Ad Strategy:</b> Always clear the optional ad video prompt after tournament matches to double your win bonuses from 40 coins to 80 coins.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# Legal Footer
st.markdown("<br><hr><p style='text-align: center; color: #4b5563; font-size: 11px;'>🛑 LEGAL DISCLAIMER: Unofficial fan utility. Stat values are simulations for community evaluation. Not affiliated with First Touch Games.</p>", unsafe_allow_html=True)
