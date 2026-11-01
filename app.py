import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Page Configuration
st.set_page_config(
    page_title="ZactheGamer | Official Games & Updates Hub",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Professional Dark Gaming Theme CSS
st.markdown("""
<style>
    /* Main Background & Typography */
    .stApp {
        background-color: #0b0e14;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 50%, #0f172a 100%);
        padding: 40px 30px;
        border-radius: 16px;
        border: 1px solid rgba(139, 92, 246, 0.3);
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px -10px rgba(124, 58, 237, 0.5);
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 10px;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #cbd5e1;
        max-width: 700px;
        margin: 0 auto;
    }
    
    /* Game Card Styling */
    .game-card {
        background-color: #131825;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .game-card:hover {
        transform: translateY(-4px);
        border-color: #8b5cf6;
        box-shadow: 0 10px 25px -5px rgba(139, 92, 246, 0.2);
    }
    
    /* Badges */
    .badge-update {
        background-color: rgba(16, 185, 129, 0.15);
        color: #34d399;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .badge-genre {
        background-color: rgba(59, 130, 246, 0.15);
        color: #60a5fa;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }
    
    /* Metrics and Stats */
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #a78bfa;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        transition: opacity 0.2s ease;
    }
    .stButton button:hover {
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State for Games Dataset & Downloads
if "games_db" not in st.session_state:
    # 50 Famous Games Initial Dataset with realistic update details & download links
    famous_games = [
        ("Grand Theft Auto V", "Action / Open World", "v1.68 Online Tuners", "98 GB", "2026-02-15", "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/", "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=600&q=80"),
        ("Minecraft", "Sandbox / Survival", "v1.20.5 Armored Paws", "1.2 GB", "2026-01-20", "https://www.minecraft.net/", "https://images.unsplash.com/photo-1627856013091-fed6e4e30abe?auto=format&fit=crop&w=600&q=80"),
        ("Cyberpunk 2077", "Action RPG", "v2.12 Patch & Phantom Liberty", "70 GB", "2026-02-10", "https://store.steampowered.com/app/1091500/Cyberpunk_2077/", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=600&q=80"),
        ("Counter-Strike 2", "Tactical Shooter", "v1.39.7.5 Arsenal Update", "33 GB", "2026-02-28", "https://store.steampowered.com/app/730/CounterStrike_2/", "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=600&q=80"),
        ("Elden Ring", "Action RPG / Souls-like", "v1.12 Shadow of the Erdtree Prep", "60 GB", "2026-01-15", "https://store.steampowered.com/app/1245620/ELDEN_RING/", "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?auto=format&fit=crop&w=600&q=80"),
        ("Fortnite", "Battle Royale", "Chapter 5 Season 2 Myths & Mortals", "45 GB", "2026-03-01", "https://www.fortnite.com/", "https://images.unsplash.com/photo-1589241062272-c0a000071dfa?auto=format&fit=crop&w=600&q=80"),
        ("Baldur's Gate 3", "Turn-based RPG", "Patch 6 Hotfix 25", "150 GB", "2026-02-05", "https://store.steampowered.com/app/1086940/Baldurs_Gate_3/", "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=600&q=80"),
        ("Valorant", "Tactical Hero Shooter", "Episode 8 Act II Update", "28 GB", "2026-02-22", "https://playvalorant.com/", "https://images.unsplash.com/photo-1542751110-97427bbecf20?auto=format&fit=crop&w=600&q=80"),
        ("Apex Legends", "Battle Royale", "Breakthrough Season Update", "75 GB", "2026-02-18", "https://www.ea.com/games/apex-legends", "https://images.unsplash.com/photo-1560253023-3ec5d502959f?auto=format&fit=crop&w=600&q=80"),
        ("Call of Duty: Warzone", "First-Person Shooter", "Season 2 Reloaded", "125 GB", "2026-02-25", "https://www.callofduty.com/warzone", "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=600&q=80"),
        ("The Witcher 3: Wild Hunt", "Action RPG", "v4.04 Next-Gen Hotfix", "50 GB", "2025-12-10", "https://store.steampowered.com/app/292030/The_Witcher_3_Wild_Hunt/", "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=600&q=80"),
        ("Red Dead Redemption 2", "Action / Adventure", "v1.32 Stability & DLSS 3 Support", "116 GB", "2025-11-15", "https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/", "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80"),
        ("League of Legends", "MOBA", "Patch 14.4 Balance Update", "22 GB", "2026-02-21", "https://www.leagueoflegends.com/", "https://images.unsplash.com/photo-1542751110-97427bbecf20?auto=format&fit=crop&w=600&q=80"),
        ("Dota 2", "MOBA", "Crownfall Event & Gameplay Patch 7.35d", "65 GB", "2026-02-19", "https://store.steampowered.com/app/570/Dota_2/", "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=600&q=80"),
        ("Genshin Impact", "Action RPG", "v4.5 'Blades Weaving Devotion'", "85 GB", "2026-02-27", "https://genshin.hoyoverse.com/", "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?auto=format&fit=crop&w=600&q=80"),
        ("Hollow Knight", "Metroidvania", "v1.5.8 Complete Edition", "9 GB", "2025-10-05", "https://store.steampowered.com/app/367520/Hollow_Knight/", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=600&q=80"),
        ("Terraria", "Sandbox / Adventure", "v1.4.4.9 Labor of Love", "500 MB", "2025-11-30", "https://store.steampowered.com/app/105600/Terraria/", "https://images.unsplash.com/photo-1627856013091-fed6e4e30abe?auto=format&fit=crop&w=600&q=80"),
        ("Stardew Valley", "Simulation / RPG", "v1.6 Major Content Update", "600 MB", "2026-03-02", "https://store.steampowered.com/app/413150/Stardew_Valley/", "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80"),
        ("Palworld", "Survival / Crafting", "v0.1.5.0 Bug Fixes & Optimization", "40 GB", "2026-02-12", "https://store.steampowered.com/app/1623730/Palworld/", "https://images.unsplash.com/photo-1589241062272-c0a000071dfa?auto=format&fit=crop&w=600&q=80"),
        ("Helldivers 2", "Co-op Shooter", "v01.000.200 Balance & Armor Fixes", "70 GB", "2026-02-26", "https://store.steampowered.com/app/553850/HELLDIVERS_2/", "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=600&q=80"),
    ]
    
    # Pad up to 50 famous games with procedural professional template data
    additional_titles = [
        ("Monster Hunter World", "Action RPG"), ("Forza Horizon 5", "Racing"), ("God of War Ragnarok", "Action / Adventure"),
        ("Spider-Man Remastered", "Action"), ("Horizon Zero Dawn", "Action RPG"), ("Death Stranding", "Action"),
        ("Resident Evil 4 Remake", "Survival Horror"), ("Dead Space Remake", "Survival Horror"), ("Among Us", "Party / Deduction"),
        ("Fall Guys", "Platform / Battle Royale"), ("Rocket League", "Sports / Racing"), ("Phasmophobia", "Co-op Horror"),
        ("Assetto Corsa Competizione", "Simulation"), ("Microsoft Flight Simulator", "Simulation"), ("Cities: Skylines II", "Simulation"),
        ("Civilization VI", "Strategy"), ("Total War: Warhammer III", "Strategy"), ("Age of Empires IV", "Strategy"),
        ("Subnautica", "Survival"), ("The Forest", "Survival"), ("Sons of the Forest", "Survival"),
        ("Hades II", "Roguelike"), ("Dead Cells", "Roguelike"), ("Risk of Rain 2", "Roguelike"),
        ("Sekiro: Shadows Die Twice", "Action / Souls-like"), ("Dark Souls III", "Action RPG"), ("Monster Hunter Rise", "Action RPG"),
        ("Remnant 2", "Action Shooter"), ("Borderlands 3", "Looter Shooter"), ("Destiny 2", "MMO Shooter")
    ]
    
    for idx, (title, genre) in enumerate(additional_titles, start=21):
        famous_games.append((
            title,
            genre,
            f"v1.{idx} Performance & Content Patch",
            f"{random.randint(15, 80)} GB",
            f"2026-01-{random.randint(10, 28):02d}",
            "https://store.steampowered.com/",
            "https://images.unsplash.com/photo-1542751110-97427bbecf20?auto=format&fit=crop&w=600&q=80"
        ))

    st.session_state.games_db = [
        {
            "id": i+1,
            "title": g[0],
            "genre": g[1],
            "version": g[2],
            "size": g[3],
            "date": g[4],
            "link": g[5],
            "image": g[6],
            "description": f"Official verified update package for {g[0]}. Fully tested and safe developer release hosted on ZactheGamer secure CDN servers.",
            "downloads_count": random.randint(1200, 45000)
        }
        for i, g in enumerate(famous_games)
    ]

if "download_history" not in st.session_state:
    st.session_state.download_history = []

if "uploaded_games" not in st.session_state:
    st.session_state.uploaded_games = []

# Sidebar Navigation & Branding
st.sidebar.markdown("# 🎮 ZactheGamer")
st.sidebar.markdown("---")
nav_choice = st.sidebar.radio("Navigation Menu", ["Home & Game Updates", "Browse All 50+ Games", "Search Games", "Developer Upload Portal", "My Downloads & Activity"])

st.sidebar.markdown("---")
st.sidebar.info("⚡ **ZactheGamer Hub v3.5**\nLive tracking active for top 50 global titles. Secure direct server nodes ready.")

# --- PAGE 1: HOME & GAME UPDATES ---
if nav_choice == "Home & Game Updates":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">ZactheGamer Game Hub</div>
        <div class="hero-subtitle">Your premier destination for verified game updates, patch notes, high-speed downloads, and community developer releases.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Tracked Top Games", "50+", "Live")
    with col2:
        st.metric("Total Platform Downloads", "1.4M+", "+12% this week")
    with col3:
        st.metric("Server Status", "Operational", "10Gbps Link")
    with col4:
        st.metric("Verified Safe Rate", "100%", "Anti-Cheat Clean")
        
    st.markdown("### 🔥 Latest Trending Updates (Top 50 Spotlight)")
    
    # Display top 6 trending games
    trending_games = st.session_state.games_db[:6]
    c1, c2, c3 = st.columns(3)
    cols = [c1, c2, c3]
    
    for idx, game in enumerate(trending_games):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="game-card">
                <img src="{game['image']}" style="width:100%; height:150px; object-fit:cover; border-radius:8px; margin-bottom:12px;">
                <span class="badge-genre">{game['genre']}</span>
                <span class="badge-update">{game['version']}</span>
                <h4 style="margin-top:10px; margin-bottom:5px; color:#ffffff;">{game['title']}</h4>
                <p style="font-size:0.85rem; color:#94a3b8; margin-bottom:10px;">Size: {game['size']} | Updated: {game['date']}</p>
                <p style="font-size:0.9rem; color:#cbd5e1;">{game['description'][:90]}...</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"📥 Download / Update", key=f"home_dl_{game['id']}"):
                st.session_state.selected_download = game
                st.rerun()

# --- PAGE 2: BROWSE ALL 50+ GAMES ---
elif nav_choice == "Browse All 50+ Games":
    st.markdown("## 📚 Complete Catalog: 50 Famous Games & Updates")
    st.markdown("Explore the complete database of 50 top-tier games tracked in real-time by ZactheGamer.")
    
    # Genre filter
    genres = ["All"] + sorted(list(set(g["genre"] for g in st.session_state.games_db)))
    selected_genre = st.selectbox("Filter by Genre", genres)
    
    filtered_list = st.session_state.games_db if selected_genre == "All" else [g for g in st.session_state.games_db if g["genre"] == selected_genre]
    
    st.markdown(f"Showing **{len(filtered_list)}** games in catalog.")
    
    # Display in a clean interactive data table with download buttons
    for game in filtered_list:
        with st.container():
            col_img, col_info, col_action = st.columns([1, 3, 1])
            with col_img:
                st.image(game['image'], width=120)
            with col_info:
                st.markdown(f"### {game['title']}")
                st.markdown(f"<span class='badge-genre'>{game['genre']}</span> &nbsp; <span class='badge-update'>{game['version']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Size:** {game['size']} &nbsp;|&nbsp; **Last Patch Date:** {game['date']} &nbsp;|&nbsp; **Downloads:** {game['downloads_count']:,}")
                st.write(game['description'])
            with col_action:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Get Update", key=f"browse_dl_{game['id']}"):
                    st.session_state.selected_download = game
                    st.rerun()
            st.markdown("---")

# --- PAGE 3: SEARCH GAMES ---
elif nav_choice == "Search Games":
    st.markdown("## 🔍 Advanced Game Search & Instant Data Lookup")
    st.markdown("Search instantly across all 50 famous titles, developer releases, patches, and version numbers.")
    
    search_query = st.text_input("Enter game name, keyword, or genre:", placeholder="e.g., GTA, Minecraft, RPG, Shooter...")
    
    if search_query:
        query_lower = search_query.lower()
        results = [g for g in st.session_state.games_db if query_lower in g['title'].lower() or query_lower in g['genre'].lower() or query_lower in g['version'].lower()]
        
        # Also search user-uploaded games
        user_results = [g for g in st.session_state.uploaded_games if query_lower in g['title'].lower() or query_lower in g['genre'].lower()]
        
        total_found = len(results) + len(user_results)
        st.success(f"Found {total_found} matching game(s) for '{search_query}'")
        
        for game in results + user_results:
            st.markdown(f"""
            <div class="game-card">
                <h3>{game['title']} <span style="font-size:0.8rem; color:#a78bfa;">({game['version']})</span></h3>
                <p><b>Genre:</b> {game['genre']} | <b>Size:</b> {game['size']} | <b>Date:</b> {game['date']}</p>
                <p>{game['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("📥 Download Setup / Update", key=f"search_dl_{game['title']}"):
                st.session_state.selected_download = game
                st.rerun()
    else:
        st.info("💡 Type any game title or genre above to query our live database instantly.")

# --- PAGE 4: DEVELOPER UPLOAD PORTAL ---
elif nav_choice == "Developer Upload Portal":
    st.markdown("## ☁️ ZactheGamer Developer Upload Portal")
    st.markdown("Upload custom game builds, indie titles, or patch modifications directly to the ZactheGamer repository.")
    
    with st.form("developer_upload_form"):
        col1, col2 = st.columns(2)
        with col1:
            game_title = st.text_input("Game / Project Title")
            game_genre = st.selectbox("Category / Genre", ["Action", "Adventure", "RPG", "Simulation", "Strategy", "Indie", "Sandbox", "Sports"])
            game_version = st.text_input("Version / Build Number", value="v1.0.0")
        with col2:
            file_size = st.text_input("Package Size (e.g., 1.5 GB)")
            dev_name = st.text_input("Developer / Studio Name")
            contact_email = st.text_input("Contact Email")
            
        game_desc = st.text_area("Game Description & Patch Notes")
        submit_upload = st.form_submit_button("🚀 Publish Game to ZactheGamer CDN")
        
        if submit_upload:
            if game_title and dev_name and game_desc:
                new_game_entry = {
                    "id": len(st.session_state.games_db) + len(st.session_state.uploaded_games) + 1,
                    "title": f"{game_title} (By {dev_name})",
                    "genre": game_genre,
                    "version": game_version,
                    "size": file_size or "500 MB",
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "link": "#",
                    "image": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=600&q=80",
                    "description": game_desc,
                    "downloads_count": 1
                }
                st.session_state.uploaded_games.append(new_game_entry)
                st.success(f"Success! '{game_title}' has been verified and published to the ZactheGamer directory.")
            else:
                st.error("Please fill in all required fields before submitting.")

# --- PAGE 5: MY DOWNLOADS & ACTIVITY ---
elif nav_choice == "My Downloads & Activity":
    st.markdown("## 📥 My Downloads & Installation Queue")
    st.markdown("Manage your active download session, review receipt records, and launch installers.")
    
    if "selected_download" in st.session_state and st.session_state.selected_download:
        g = st.session_state.selected_download
        st.markdown(f"""
        <div style="background-color:#131825; padding:25px; border-radius:12px; border:1px solid #7c3aed; margin-bottom:25px;">
            <h3>🎮 Selected for Download: {g['title']}</h3>
            <p><b>Version:</b> {g['version']} &nbsp;|&nbsp; <b>Size:</b> {g['size']} &nbsp;|&nbsp; <b>Genre:</b> {g['genre']}</p>
            <p>{g['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("⚡ Start High-Speed Download Simulation"):
                receipt = {
                    "title": g['title'],
                    "version": g['version'],
                    "size": g['size'],
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "status": "Completed Secure Download",
                    "reference_id": f"ZGT-{random.randint(100000, 999999)}"
                }
                st.session_state.download_history.append(receipt)
                st.success(f"Download completed successfully for {g['title']}! Verification hash passed.")
        with col_btn2:
            if st.button("❌ Clear Selection"):
                del st.session_state.selected_download
                st.rerun()
                
    st.markdown("---")
    st.markdown("### 📜 Download History & Receipts")
    if st.session_state.download_history:
        history_df = pd.DataFrame(st.session_state.download_history)
        st.dataframe(history_df, use_container_width=True)
        
        # Download receipt as CSV option
        csv_data = history_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Activity Receipt (CSV)",
            data=csv_data,
            file_name="zacthegamer_download_receipts.csv",
            mime="text/csv"
        )
    else:
        st.info("No downloads recorded in current session. Select any game from Home or Catalog to initiate a download.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 0.85rem;'>"
    "© 2026 ZactheGamer Hub. All rights reserved. Real-time game tracking & developer updates platform.<br>"
    "Powered by Streamlit & Python."
    "</p>",
    unsafe_allow_html=True
)