# tutte le chiamate a IPMA + cache

import requests, json
from datetime import datetime, timedelta
import streamlit as st

BASE = "https://api.ipma.pt/open-data"

@st.cache_data(ttl=1800)            # 30 min cache
def get_webcams():
    with open("data/webcams.json") as f:
        return json.load(f)

@st.cache_data(ttl=900)             # 15 min cache
def get_surface_obs():
    url = f"{BASE}/observation/meteorology/stations/obs-surface.geojson"
    return requests.get(url, timeout=10).json()

def latest_wind(id_estacao):
    data = get_surface_obs()
    last, ts = None, None
    for f in data["features"]:
        if f["properties"]["idEstacao"] == id_estacao:
            t = datetime.fromisoformat(f["properties"]["time"])
            if not ts or t > ts:
                last, ts = f["properties"], t
    if last and last["intensidadeVento"] >= 0 and ts >= datetime.now() - timedelta(hours=5):
        return {
            "time": ts.strftime("%H:%M"),
            "knots": round(last["intensidadeVento"] * 1.94384449, 1),
            "dir": last["descDirVento"],
        }
    return None

@st.cache_data(ttl=43200)           # 12 h cache
def swell_today():
    url = f"{BASE}/forecast/oceanography/daily/hp-daily-sea-forecast-day0.json"
    data = requests.get(url, timeout=10).json()["data"]
    lisboa = next(i for i in data if i["globalIdLocal"] == 1111026)
    return lisboa
