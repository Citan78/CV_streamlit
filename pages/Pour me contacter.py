import streamlit as st
from PIL import Image, ImageDraw, ImageOps

def main():
    st.title('Pour me contacter')

    st.markdown("**Téléphone** :")
    st.write("06 63 79 76 02")

    st.markdown("**E-mail** :")
    st.write(" itanchloe@gmail.com")

    st.markdown("**adresse** :")
    st.write(" 39 rue du Général Foy 8e")
    st.write(" 75008 Paris ")
    st.write(" 75008 Paris ")

    st.markdown("**Ages** :")
    st.write("  08/08/2003 (20 ans)")

    st.markdown("**linkedin**")
    st.write(" https://www.linkedin.com/in/chloe-itan-5a634b235")
      
if __name__ == '__main__':
    main()
