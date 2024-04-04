import random
import pyfiglet
from fucksyon import *

class colors:
    whiteman = "\033[1;37m"
    blahdziheyl = "\033[91m"

a = 'THE NIGGA SQUAD'

print(colors.whiteman + a)

ascii_banner = pyfiglet.figlet_format('TNS')
print(ascii_banner)

print(colors.blahdziheyl + "[1]=={====PHISHING=ATTACK=>")
print(colors.blahdziheyl + "[2]=={====AUTO=SQLI=ATTACKS=>")

option = int(input(colors.whiteman + "=SELECT=PLEASE=: "))

if option == 1:
    clear()

    import subprocess

    cmd = "bash fishing.sh"
    p=subprocess.Popen(cmd,shell=True)
    NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
    print(BOBO_ERROR_HAHAHAH_KAWAWA)
    print(NAG_OUT_TANGINANG_YAN)

if option == 2:
    clear()

    import subprocess

    cmd = "python autosqli.py"
    p=subprocess.Popen(cmd,shell=True)
    NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
    print(BOBO_ERROR_HAHAHAH_KAWAWA)
    print(NAG_OUT_TANGINANG_YAN)
