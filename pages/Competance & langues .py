import streamlit as st
from PIL import Image, ImageDraw, ImageOps

def main():
    st.title('Competance & langues ')


    with st.expander("Langages informatiques"):

        st.write("Python")
        st.write("R")
        st.write("SAS")
        st.write("SQL ")
        st.write("HTM/CSV")   
            

    with st.expander("Logiciels informatiques"):

        st.write("PowerBI ")
        st.write("Tableau ")
        st.write("Suite Microsoft Office (Word, Excel, Access)  ")    

    
    with st.expander("Compétences d'informatique décisionnelle et de statistiques"):

        st.write("Base de données")
        st.write("Informatique décisionnelle")
        st.write("Statistique inférentielle ") 
        st.write("Test statistique  ") 
        st.write("Test paramétrique ") 
        st.write("Statistique descriptive ") 
        st.write("Data Visualisation")

    with st.expander("Langues"):

        st.write("Anglais LV1")
        st.write("Espagnol LV2")

if __name__ == '__main__':
    main()