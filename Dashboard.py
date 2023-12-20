import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Pesan tiket Anda",
    page_icon="🚌",
    layout="wide",
)
def show_facilities():
        st.image("img/header.png")

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        h1,h2 ,h3, h4= st.columns([4,18,10,25])
        with h1:
            st.write("")
        with h2:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")

                st.header("Mulai Perjalanan Anda")
                st.write("Bus Santoso Siap Mengantarkan Anda")
                b1, b2 = st.columns([2,3.5])
                with b1:
                    st.button("Booking Now")
                with b2:
                    st.button("Learn More >")

        with h3:
            st.image("img/po.png", width=700)
        with h4:
            st.write("")
    
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")    

        video_file = open('img/bus.mp4', 'rb')
        video_bytes = video_file.read() 
        st.video(video_bytes)

        st.write("""
            Di sini Anda dapat mengetahui berbagai fasilitas yang disediakan oleh layanan bus kami.
            - Kursi yang nyaman
            - AC dan penyejuk udara
            - Wi-Fi gratis
            - Toilet    
            - Hiburan di perjalanan
        """)

def show_reviews():     
    st.header("Ulasan Pengguna")
    ulasan1, ulasan2, ulasan3 = st.columns(3)
    with ulasan1 :
        st.image("img/ulasan1.png")
    with ulasan2 :
        st.image("img/ulasan2.png")
    with ulasan3 :
        st.image("img/ulasan3.png")

def show_contact_info():
    st.header("Kontak Person")
    st.write("""
    Jika Anda memiliki pertanyaan atau memerlukan bantuan, silakan hubungi kami:
    - Email: santos@gmail.com
    - Telepon: 123-456-7890
    """)

def show_address():
    st.header("Alamat Kantor")
    st.write("""
    Anda juga dapat mengunjungi kantor kami di alamat berikut:
    PO BUS SANTOS
    Jalan panjang 
    Lampung, Indonesia
    """)

def show_ticket_info(jadwal_terpilih, jumlah_tiket, total_harga):
        st.header("Tiket Anda")
        st.write(f"Jadwal: {jadwal_terpilih}")
        st.write(f"Jumlah Tiket: {jumlah_tiket}")
        st.write(f"Total Harga: Rp {total_harga:,.0f}")

def show_payment(jadwal_terpilih, jumlah_tiket, total_harga):
        st.header("Menu Pembayaran")
        st.write(f"Jadwal: {jadwal_terpilih}")
        st.write(f"Jumlah Tiket: {jumlah_tiket}")
        st.write(f"Total Harga: Rp {total_harga:,.0f}")    

