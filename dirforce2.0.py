import os
import sys
import argparse
import httpx as r
from colorama import Fore
from threading import Thread
import time

os.system('clear')


parser = argparse.ArgumentParser()

print(Fore.LIGHTCYAN_EX ,'''
 ___  _       ___                    
| . \<_> _ _ | __>___  _ _  ___  ___ 
| | || || '_>| _>/ . \| '_>/ | '/ ._>
|___/|_||_|  |_| \___/|_|  \_|_.\___.

[+] Version : 2.0 [+]
''')
parser.add_argument('-w','--wordlist', type=str, required=True,help="Enter Wordlist")
parser.add_argument('-u','--url', type=str, required=True, help="Enter URL (eg. https://example.com/)")
parser.add_argument('-o','--output', type=str, required=False, help="Enter OUTPUT (eg. name.txt)")
parser.add_argument('-t', '--threads', type=int, default=1, help="threads")
args = parser.parse_args()
os.system("clear")
print (Fore.LIGHTCYAN_EX, '''

####################################
##[`'`']####(:)#####[`'`']###\`~'/##
###|  |#####|:|######|  |####(o o)##
###|__|#####|:|######|__|#####\ / \#
###############################"####

v2.0
''')
print("Author : Varel Security")
print("")
print("[+] Wordlist: ",args.wordlist)
print("[+] Url: ", args.url)
print("[+] Output:", args.output)
print("[+] Threads:", args.threads)
print("")

list = open(args.wordlist)
word = list.readlines()

def fuzz(file):
    request = r.get(f"{args.url}{file}")
    url_path = (f'(Status : {request.status_code}) ( Url {args.url}{file} \n')
    if request.status_code == 200:
        print (Fore.LIGHTGREEN_EX,f"(Status: {request.status_code}) [Size : {len(request.content)}]\t {args.url}{file}")
        a = open(f'200.{args.output}','a')
        a.write(url_path)

    elif request.status_code in ['301','302','303','304']:
        print (Fore.LIGHTBLUE_EX,f"(Status: {request.status_code}) [Size : {len(request.content)}]\t {args.url}{file}")
        b = open(f'301.{args.output}','a')
        b.write(url_path)

    elif request.status_code == 403:
        print (Fore.LIGHTBLACK_EX,f"(Status: {request.status_code}) [Size : {len(request.content)}]\t {args.url}{file}")
        c = open(f'403.{args.output}','a')
        c.write(url_path)

    elif request.status_code == 404:
        None

threads = []

for i in word:
    file = i.strip()
    threads.append(Thread(target=fuzz, args=(file,)))

else:
    print('Start Fuzzing....\n')

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
