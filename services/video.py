from streamlit.components.v1 import html

def show_beach_stream(beach: str):
    url = f"https://video-auth1.iol.pt/beachcam/{beach}/playlist.m3u8"

    player = f"""
    <style>
      .sb-video-wrapper {{
        aspect-ratio: 16 / 9;
        width: 100%;
        margin-bottom: 1.2rem;
        border-radius: 12px;
        overflow: hidden;
        background-color: #000;
      }}
      .sb-video-wrapper video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
      }}
    </style>

    <div class="sb-video-wrapper">
      <video id="video-{beach}" autoplay muted playsinline loop></video>
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

    # ⬅️ Altezza sufficiente per Streamlit, ma gestita davvero dal CSS
    html(player, height=400)
