import streamlit as st
import json
from streamlit.components.v1 import html

# --- Carica le zone da JSON ---
with open("webcams.json", "r") as f:
    zones = json.load(f)

# --- Funzione per mostrare il video ---
def show_beach_stream(beach: str):
    url = f"https://video-auth1.iol.pt/beachcam/{beach}/playlist.m3u8"

    player = f"""
    <style>
      .video-container {{
        position: relative;
        width: 100%;
        padding-bottom: 56.25%;
        height: 0;
        margin-bottom: 30px;
      }}
      .video-container video {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }}
    </style>

    <div class="video-container">
      <video id="video-{beach}" controls autoplay muted></video>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    <script>
      const video = document.getElementById("video-{beach}");
      if (Hls.isSupported()) {{
        const hls = new Hls();
        hls.loadSource("{url}");
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED, function () {{
          hls.currentLevel = hls.levels.length - 1;
        }});
      }} else if (video.canPlayType('application/vnd.apple.mpegurl')) {{
        video.src = "{url}";
      }}
    </script>
    """
    html(player, height=400)

# --- UI: Selezione zona ---
st.title("🌍 Paolino's Cams")

zone_names = list(zones.keys())
selected_zone = st.selectbox("Select a surf area", zone_names)

st.header(f"📍 Webcams in the area: {selected_zone}")

for beach in zones[selected_zone]:
    st.subheader(beach.replace("-", " ").title())
    show_beach_stream(beach)
