# Import modul

import os
import sys
import argparse
import requests as r
from colorama import Fore

os.system('clear')

headers = {
	'User-Agent':'Macintosh Mac OS X'
}

parser = argparse.ArgumentParser()

print(Fore.LIGHTCYAN_EX ,'''
 ___  _       ___                    
| . \<_> _ _ | __>___  _ _  ___  ___ 
| | || || '_>| _>/ . \| '_>/ | '/ ._>
|___/|_||_|  |_| \___/|_|  \_|_.\___.
''')
parser.add_argument('-w','--wordlist', type=str, required=True,help="Masukan Wordlist")
parser.add_argument('-u','--url', type=str, required=True, help="Masukan URL")
args = parser.parse_args()

os.system("clear")
print (Fore.LIGHTCYAN_EX, '''
####################################
##[`'`']####(:)#####[`'`']###\`~'/##
###|  |#####|:|######|  |####(o o)##
###|__|#####|:|######|__|#####\ / \#
###############################"####
''')
print("Author : Varel Security")
print("")
print("[+] Wordlist: ",args.wordlist)
print("[+] URL: ", args.url)
print("")

list = open(args.wordlist)
word = list.readlines()

for i in word:
    line = i.strip()
    request = r.get(f'{args.url}{line}')
    url_path = (f"{args.url}{line}")
    if request.status_code == 200:
        print (Fore.GREEN,f"(Status: {request.status_code}) [Size : {len(request.content)}] \t{url_path}")
    elif request.status_code ==404:
        print (Fore.RED,f"(Status: {request.status_code}) [Size : {len(request.content)}] \t{url_path}")
    elif request.status_code==301:
        print (Fore.BLUE,f"(Status: {request.status_code}) [Size : {len(request.content)}] \t{url_path}")
