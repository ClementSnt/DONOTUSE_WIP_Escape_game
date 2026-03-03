import streamlit as st
import time

st.set_page_config(page_title="Archive 10Y", page_icon="🔐")


LAT_DECIMALS = "850618"
LON_DECIMALS = "308939"
TOTAL_QUESTIONS = 6

questions = [
    {"question": "Combien font 7 x 8 ?", "answer": "56"},
    {"question": "Quelle est la capitale de l'Espagne ?", "answer": "madrid"},
    {"question": "Combien y a-t-il de jours dans une semaine ?", "answer": "7"},
    {"question": "Quelle couleur obtient-on en mélangeant bleu et jaune ?", "answer": "vert"},
    {"question": "Combien de lettres dans le mot 'amour' ?", "answer": "5"},
    {"question": "Quelle est la première lettre de l'alphabet ?", "answer": "a"},
]



if "progress" not in st.session_state:
    st.session_state.progress = 0

if "completed" not in st.session_state:
    st.session_state.completed = False



st.title("🔐 ARCHIVE CLASSIFIÉE")
st.caption("Niveau d'accès requis : Mémoire complète")



progress_ratio = st.session_state.progress / TOTAL_QUESTIONS
st.progress(progress_ratio)

st.write(f"Fragments restaurés : {st.session_state.progress} / {TOTAL_QUESTIONS}")

st.divider()



def display_coordinates():
    revealed = st.session_state.progress
    
    lat_display = LAT_DECIMALS[:revealed] + "_" * (6 - revealed)
    lon_display = LON_DECIMALS[:revealed] + "_" * (6 - revealed)

    st.subheader("📍 Localisation en cours de reconstruction")
    st.code(f"48.{lat_display} , 2.{lon_display}")

display_coordinates()

st.divider()


if not st.session_state.completed:

    if st.session_state.progress < TOTAL_QUESTIONS:
        current_q = questions[st.session_state.progress]
        
        st.subheader("🔎 Fragment suivant")
        user_input = st.text_input(current_q["question"], key="input")

        if st.button("Valider le fragment"):
            if user_input.strip().lower() == current_q["answer"]:
                
                with st.spinner("Décryptage en cours..."):
                    time.sleep(1.2)
                
                st.session_state.progress += 1
                st.success("Fragment restauré.")
                st.rerun()
            else:
                st.error("Mémoire insuffisante. Réessaie.")

    else:
        st.session_state.completed = True
        st.rerun()


if st.session_state.completed:

    st.success("✔ Reconstruction complète")
    st.subheader("📍 Coordonnées validées")
    st.code("48.850618 , 2.308939")

    time.sleep(0.8)
    st.balloons()

    st.markdown("### 🕒 Heure du rendez-vous : 20:30")
    st.markdown("### 📅 Date : 20/03")

    st.success("MISSION VALIDÉE. RDV confirmé.")
