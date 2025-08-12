import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>DESA SIDODADI</h1>
        <p style='font-size: 2em;'>Ke. Teluk Pandan Kab. Pesawaran Provinsi Lampung</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=1vgsssx6JFSRMSyRlFirKMuoKIh-f6z9F"

def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)



def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#FDFFE2",
            },
            "nav-link-selected": {"background-color": "#83B4FF"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Desa</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Desa Sidodadi, yang terletak di Kecamatan Teluk Pandan, Kabupaten Pesawaran, 
            merupakan salah satu desa pesisir di Provinsi Lampung yang memiliki potensi besar di bidang lingkungan dan pariwisata. 
            Desa ini dikenal dengan kekayaan ekosistem mangrove yang menjadi daya tarik utama ekowisata Cuku Nyi‑Nyi. 
            Wilayahnya berada di pesisir Teluk Lampung dan sebagian besar masyarakatnya bermata pencaharian sebagai nelayan, petani, serta pelaku UMKM. 
            Selain itu, berbagai program pembangunan berbasis lingkungan dan pemberdayaan masyarakat aktif dijalankan melalui kerja sama antara pemerintah desa, BUMDes, dan kelompok-kelompok masyarakat.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()
