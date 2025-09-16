import streamlit as st
from services.ipma_api import swell_today
import streamlit.components.v1 as components
from config.constants import WINDFINDER_SLUG

def render(zone_label: str | None = None):
    s = swell_today()
    st.markdown(
        f"#### 🌊 Swell forecast for today\n"
        f"Today swell in **Lisbon** area is forcasted of about **{s['waveHighMin']}**–**{s['waveHighMax']} meters** at "
        f"**{s['wavePeriodMin']}**–**{s['wavePeriodMax']} seconds** "
        f"from **{s['predWaveDir']}**"
    )

    # --- Accordion con Super Forecast Windfinder, basato sulla zona selezionata ---
    slug = WINDFINDER_SLUG.get(zone_label or "", "parede_murtal")  # default di sicurezza
    with st.expander("📈 Super Forecast (Windfinder)", expanded=False):
        components.html(
            f"""
            <div id="wf-super-forecast">
              <script src="https://www.windfinder.com/widget/forecast/js/{slug}?unit_wave=m&unit_rain=mm&unit_temperature=c&unit_wind=kts&unit_pressure=hPa&days=3&show_day=0"></script>
              <noscript>
                <a rel="nofollow" href="https://www.windfinder.com/forecast/{slug}?utm_source=forecast&utm_medium=web&utm_campaign=homepageweather&utm_content=noscript-forecast">
                  Wind forecast
                </a> provided by
                <a rel="nofollow" href="https://www.windfinder.com?utm_source=forecast&utm_medium=web&utm_campaign=homepageweather&utm_content=noscript-logo">
                  windfinder.com
                </a>
              </noscript>
            </div>
            """,
            height=540,
            scrolling=True,
        )
