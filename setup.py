import time
import sys
import colorama
import itertools
import threading
import os
from colorama import init, Fore, Back, Style

os.system('wget https://raw.githubusercontent.com/MalwareMix/PsychoSploit/main/PsychoSploit.py > /usr/bin && mv /usr/bin/PsychoSploit.py /usr/bin/psychosploit')

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(Style.BRIGHT + Fore.MAGENTA + '\rInstalling ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(Style.BRIGHT + Fore.MAGENTA + '\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True


print('Now all you need to do to access PsychoSploit anywhere is just type "psychosploit" in your terminal \n make sure that you still have the PsychoSploit Directory still in your home folder!')