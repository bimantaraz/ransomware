import os
from cryptography.fernet import Fernet

# Fungsi untuk mendekripsi file
def dekripsi_file(file_path, key):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    decrypted_data = f.decrypt(file_data)
    with open(file_path.replace('.teraz', ''), 'wb') as file:
        file.write(decrypted_data)
    os.remove(file_path)

# Konfigurasi direktori yang akan didekripsi (desktop)
DESKTOP_DIR = os.path.join(os.environ.get('USERPROFILE', os.environ.get('HOME', '/')), 'Desktop')

# Kunci enkripsi yang dikirim ke webhook Discord (ganti dengan kunci yang benar)
key = b'5oo_W9pLi1oSfYIOmRTPj6E26Vs_39pH6BQcx291BCg='  # Sesuaikan dengan kunci yang benar

# Mendekripsi file dengan ekstensi .teraz di direktori desktop

for file in os.listdir(DESKTOP_DIR):
    if file.endswith(".teraz"):
        dekripsi_file(os.path.join(DESKTOP_DIR, file), key)


