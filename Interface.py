import streamlit as st

st.set_page_config(page_title="Mission Archive", page_icon="🔐")

st.title("🔐 Mission : Archive Confidentielle")
st.write("Réponds correctement aux questions pour débloquer les coordonnées.")

# Initialisation état
if "progress" not in st.session_state:
    st.session_state.progress = 0

# Coordonnées cibles (exemple)
LAT_PARTS = ["48", "8", "5"]
LON_PARTS = ["2", "3", "4"]
TIME_PARTS = ["20", "30"]

# Fonction affichage coordonnées
def display_coordinates():
    lat_display = "48." 
    lon_display = "2."
    
    if st.session_state.progress >= 1:
        lat_display += LAT_PARTS[1]
    else:
        lat_display += "__"
        
    if st.session_state.progress >= 2:
        lat_display += LAT_PARTS[2]
    else:
        lat_display += "__"
        
    if st.session_state.progress >= 3:
        lon_display += LON_PARTS[1]
    else:
        lon_display += "__"
        
    if st.session_state.progress >= 4:
        lon_display += LON_PARTS[2]
    else:
        lon_display += "__"

    st.subheader("📍 Coordonnées en cours de décryptage :")
    st.write(f"Latitude : {lat_display}")
    st.write(f"Longitude : {lon_display}")

    if st.session_state.progress >= 6:
        st.success(f"🕒 Heure du rendez-vous : {TIME_PARTS[0]}:{TIME_PARTS[1]}")

display_coordinates()

st.divider()

# Questions test (random pour l'instant)
questions = [
    {
        "question": "Combien font 7 x 8 ?",
        "answer": "56"
    },
    {
        "question": "Quelle est la capitale de l'Espagne ?",
        "answer": "madrid"
    },
    {
        "question": "Combien y a-t-il de jours dans une semaine ?",
        "answer": "7"
    },
    {
        "question": "Quelle couleur obtient-on en mélangeant bleu et jaune ?",
        "answer": "vert"
    },
    {
        "question": "Combien de lettres dans le mot 'amour' ?",
        "answer": "5"
    },
    {
        "question": "Quelle est la première lettre de l'alphabet ?",
        "answer": "a"
    }
]

# Affichage progressif des questions
if st.session_state.progress < len(questions):
    current_q = questions[st.session_state.progress]
    
    user_input = st.text_input(current_q["question"])
    
    if st.button("Valider"):
        if user_input.strip().lower() == current_q["answer"]:
            st.session_state.progress += 1
            st.success("Bonne réponse. Fragment débloqué.")
            st.rerun()
        else:
            st.error("Réponse incorrecte. Réessaie.")
else:
    st.success("🎉 Toutes les coordonnées ont été débloquées.")
