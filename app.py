import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import streamlit as st
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="⚽ Futbol Analiz Botu", page_icon="⚽", layout="wide")

st.markdown("<h1 style='text-align: center;'>⚽ Futbol Maçı Analiz Botu</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Yapay Zeka ile Maç Tahminleri</p>", unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.title("⚙️ AYARLAR")
    
    leagues = {
        "Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": ["Manchester United", "Liverpool", "Chelsea", "Arsenal"],
        "La Liga 🇪🇸": ["Real Madrid", "Barcelona", "Atletico Madrid"],
        "Serie A 🇮🇹": ["Juventus", "Inter Milan", "AC Milan"],
        "Bundesliga 🇩🇪": ["Bayern Munich", "Borussia Dortmund", "RB Leipzig"]
    }
    
    selected_league = st.selectbox("Lig Seç:", list(leagues.keys()))
    season = st.slider("Sezon:", 2020, 2025, 2024)

teams = leagues[selected_league]
matches = []
today = datetime.now()

for i in range(12):
    home = np.random.choice(teams)
    away = np.random.choice([t for t in teams if t != home])
    matches.append({
        "id": i,
        "home": home,
        "away": away,
        "date": (today + timedelta(days=i)).strftime("%d.%m.%Y")
    })

st.markdown(f"### 📋 Yaklaşan Maçlar ({selected_league})")
st.success(f"✅ {len(matches)} maç bulundu")

cols = st.columns(3)
for idx, match in enumerate(matches):
    with cols[idx % 3]:
        with st.container(border=True):
            st.markdown(f"📅 **{match['date']}**")
            st.markdown(f"**{match['home']}** vs **{match['away']}**")
            
            if st.button("🎯 Tahmin Yap", key=f"btn_{idx}", use_container_width=True):
                st.session_state[f"pred_{idx}"] = {
                    "home": match["home"],
                    "away": match["away"],
                    "home_goal": np.random.randint(0, 4),
                    "away_goal": np.random.randint(0, 4),
                    "confidence": int(np.random.uniform(75, 99))
                }

st.markdown("---")
st.markdown("### 🎯 Tahmin Sonuçları")

found = False
for key in st.session_state.keys():
    if key.startswith("pred_"):
        found = True
        pred = st.session_state[key]
        
        with st.container(border=True):
            st.markdown(f"**{pred['home']} vs {pred['away']}**")
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("⚽ Skor", f"{pred['home_goal']}-{pred['away_goal']}")
            c2.metric("⚽ Toplam", pred['home_goal'] + pred['away_goal'])
            c3.metric("🎯 İlk Yarı", np.random.randint(0, 3))
            c4.metric("📊 Güven", f"{pred['confidence']}%")

if not found:
    st.info("💡 Bir maç seçerek tahmin yapın")

st.markdown("---")
st.caption("© 2026 Futbol Analiz Botu")

st.set_page_config(page_title="⚽ Futbol Analiz Botu", page_icon="⚽", layout="wide")

st.markdown("<h1 style='text-align: center;'>⚽ Futbol Maçı Analiz Botu</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Yapay Zeka ile Maç Tahminleri</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.title("⚙️ AYARLAR")
    
    leagues = {
        "Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": ["Manchester United", "Liverpool", "Chelsea", "Arsenal", "Manchester City"],
        "La Liga 🇪🇸": ["Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla", "Valencia"],
        "Serie A 🇮🇹": ["Juventus", "Inter Milan", "AC Milan", "Napoli", "Roma"],
        "Bundesliga 🇩🇪": ["Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Leverkusen"]
    }
    
    selected_league = st.selectbox("Lig Seç:", list(leagues.keys()))
    season = st.slider("Sezon:", 2020, 2025, 2024)

# Generate mock matches
teams = leagues[selected_league]
matches = []
today = datetime.now()

for i in range(12):
    home = np.random.choice(teams)
    away = np.random.choice([t for t in teams if t != home])
    matches.append({
        "id": i,
        "home": home,
        "away": away,
        "date": (today + timedelta(days=i)).strftime("%d.%m.%Y %H:%M")
    })

st.markdown(f"### 📋 Yaklaşan Maçlar ({selected_league})")
st.info(f"✅ {len(matches)} maç bulundu")

# Display matches in grid
cols = st.columns(3)
for idx, match in enumerate(matches):
    with cols[idx % 3]:
        with st.container(border=True):
            st.markdown(f"**{match['date']}**")
            st.markdown(f"{match['home']} **vs** {match['away']}")
            
            if st.button("🎯 Tahmin Yap", key=f"btn_{idx}", use_container_width=True):
                st.session_state[f"pred_{idx}"] = {
                    "home": match["home"],
                    "away": match["away"],
                    "home_goal": np.random.randint(0, 4),
                    "away_goal": np.random.randint(0, 4),
                    "confidence": np.random.uniform(0.75, 0.99)
                }

# Show predictions
st.markdown("---")
st.markdown("### 🎯 Tahmin Sonuçları")

found = False
for key in st.session_state.keys():
    if key.startswith("pred_"):
        found = True
        pred = st.session_state[key]
        
        with st.container(border=True):
            st.markdown(f"**{pred['home']} vs {pred['away']}**")
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Skor", f"{pred['home_goal']}-{pred['away_goal']}")
            c2.metric("Toplam Gol", pred['home_goal'] + pred['away_goal'])
            c3.metric("İlk Yarı", np.random.randint(0, pred['home_goal'] + pred['away_goal'] + 1))
            c4.metric("Güven", f"{int(pred['confidence']*100)}%")

if not found:
    st.info("💡 Bir maç seçerek tahmin yapın")

st.markdown("---")
st.caption("© 2026 Futbol Analiz Botu | Test Modu")
