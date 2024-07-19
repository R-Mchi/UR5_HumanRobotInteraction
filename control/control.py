from flask import Flask, request, jsonify
import re
import requests
from loguru import logger
import time

app = Flask(__name__)

file_path = 'captured_text.txt'


def clear_text_file():
    with open(file_path, 'w') as f:
        f.truncate(0)


def memeriksa_file(file_path, kalimat_list):
    try:
        # Membaca isi file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        for kalimat in kalimat_list:
            if re.search(re.escape(kalimat), text, re.IGNORECASE):
                return kalimat

        return None
    except FileNotFoundError:
        logger.error(f"File tidak ditemukan: {file_path}")
        return None
    except IOError as e:
        logger.error(f"Kesalahan membaca file: {e}")
        return None


def set_relay_state(relay, state):
    url = f"http://192.168.43.149/relay/{relay}"
    data = {'state': state}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        logger.info(f"Successfully set relay {relay} to state {state}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error setting relay state: {e}")


def process_relay_control():
    # Mengatur semua relay ke 'off' saat memulai
    set_relay_state(0, 'off')
    set_relay_state(1, 'off')
    set_relay_state(2, 'off')
    set_relay_state(3, 'off')
    set_relay_state(4, 'off')
    set_relay_state(5, 'off')
    set_relay_state(6, 'off')
    set_relay_state(7, 'off')

    # Daftar kalimat yang dicari dan state relay yang sesuai
    kalimat_aksi = {
        'buka',
        'tutup',
        'siap',
        'siaga',
        'ambilkan kotak',
        'ambilkan kaleng',
        'ambilkan botol',
        'makasih',
        'kesini'
    }

    """
    buka = 0
    tutup = 1
    siap = 2
    siaga = 3
    ambilkan kotak = 4
    ambilkan kaleng = 5
    ambilkan botol = 6
    kesini = 7
    terimakasih = 0
    """

    # Daftar kalimat untuk memeriksa
    kalimat = memeriksa_file(file_path, list(kalimat_aksi))

    # Logika if berdasarkan kalimat yang ditemukan
    if kalimat:
        print(kalimat)
        if kalimat == 'buka':
            aksi = 1
            clear_text_file()

        elif kalimat == 'tutup':
            aksi = 2
            clear_text_file()

        elif kalimat == 'siap':
            aksi = 3
            clear_text_file()

        elif kalimat == 'siaga':
            aksi = 4
            clear_text_file()

        elif kalimat == 'ambilkan kotak':
            aksi = 5
            clear_text_file()

        elif kalimat == 'ambilkan botol':
            aksi = 6
            clear_text_file()

        elif kalimat == 'ambilkan kaleng':
            aksi = 7
            clear_text_file()

        elif kalimat == 'makasih':
            aksi = 1
            clear_text_file()

        elif kalimat == 'kesini':
            aksi = 8
            clear_text_file()

        else:
            set_relay_state(0, 'off')
            set_relay_state(1, 'off')
            set_relay_state(2, 'off')
            set_relay_state(3, 'off')
            set_relay_state(4, 'off')
            set_relay_state(5, 'off')
            set_relay_state(6, 'off')
            set_relay_state(7, 'off')
            clear_text_file()

    else:
        print("Tidak ada kalimat yang sesuai ditemukan dalam file.")
        clear_text_file()

    # Aksi Null
    if aksi == 0:
        set_relay_state(0, 'off')
        set_relay_state(1, 'off')
        set_relay_state(2, 'off')
        set_relay_state(3, 'off')
        set_relay_state(4, 'off')
        set_relay_state(5, 'off')
        set_relay_state(6, 'off')
        set_relay_state(7, 'off')

    # Aksi Buka Grip
    if aksi == 1:
        set_relay_state(0, 'on')
        set_relay_state(1, 'off')
        set_relay_state(2, 'off')
        set_relay_state(3, 'off')
        set_relay_state(4, 'off')
        set_relay_state(5, 'off')
        set_relay_state(6, 'off')
        set_relay_state(7, 'off')

    # Aksi Tutup Grip
    if aksi == 2:
        set_relay_state(0, 'off')
        set_relay_state(1, 'on')
        set_relay_state(2, 'off')
        set_relay_state(3, 'off')
        set_relay_state(4, 'off')
        set_relay_state(5, 'off')
        set_relay_state(6, 'off')
        set_relay_state(7, 'off')

    # Aksi Siap
    if aksi == 3:
        set_relay_state(0, 'off')
        set_relay_state(1, 'off')
        set_relay_state(2, 'on')
        set_relay_state(3, 'off')
        set_relay_state(4, 'off')
        set_relay_state(5, 'off')
        set_relay_state(6, 'off')
        set_relay_state(7, 'off')

     # Aksi Siaga
    if aksi == 4:
        set_relay_state(0, 'off')
        set_relay_state(1, 'off')
        set_relay_state(2, 'off')
        set_relay_state(3, 'on')
        set_relay_state(4, 'off')
        set_relay_state(5, 'off')
        set_relay_state(6, 'off')
        set_relay_state(7, 'off')

     # Aksi Kotak
    if aksi == 5:
        set_relay_state(0, 'off')
        set_relay_state(1, 'off')
        set_relay_state(2, 'off')
        set_relay_state(3, 'off')
        set_relay_state(4, 'on')
        set_relay_state(5, 'off')
        set_relay_state(6, 'off')
        set_relay_state(7, 'off')

    # Aksi Botol
    if aksi == 6:
        set_relay_state(0, 'off')
        set_relay_state(1, 'off')
        set_relay_state(2, 'off')
        set_relay_state(3, 'off')
        set_relay_state(4, 'off')
        set_relay_state(5, 'on')
        set_relay_state(6, 'off')
        set_relay_state(7, 'off')

    # Aksi Kaleng
    if aksi == 7:
        set_relay_state(0, 'off')
        set_relay_state(1, 'off')
        set_relay_state(2, 'off')
        set_relay_state(3, 'off')
        set_relay_state(4, 'off')
        set_relay_state(5, 'off')
        set_relay_state(6, 'on')
        set_relay_state(7, 'off')

    # Aksi Orang
    if aksi == 8:
        set_relay_state(0, 'off')
        set_relay_state(1, 'off')
        set_relay_state(2, 'off')
        set_relay_state(3, 'off')
        set_relay_state(4, 'off')
        set_relay_state(5, 'off')
        set_relay_state(6, 'off')
        set_relay_state(7, 'on')


@app.route('/save-text', methods=['POST'])
def save_text():
    data = request.json
    if 'text' in data:
        text = data['text']
        with open(file_path, 'a') as f:
            f.write(text + '\n')

        # Proses kontrol relay setelah menyimpan teks
        process_relay_control()

        return jsonify({"status": "success", "message": "Text saved and relay control processed successfully"}), 200

    return jsonify({"status": "error", "message": "No text found"}), 400


if __name__ == "__main__":
    clear_text_file()  # Clear the file before starting the server
    app.run(host='0.0.0.0', port=5000)
