import streamlit_authenticator as stauth
import streamlit as st

def get_authenticator():
    # Daten aus secrets.toml laden
    names = st.secrets["users"]["names"]
    usernames = st.secrets["users"]["usernames"]
    passwords = st.secrets["users"]["passwords"]

    # Passwörter hashen
    
    hashed_passwords = stauth.Hasher.hash_passwords(passwords)

    # Credentials-Dictionary
    credentials = {
        "usernames": {
            uname: {
                "name": name,
                "password": pw
            }
            for uname, name, pw in zip(usernames, names, hashed_passwords)
        }
    }

    # Authenticator erstellen
    authenticator = stauth.Authenticate(
        credentials,
        'meine_app_cookie',
        'geheimer_schluessel',
        cookie_expiry_days=30
    )

    return authenticator
