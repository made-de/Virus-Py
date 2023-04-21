import os
import shutil

try:
    from cryptography.fernet import Fernet
except ImportError:
    os.system('pip3 install cryptography')
    from cryptography.fernet import Fernet

print("باسوورد فك التسفير:\n")
password = ("abcde")
print(password)
with open("Password.txt", "rb") as f:
    key = f.read()

cipher = Fernet(key)

for root, dirs, files in os.walk("/storage/emulated/0/"):
    for filename in files:
        filepath = os.path.join(root, filename)
        with open(filepath, "rb") as f:
            encrypted = f.read()
        try:
            original = cipher.decrypt(encrypted)
        except Exception as e:
            print(f"Error decrypting file {filepath}: {e}")
            print(f"حدث خطاء اثناء فك تشفير الملف  {filepath}: {e}")
            continue

        with open(filepath, "wb") as f:
            f.write(original)

        print(f"File {filepath} decrypted.\n")
        print(f"تم فك تشفير الملف  {filepath} بنجاح.\n")
        decrypted_dir = os.path.join(root)
        if not os.path.exists(decrypted_dir):
            os.makedirs(decrypted_dir)
        shutil.move(filepath, os.path.join(decrypted_dir, filename))

print("Decryption complete.\n")
print("تم فم تشفير الملفات بنجاح.")
