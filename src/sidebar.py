import streamlit as st



def angemeldet_als():
    name = st.session_state.get('name')
    st.sidebar.success(f"Angemeldet als: {name}")

def navigation():
    auswahl_optionen = st.sidebar.radio("Navigation", ["Start", "Kommunikation", "Rezeptideen", "Dateideen"])
    st.session_state["active_page"] = auswahl_optionen