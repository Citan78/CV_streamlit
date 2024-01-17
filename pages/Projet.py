import streamlit as st
from PIL import Image, ImageDraw, ImageOps

def main():
    st.title('Expérience professionnelle')


    with st.expander("Enquête sur des sprinteurs du 100 m"):

        st.write("IUT Paris-Rives de Seine   ")

        st.markdown("**Quelles conditions affectent la course du sprinteur ?**")

        st.write("Récupération de la base de données sur 1000 sprinteurs")
        st.write("Nettoyage de la base de données sur R")
        st.write("Création de graphique sur R")
        st.write("Test statistique sur R ")
        st.write("Présentation de la réponse à l’oral sur Power Point  ")   
            

    with st.expander("Visualisation de données sur les caractéristiques de la formation "):

        st.write("IUT Paris-Rives de Seine   ")

        st.markdown("**Quelles sont les caractéristiques de notre formation ?**")

        st.write("Création de la base de données ")
        st.write("Création de graphiques sur Tableau ")
        st.write("Création de posters sur Canvas  ")    

if __name__ == '__main__':
    main()