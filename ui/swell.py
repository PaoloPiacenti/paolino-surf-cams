import streamlit as st
from services.ipma_api import swell_today

def render():
    s = swell_today()
    st.markdown(
        f"#### 🌊 Swell forecast for today\n"
        f"Today swell in **Lisbon** area is forcasted of about **{s['waveHighMin']}**–**{s['waveHighMax']} meters** at "
        f"**{s['wavePeriodMin']}**–**{s['wavePeriodMax']} seconds** "
        f"from **{s['predWaveDir']}**"
    )
