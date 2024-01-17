import streamlit as st
from PIL import Image, ImageDraw, ImageOps

def add_circle_mask(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    size = (150, 150)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output

def main():
    st.title('Bienvenue dans l\'application CV')

    # Ajout de l'image en cercle
    image = add_circle_mask('photo.jpg')
    st.image(image, use_column_width=False, width=150)

    # Ajout de texte descriptif
    st.write(
        "Je suis étudiante en 3e année de statistique et informatique décisionnelle. En ce moment, en alternance à la DRIEAT.\n"
        "J'ai créé ce site afin de vous partager mon portfolio de manière créative. Si vous êtes intéressé par mon profil, "
        "n'hésitez pas à me contacter ou à devenir membre pour bénéficier des dernières modifications effectuées sur le site."
    )

if __name__ == '__main__':
    main()



