import streamlit as st
import time

st.set_page_config(page_title="Archive 10Y", page_icon="🔐")


LAT_DECIMALS = "850618"
LON_DECIMALS = "308939"
TOTAL_QUESTIONS = 6

questions = [
    {"question": "Combien de pays ont visité ensemble les sousous ?", "answer": "13"},
    {"question": "Numéro et rue de la première adresse commune des sousous ?", "answer": "1005 argyle street"},
    {"question": "Où est parti Tof ?", "answer": "courir"},
    {"question": "Combien de fois Jul prononce t'il le son 'sous' dans son tube 'sousou' ?", "answer": "14"},
    {"question": "Prénom et Nom du célébre moniteur de parachutisme dont le certificat a été honteusement perdu' ?", "answer": "victor rollinger"},
    {"question": "Que se dice la sousous antes de cruzar un obstaculo ?", "answer": "a la poté no se falta"},
]



if "progress" not in st.session_state:
    st.session_state.progress = 0

if "completed" not in st.session_state:
    st.session_state.completed = False



st.title("🔐 ARCHIVE CLASSIFIÉE")
st.caption("Error : Niveau d'accès supérieur requis")



progress_ratio = st.session_state.progress / TOTAL_QUESTIONS
st.progress(progress_ratio)

st.write(f"Chargement des données : {st.session_state.progress} / {TOTAL_QUESTIONS}")

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
        
        st.subheader("🔎 Indice suivant")
        user_input = st.text_input(current_q["question"], key="input")

        if st.button("Valider l'indice"):
            if user_input.strip().lower() == current_q["answer"]:
                
                with st.spinner("Décryptage en cours..."):
                    time.sleep(1.2)
                
                st.session_state.progress += 1
                st.success("Indice validé")
                st.rerun()
            else:
                st.error("Mémoire insuffisante. Réessaie.")

    else:
        st.session_state.completed = True
        st.rerun()


if st.session_state.completed:

    time.sleep(0.5)
    st.balloons()

    st.success("Mission complète. RDV confirmé le 20/03 à 20:30 (précise hein pas 15min de retard)")
