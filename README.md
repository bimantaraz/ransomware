# Ransomware Teraz

This project contains two main scripts: `ransom.py` and `decrypt.py`, demonstrating how to encrypt and decrypt files using the symmetric encryption algorithm **Fernet** from the **Cryptography Library**.

- `ransom.py`: This script encrypts files with certain extensions from the user's directory and then sends the encryption key to a **Discord webhook**.
- `decrypt.py`: A script to decrypt the files that have been encrypted using the key obtained from the **Discord webhook**.

> **🚨⚠️WARNING⚠️🚨:**
> This is a ransomware-like script intended solely for **educational purposes**. Using this script for malicious or illegal activities is against the law.

## Features
- **Encrypts** files with specific extensions like `.txt`, `.docx`, `.pdf`, etc.
- **Sends the encryption key** to a **Discord webhook**.
- **Decrypts** files using the encryption key sent to the webhook.

## Requirements
- Python 3.x
- Python module `cryptography`
- Python module `requests` for sending the encryption key to the Discord webhook

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bimantaraz/ransomware.git
   cd ransomware-script
   ```

2. Install dependencies:
   ```bash
   pip install cryptography requests
   ```

## Usage

### Encrypt Files
1. Edit the `ransom.py` script and add your Discord webhook URL to the `WEBHOOK_URL` variable.
2. Run the `ransom.py` script:

   ```bash
   python ransom.py
   ```
   The script will encrypt specific files in the user's directory (Windows or other OS) and send the encryption key to the Discord webhook.

### Decrypt Files
1. Retrieve the encryption key sent to the Discord webhook.
2. Replace the `KEY_FROM_WEBHOOK` in the `decrypt.py` script with the correct key.
3. Run the `decrypt.py` script to decrypt the files encrypted on the desktop directory:
   
   ```bash
   python decrypt.py
   ```
### Video :
https://video.anugrahbimantara.my.id/videos/ransomware.mp4

### Example Key :
![zzz](https://github.com/user-attachments/assets/855a9e0e-454b-4fbf-a93b-94b7bba8e380)


## 🚨⚠️WARNING⚠️🚨
This project is **for educational purposes only**. Using this script without permission to damage, steal data, or engage in other illegal activities is a serious legal violation and can lead to criminal charges.
