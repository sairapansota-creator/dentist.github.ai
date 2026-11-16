import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Dentist Outreach Tracker", layout="wide")

html = Path(__file__).parent.joinpath("tracker.html").read_text(encoding="utf-8")
components.html(html, height=1600, scrolling=True)
