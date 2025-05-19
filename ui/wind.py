import streamlit as st
from config.constants import wind_station
from services.ipma_api import latest_wind

def render():
    st.markdown("#### 💨 Last wind observations:")
    rows = []
    for label, est in wind_station.items():
        obs = latest_wind(est)
        short = label.split(" - ")[-1]
        if obs:
            rows.append(f"- **{short}** ({obs['time']}): **{obs['knots']} kt** from **{obs['dir']}**")
    st.markdown("\n".join(rows))