def main():
    data_jadwal = [
        {"nomor": "001", "tujuan": "Jakarta - Bandung", "jam": "08:00", "harga": 100000},
        {"nomor": "002", "tujuan": "Bandung - Surabaya", "jam": "10:00", "harga": 150000},
        {"nomor": "003", "tujuan": "Surabaya - Bali", "jam": "12:00", "harga": 200000},
        {"nomor": "004", "tujuan": "Bali - Semarang", "jam": "14:00", "harga": 250000},
        {"nomor": "005", "tujuan": "Semarang - Solo", "jam": "16:00", "harga": 300000},
        {"nomor": "006", "tujuan": "Solo - Jakarta", "jam": "11.00", "harga": 350000},
        {"nomor": "007", "tujuan": "Jakarta - Surabaya", "jam": "13.00", "harga": 400000},
        {"nomor": "008", "tujuan": "Surabaya - Semarang", "jam": "15.00", "harga": 450000},
        {"nomor": "009", "tujuan": "Semarang - Solo", "jam": "17.00", "harga": 500000},
        {"nomor": "010", "tujuan": "Solo - Bandung", "jam": "09.00", "harga": 550000},
        {"nomor": "011", "tujuan": "Bandung - Jakarta", "jam": "11.00", "harga": 600000},
        {"nomor": "012", "tujuan": "Jakarta - Semarang", "jam": "13.00", "harga": 650000},
        {"nomor": "013", "tujuan": "Semarang - Surabaya", "jam": "15.00", "harga": 700000},
        {"nomor": "014", "tujuan": "Surabaya - Solo", "jam": "17.00", "harga": 750000},
        {"nomor": "015", "tujuan": "Solo - Bali", "jam": "09.00", "harga": 800000},
    ]

    menu_selection = option_menu(menu_title=None,options=["Beranda", "Pesan Tiket", "Kontak Person", "About"], orientation="vertikal", key="nav")

    st.sidebar.write("Keluar dari akun")
    st.sidebar.button("Log Out")

    if menu_selection == "Beranda":
        show_facilities()
        show_reviews()

        s1, y = st.columns(2)
        with s1:
            st.header("PO Bus Santoso")
            st.video("https://www.youtube.com/watch?v=LGrnIpNUaSo")
        with y:
            st.write("")

    if menu_selection == "Pesan Tiket":

        col1, col2 = st.columns([2,0.5])
        with col1:
            jadwal_terpilih = st.selectbox("Pilih Jadwal Bus", [jadwal["nomor"] + " - " + jadwal["tujuan"] + " - " + jadwal["jam"] for jadwal in data_jadwal])
            hari = st.date_input("Hari Berangkat")
            jumlah_tiket = st.number_input("Jumlah Tiket", min_value=1, value=1)
            nama_penumpang = st.text_input("Nama Penumpang")
            nomor_telepon = st.text_input("Nomor telepon")
            nomor_kursi = st.selectbox("Pilih Nomor Kursi", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46))
        with col2:
            st.image("img/po.jpg", width=240)          

        if st.button("Pesan Tiket"):
            if not nama_penumpang.strip() or not nomor_telepon.strip():
                st.warning("Mohon lengkapi informasi penumpang.")
            else:
                for jadwal in data_jadwal:
                    if jadwal_terpilih.startswith(jadwal["nomor"]):
                        harga = jadwal["harga"]
                total_harga = jumlah_tiket * harga
                st.success(f"{jumlah_tiket} tiket berhasil dipesan untuk {jadwal_terpilih}. Total harga: Rp {total_harga:,}.")
                show_payment(jadwal_terpilih, jumlah_tiket, total_harga)

                st.subheader("Pilih Metode Pembayaran:")
                payment_option = st.selectbox("Metode Pembayaran", ("Transfer Bank BRI", "Kartu Kredit", "E-Wallet"))

        if st.button("Cetak Tiket"):
                col3, col4 = st.columns([2,3])
                with col3:
                    st.write("")
                with col4:
                    st.subheader("Scan Tiket Anda Disini")
                    st.image("img/qr.jpg")
                
    elif menu_selection == "Kontak Person":
        show_contact_info()
        show_address()

    elif menu_selection == "About" :
        st.subheader("Mengapa Memilih PO Santoso?")
        st.write("Sebagai bagian dari pelayanan kepada penumpang, PO Santoso menyediakan beberapa kelas untuk armadanya, antara lain Bisnis, Executive, dan Sinar Jaya Suite Class. Sinar Jaya terus meningkatkan kualitas pelayanan dan armadanya guna memberikan pengalaman perjalanan yang lebih nyaman dan aman bagi penumpang.")

        st.write("Berikut adalah beberapa alasan penting mengapa pesan tiket bus Santoso online untuk perjalanan Anda:")

        st.subheader("Rute yang luas")
        st.write("Setiap harga tiket bus Santoso selalu tersedia untuk keberangkatan dan penurunan penumpang di Pulau Jawa dan Pulau Sumatera. Karena itu, ke mana pun tujuan kita, baik yang dekat maupun jauh, akan selalu dilayani oleh jadwal Santoso.")

        st.subheader("Kualitas armada.")
        st.write("Tiket bus Santoso terus meningkatkan kualitas armadanya dengan melakukan pemeliharaan dan perawatan yang berkala dan ketat. Hal ini dilakukan guna memberikan pengalaman perjalanan yang lebih nyaman dan aman bagi penumpang.")

        st.subheader("Reputasi yang baik.")
        st.write("PO Santoso memiliki reputasi yang baik di kalangan penumpang karena kualitas layanan dan keamanan yang diberikan. Hal ini membuat Sinar Jaya Suite Class menjadi pilihan yang terpercaya dan populer di kalangan penumpang.")

        st.subheader("Sistem pengelolaan yang baik.")
        st.write("Sinar Jaya dikelola dengan baik dan tepercaya oleh PT Santoso Megah Langgeng dan bagian dari Santoso Group, sehingga memberikan jaminan bahwa perjalanan Anda akan diatur dengan baik dan aman")

if __name__ == "__main__":
    main()
