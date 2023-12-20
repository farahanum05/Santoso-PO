import streamlit as st
import mysql.connector

st.set_page_config(
    page_title="Pesan tiket Anda",
    page_icon="🚌",
    layout="wide",
)

# Koneksi ke database MariaDB
def connect_to_db():   
    try:
        # Ganti dengan informasi koneksi database MariaDB kamu
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="flora050903",
            database="tubes"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error: {e}")
        return None

def login_page():



    st.image("img/header.png")
    st.title("Halaman Login")

    st.subheader("Halaman Login User")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Melakukan validasi login di sini
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            # Ganti dengan query validasi login sesuai kebutuhanmu
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            
            if result:
                st.success("Login berhasil")
            else:
                st.error("Login gagal. Cek kembali username dan password")


    st.write("")
    st.write("")
    st.write("")    
    
    st.subheader("Halaman Login Admin")
    st.text_input("Username Admin")
    st.text_input("Password Admin", type="password")
    st.button("Login Admin")

def main():
    login_page()

if __name__ == "__main__":
    main()