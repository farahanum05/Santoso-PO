import streamlit as st
import mysql.connector

# Koneksi ke database MariaDB
def connect_to_db():
    try:
        # Ganti dengan informasi koneksi database MariaDB 
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

def register_page():

    st.image("img/header.png")
    st.title("Halaman Registrasi")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")

    if st.button("Register"):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            # Ganti dengan query penyimpanan data ke dalam database
            query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (username, password, email))
                conn.commit()
                st.success("Registrasi berhasil")
            except mysql.connector.Error as e:
                st.error(f"Error: {e}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()

def main():
    register_page()

if __name__ == "__main__":
    main()