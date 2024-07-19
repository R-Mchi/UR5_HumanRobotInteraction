import streamlit as st
import os

# Fungsi untuk menampilkan teks yang disimpan
def load_text():
    if os.path.exists("captured_text.txt"):
        with open("captured_text.txt", "r") as file:
            text = file.read()
        return text
    return "No text found"

# Fungsi utama Streamlit
def main():
    st.title("Google Assistant Text Capture")
    st.write("This application displays text captured from Google Assistant.")
    
    if st.button("Load Text"):
        captured_text = load_text()
        st.write("Captured Text:")
        st.write(captured_text)

if __name__ == "__main__":
    main()
