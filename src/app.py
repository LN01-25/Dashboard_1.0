import streamlit as st
from authentification import get_authenticator
import sidebar
from featers import rezepte
from featers import dateideen

st.set_page_config(page_title="Dashboard", layout="wide")

# Authenticator holen
authenticator = get_authenticator()

# Login anzeigen
authenticator.login('main')

# Zugriff über Session State

authentication_status = st.session_state.get('authentication_status')
username = st.session_state.get('username')

# Login-Status prüfen
if authentication_status:


    st.title("Hättest du das gedacht.... crazy oder??")
    st.subheader("Dicken Kuss... viel Spaß morgen auf der Arbeit")
    sidebar.angemeldet_als()
    sidebar.navigation()
    if st.session_state.get("active_page") == "Rezeptideen":
        rezepte.rezept1()
    if st.session_state.get("active_page") == "Dateideen":
        dateideen.dateidee()




elif authentication_status == False:
    st.error("Benutzername oder Passwort falsch")
elif authentication_status == None:
    st.warning("Bitte anmelden, um Zugriff zu erhalten.")
