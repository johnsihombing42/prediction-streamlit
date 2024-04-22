import streamlit as st

def main():

    # Menampilkan logo universitas
    st.image("images/logo_usu.png", width=200)

    # Menampilkan judul halaman
    st.title("Tugas Akhir S-1 ILKOM USU")
    st.write("Nama: John Tri Putra Sihombing")
    st.write("NIM: 201401050")
    st.write("Program Studi: Ilmu Komputer")
    st.write("Fakultas Ilmu Komputer dan Teknologi Informasi")
    st.write("Universitas: Universitas Sumatera Utara")

    # Menampilkan judul skripsi
    st.write("Judul : IMPLEMENTASI ALGORITMA FB-PROPHET DAN ALGORITMA ARIMA DALAM MEMPREDIKSI HARGA KOIN CRYPTOCURRENCY")

    # Informasi dosen pembimbing
    st.write("Dosen Pembimbing 1:")
    st.write("- Nama: Dewi Sartika Ginting, S.Kom., M.Kom")
    st.write("- NIP: 199005042019032023")

    st.write("Dosen Pembimbing 2:")
    st.write("- Nama: Amer Sharif, S.Si., M.Kom")
    st.write("- NIP: 196910212021011001")


if __name__ == "__main__":
    main()
