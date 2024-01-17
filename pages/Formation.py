import streamlit as st
from PIL import Image, ImageDraw, ImageOps

def main():
    st.title('Expérience professionnelle')

    # Utilisation de st.expander() pour créer une section extensible
    with st.expander("IUT Paris-Rives de Seine -  Statistique et Informatique Décisionnelle"):

        st.markdown("**Statistique et Informatique Décisionnelle**")

        st.write("Sept 2021 - en cours ")

        st.write("Le BUT STID (statistique et informatique décisionnelle) forme des techniciens capables d’aider à la prise de décision par des activités de gestion de données (data management), d’analyse et de programmation statistiques, mais aussi de restitution. ")   
            

    with st.expander("Lycée Jean Rostand (Mantes-la-Jolie)"):
        st.write(" Sept 2020 -Juin 2021 (1 an )")

        st.markdown("**Baccalauréat :**")

        st.write("Option mathématique complémentaire Spécialité, science et vie de la terre Spécialité physique chimie ")   
        st.write("mention assez bien")   

if __name__ == '__main__':
    main()