import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>Berita Bulan Agustus</h1>", unsafe_allow_html=True) #heading halaman

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "KKN Bersama Internasional 2025"
        ],
        icons=[
            "people-fill"
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((1920, 1080))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Berita: {data_list[i]['berita']}")
            st.write(f"Penulis: {data_list[i]['penulis']}")
            st.write(f"Tanggal publikasi: {data_list[i]['publikasi']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# Ubah bagian ini
if menu == "KKN Bersama Internasional 2025": #judul
    def kknbi():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sZHWuuSqwxkk2ZbaGBjkikXMb68i8KEr", #gambar
        ]
        data_list = [ #isi berita
            {
                "berita": "KKN Bersama Internasional tahun 2025 melibatkan seluruh kampus BKS-PTN Barat. Kelompok 18 merupakan salah satu kelompok yang ditempatkan di Kabupaten Pesawaran. "
                "Memiliki 9 anggota yang berasal dari berbagai daerah di Indonesia membuat KKN tahun ini berbeda. "
                "Program unggulannya bertujuan untuk memajukan wisata bahari dan UMKM yang berada di Desa Sidodadi."
                ""
                " Kelompok 18 terdiri dari 9 anggota yang berasal dari 7 Badan Kerja Sama Perguruan Tinggi Negeri Wilayah Barat (BKS-PTN Barat). Fathinah Nur Azizah (Institut Teknologi Sumatera)"
                "menjadi ketua kelompok dan anggota lainnya adalah: Haidar Khadafi (Institut Teknologi Sumatera), Tiana Azzahra (Institut Teknologi Sumatera), Aji Fhahriyan (Universitas Syah Kuala),"
                "Greece Ravaell (Universitas Palangka Raya), Nurul Dwi Endarina (Universitas Bengkulu), Nindya Armen Salsabila (Universitas Andalas),"
                "Theo Sefa (Universitas Terbuka), Safitri Mutiara Putri (Universitas Lampung).",
                "penulis": "KKN Bersama Internasional 2025",
                "publikasi":"14 Agustus 2025",# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kknbi()

elif menu == "Perpisahan KKN Bersama Internasional 2025 dengan Perangkat Desa": #judul
    def LepasPisah():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sZHWuuSqwxkk2ZbaGBjkikXMb68i8KEr", #gambar
        ]
        data_list = [ #isi berita
            {
                "berita": "KKN Bersama Internasional tahun 2025 melibatkan seluruh kampus BKS-PTN Barat. Kelompok 18 merupakan salah satu kelompok yang ditempatkan di Kabupaten Pesawaran. "
                "Memiliki 9 anggota yang berasal dari berbagai daerah di Indonesia membuat KKN tahun ini berbeda. "
                "Program unggulannya bertujuan untuk memajukan wisata bahari dan UMKM yang berada di Desa Sidodadi."
                ""
                " Kelompok 18 terdiri dari 9 anggota yang berasal dari 7 Badan Kerja Sama Perguruan Tinggi Negeri Wilayah Barat (BKS-PTN Barat). Fathinah Nur Azizah (Institut Teknologi Sumatera)"
                "menjadi ketua kelompok dan anggota lainnya adalah: Haidar Khadafi (Institut Teknologi Sumatera), Tiana Azzahra (Institut Teknologi Sumatera), Aji Fhahriyan (Universitas Syah Kuala),"
                "Greece Ravaell (Universitas Palangka Raya), Nurul Dwi Endarina (Universitas Bengkulu), Nindya Armen Salsabila (Universitas Andalas),"
                "Theo Sefa (Universitas Terbuka), Safitri Mutiara Putri (Universitas Lampung).",
                "penulis": "KKN Bersama Internasional 2025",
                "publikasi":"14 Agustus 2025",# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    LepasPisah()


