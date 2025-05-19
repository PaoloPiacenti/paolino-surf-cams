# ui/auth.py
import streamlit as st

 # ui/auth_simple.py
import streamlit as st
import bcrypt

HASH = b"$2b$12$9LFUENwFMoroNniNk6pk9OmBrdz0nnXU/lM03BmDKPhXU/MVTtEnS"

def require_password():
    """Blocca l’app finché non viene inserita la password corretta."""
    # campo errore dopo un tentativo fallito
    if st.session_state.get("auth_failed"):
        st.error("Wrong password, try again.")

    if st.session_state.get("authenticated"):
        return  # già loggato → prosegui con l’app

    # ⬇️ form di login
    with st.form("login_form", clear_on_submit=True):
        pwd = st.text_input("Password", type="password")
        submit = st.form_submit_button("Enter")

    if submit:
        if bcrypt.checkpw(pwd.encode(), HASH):
            st.session_state["authenticated"] = True
            st.session_state["auth_failed"] = False
            st.rerun()          # ricarica pagina senza il form
        else:
            st.session_state["auth_failed"] = True
            st.rerun()          # mostra subito il messaggio

    # se non ancora autenticato, blocca il resto dell’app
    st.stop()
