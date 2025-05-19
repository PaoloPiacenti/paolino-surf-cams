import streamlit as st
import base64
from services.ipma_api import get_webcams
from services.video import show_beach_stream
from ui.swell import render as swell_block
from ui.wind import render as wind_block

st.set_page_config(page_title="SurfBuddy Lisboa", page_icon="🏄‍♂️", layout="centered")

# --- UTILITY ---
def load_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

banner_b64 = load_base64("assets/hero.jpg")
profile_b64 = load_base64("assets/logo.png")

# --- STILE ---
st.markdown(f"""
<style>
.banner-wrapper {{
    position: relative;
    max-width: 1000px;
    margin: 0 auto 4rem auto;
    padding: 0 1rem;
    text-align: center;
}}

.banner-img {{
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 18px;
}}

.profile-img {{
    position: absolute;
    bottom: -50px;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 4px solid white;
    background: white;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
}}

@media (max-width: 600px) {{
    .profile-img {{
        width: 72px;
        height: 72px;
        bottom: -36px;
    }}
}}
</style>

<div class="banner-wrapper">
  <img src="data:image/jpeg;base64,{banner_b64}" class="banner-img">
  <img src="data:image/png;base64,{profile_b64}" class="profile-img">
</div>
""", unsafe_allow_html=True)

# --- CONTENUTO ---
st.markdown('<div class="block">', unsafe_allow_html=True)

st.markdown("""
Hey **Meo Beachcam**, just a thought:
maybe let people free to **skip the ad after 5 seconds**?

Being forced to watch the **same irrelevant ad** again and again
feels like a scene from *A Clockwork Orange* —
except the torture is... *buffered*.

---

For our close friends only,
we're streaming Lisbon's surf cams **ad-free** — just clean swell and stoke 🌊
""")


swell_block()
wind_block()

st.markdown("#### 🎥 Watch webcams in:")
zones = get_webcams()
zone = st.selectbox("Select a surf area", list(zones))


for beach in zones[zone]:
    with st.container():
        st.markdown(f"<h4 style='margin-bottom:0.5rem'>{beach.replace('-', ' ').title()}</h4>", unsafe_allow_html=True)
        show_beach_stream(beach)
