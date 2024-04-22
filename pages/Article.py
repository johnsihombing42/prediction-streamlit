import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Tentang Cryptocurrency")
    st.markdown("Selamat datang! Di sini Anda dapat membaca artikel tentang pengertian Cryptocurrency, Bitcoin, dan Ethereum.")

    # Artikel tentang Cryptocurrency
    st.header("Cryptocurrency")
    st.markdown("Cryptocurrency adalah mata uang digital yang menggunakan teknologi kriptografi untuk mengamankan transaksi dan mengontrol penciptaan unit baru. Cryptocurrency tidak diatur oleh otoritas pusat seperti bank atau pemerintah.")

    # Artikel tentang Bitcoin
    st.header("Bitcoin")
    st.markdown("Bitcoin adalah cryptocurrency pertama yang diperkenalkan pada tahun 2009 oleh seseorang yang menggunakan nama samaran Satoshi Nakamoto. Bitcoin menggunakan teknologi blockchain untuk mencatat semua transaksi dan memiliki jumlah maksimum 21 juta koin.")

    # Artikel tentang Ethereum
    st.header("Ethereum")
    st.markdown("Ethereum adalah platform blockchain yang memungkinkan pengembang untuk membangun dan menjalankan aplikasi terdesentralisasi. Ether (ETH) adalah cryptocurrency yang digunakan di platform Ethereum.")

    # Chart Bitcoin
    st.subheader("Chart Bitcoin")
    components.html('<iframe src="https://www.tradingview.com/widgetembed/?symbol=BITSTAMP:BTCUSD&interval=D&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=%5B%5D&hideideas=1&theme=Light" style="width: 100%; height: 600px;"></iframe>', height=600)

    # Chart Ethereum
    st.subheader("Chart Ethereum")
    components.html('<iframe src="https://www.tradingview.com/widgetembed/?symbol=BITSTAMP:ETHUSD&interval=D&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=%5B%5D&hideideas=1&theme=Light" style="width: 100%; height:600px;"></iframe>', height=600)

if __name__ == "__main__":
    main()