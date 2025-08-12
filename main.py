import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("halaman_utama.py",
    title=" Profil Desa",
    default=True)

Berita = st.Page("Berita_Bulan_Agustus_2025.py",
    title=" Berita Desa Bulan Agustus 2025",
    icon=":material/person:")

#Perlu diperhatikan perubahannya
#KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
#KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Berita" : [Berita],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()



