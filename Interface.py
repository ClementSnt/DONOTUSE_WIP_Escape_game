import streamlit as st

st.set_page_config(page_title="Mission Archive", page_icon="🔐")

st.title("🔐 Mission : Archive Confidentielle")
st.write("Réponds correctement aux questions pour débloquer les coordonnées.")

# Coordonnées cibles
LAT_DECIMALS = "850618"
LON_DECIMALS = "308939"

# Initialisation état
if "progress" not in st.session_state:
    st.session_state.progress = 0

# Fonction affichage coordonnées
def display_coordinates():
    revealed = st.session_state.progress
    
    lat_display = LAT_DECIMALS[:revealed] + "_" * (6 - revealed)
    lon_display = LON_DECIMALS[:revealed] + "_" * (6 - revealed)

    st.subheader("📍 Coordonnées en cours de décryptage :")
    st.write(f"48.{lat_display} , 2.{lon_display}")

display_coordinates()

st.divider()

# Questions test
questions = [
    {"question": "Combien font 7 x 8 ?", "answer": "56"},
    {"question": "Quelle est la capitale de l'Espagne ?", "answer": "madrid"},
    {"question": "Combien y a-t-il de jours dans une semaine ?", "answer": "7"},
    {"question": "Quelle couleur obtient-on en mélangeant bleu et jaune ?", "answer": "vert"},
    {"question": "Combien de lettres dans le mot 'amour' ?", "answer": "5"},
    {"question": "Quelle est la première lettre de l'alphabet ?", "answer": "a"},
]

# Affichage progressif
if st.session_state.progress < len(questions):
    current_q = questions[st.session_state.progress]
    
    user_input = st.text_input(current_q["question"])
    
    if st.button("Valider"):
        if user_input.strip().lower() == current_q["answer"]:
            st.session_state.progress += 1
            st.success("Fragment débloqué.")
            st.rerun()
        else:
            st.error("Réponse incorrecte. Réessaie.")
else:
    st.success("🎉 Coordonnées complètes débloquées.")
    st.markdown("### 📍 48.850618 , 2.308939")

st.balloons()
st.success("MISSION VALIDÉE. Rendez-vous confirmé.")
