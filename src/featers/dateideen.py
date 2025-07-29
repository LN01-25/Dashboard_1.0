import streamlit as st
import random
import sqlite3

# Funktion zum Speichern in SQLite
def speichere_idee_db(idee):
    conn = sqlite3.connect("ideen.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS date_ideen (id INTEGER PRIMARY KEY AUTOINCREMENT, idee TEXT)")
    cursor.execute("INSERT INTO date_ideen (idee) VALUES (?)", (idee,))
    conn.commit()
    conn.close()

# Funktion zum Laden aus SQLite
def lade_ideen_db():
    conn = sqlite3.connect("ideen.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS date_ideen (id INTEGER PRIMARY KEY AUTOINCREMENT, idee TEXT)")
    cursor.execute("SELECT idee FROM date_ideen")
    daten = cursor.fetchall()
    conn.close()
    return [d[0] for d in daten]

# Funktion zum Löschen der Datenbank
def loesche_alle_ideen_db():
    conn = sqlite3.connect("ideen.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM date_ideen")
    conn.commit()
    conn.close()
# Funktion zum Löschen einer Idee
def loesche_idee_db(idee):
    conn = sqlite3.connect("ideen.db")
    curosr = conn.cursor()
    curosr.execute("DELETE FROM date_ideen WHERE idee = ?", (idee,))
    conn.commit()
    conn.close()


# Hauptfunktion
def dateidee():
    if "date_idee_liste" not in st.session_state:
        st.session_state.date_idee_liste = lade_ideen_db()
    if "eingabe_idee" not in st.session_state:
        st.session_state.eingabe_idee = ""
    if "zufalls_idee" not in st.session_state:
        st.session_state.zufalls_idee = None

    def add_idee():
        idee = st.session_state.eingabe_idee.strip()
        if idee != "" and idee not in st.session_state.date_idee_liste:
            st.session_state.date_idee_liste.append(idee)
            speichere_idee_db(idee)
        st.session_state.eingabe_idee = ""

    # Eingabe
    st.text_input("Gib eine Date-Idee ein und drücke Enter:", key="eingabe_idee", on_change=add_idee, placeholder="sei kreativ")


    spalte1, spalte2, spalte3 = st.columns(3)

    with spalte1:
        st.header("💡 Date Ideen")
        if st.session_state.date_idee_liste:
            st.subheader("📝 Unsere Ideen:")
            for i, idee in enumerate(st.session_state.date_idee_liste, 1):
                st.write(f"{i}. {idee}")
        else:
            st.info("Noch keine Ideen eingetragen.")

    with spalte2:
        st.header("Buttons")
        if st.button("Liste löschen"):
            st.session_state.date_idee_liste = []
            st.session_state.zufalls_idee = None
            loesche_alle_ideen_db()

        if st.button("🎲 Zufalls-Idee ziehen"):
            if st.session_state.date_idee_liste:
                st.session_state.zufalls_idee = random.choice(st.session_state.date_idee_liste)
            else:
                st.session_state.zufalls_idee = None

        loesch_nummer = st.number_input("Nummer der Idee, die gelöschtwerden soll:", min_value=1, step=1, format="%d")
        if st.button("Idee löschen"):
            index = loesch_nummer -1
            if 0 <= index < len(st.session_state.date_idee_liste):
                idee_zum_loeschen = st.session_state.date_idee_liste.pop(index)
                loesche_idee_db(idee_zum_loeschen)
                st.success(f"Idee Nummer {loesch_nummer} wurde gelöscht")
            else:
                st.error("Ungültige Nummer")

    with spalte3:
        st.header("🎯 Date-Idee")
        if st.session_state.zufalls_idee:
            st.success(f"💡 Idee: **{st.session_state.zufalls_idee}**")
        else:
            st.info("Noch keine Zufalls-Idee gezogen.")
