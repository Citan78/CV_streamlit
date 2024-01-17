import streamlit as st
from PIL import Image, ImageDraw, ImageOps


def main():
    st.title('Expérience professionnelle')

    # Utilisation de st.expander() pour créer une section extensible
    with st.expander("Stage en data analyse (Veoneer/Magna)"):
        st.write(" Avril 2023 - Juillet 2023 (3 mois)")

        st.markdown("**Evaluation des performances d'un système de détection et de classification des occupants d'un véhicule?**")

        # Ajout de texte descriptif
        st.write("Collecte de données ")
        st.write("Analyses statistiques de bases de données avec Python ")   
        st.write("Création et automatisation des indicateurs de performances avec Python ")    
        st.write("Modélisation de la base de données sur Power BI ")   
        st.write("Création de tableaux de bord sur Power BI ")  

        # Ajout de l'image en carré
        st.image('indicateur.png', use_column_width=False, width=350)

        # Ajout de l'image en carré
        st.image('PowerBi.png', use_column_width=False, width=650)

if __name__ == '__main__':
    main()


