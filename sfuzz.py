#!/usr/bin/env python3

import httpx as r
import argparse
import time, sys, os
from urllib.parse import urlparse
from colorama import Fore
from threading import Thread
from datetime import datetime


print (Fore.LIGHTGREEN_EX,f'''

.▄▄ · ▪  • ▌ ▄ ·.  ▄▄▄·▄▄▌  ▄▄▄ .·▄▄▄▄• ▄▌·▄▄▄▄•·▄▄▄▄•
▐█ ▀. ██ ·██ ▐███▪▐█ ▄███•  ▀▄.▀·▐▄▄·█▪██▌▪▀·.█▌▪▀·.█▌
▄▀▀▀█▄▐█·▐█ ▌▐▌▐█· ██▀·██▪  ▐▀▀▪▄██▪ █▌▐█▌▄█▀▀▀•▄█▀▀▀•
▐█▄▪▐█▐█▌██ ██▌▐█▌▐█▪·•▐█▌▐▌▐█▄▄▌██▌.▐█▄█▌█▌▪▄█▀█▌▪▄█▀
 ▀▀▀▀ ▀▀▀▀▀  █▪▀▀▀.▀   .▀▀▀  ▀▀▀ ▀▀▀  ▀▀▀ ·▀▀▀ •·▀▀▀ • V 2.0
[+] Author : KucingMalas

''')
parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', required=True, help='Masukan url website target eg: https://example.com/')
parser.add_argument('-w','--wordlist', required=False,default='/usr/share/SimpleFuzz/db/dic.txt' ,help='Masukan wordlist')
parser.add_argument('-o','--output', required=False,default='output.txt' ,help='Masukan nama output eg: output.txt')
parser.add_argument('-t','--thread', type=int,default=25 ,help='Masukan jumlah thread')
args = parser.parse_args()

parsed_url = urlparse(args.url)
if parsed_url.scheme not in ["https", "http"]:
    print(Fore.LIGHTRED_EX,"[!] Masukan https:// atau http://\n")
    sys.exit()

if parsed_url.scheme in ["https", "http"] and not parsed_url.path.endswith('/'):
    print(Fore.LIGHTRED_EX,"[!] URL harus diakhiri dengan /\n")
    sys.exit()

wordlist = open(args.wordlist, "r")
lists = wordlist.readlines()

os.system('clear')
print (Fore.LIGHTGREEN_EX,'''
.▄▄ · ▪  • ▌ ▄ ·.  ▄▄▄·▄▄▌  ▄▄▄ .·▄▄▄▄• ▄▌·▄▄▄▄•·▄▄▄▄•
▐█ ▀. ██ ·██ ▐███▪▐█ ▄███•  ▀▄.▀·▐▄▄·█▪██▌▪▀·.█▌▪▀·.█▌
▄▀▀▀█▄▐█·▐█ ▌▐▌▐█· ██▀·██▪  ▐▀▀▪▄██▪ █▌▐█▌▄█▀▀▀•▄█▀▀▀•
▐█▄▪▐█▐█▌██ ██▌▐█▌▐█▪·•▐█▌▐▌▐█▄▄▌██▌.▐█▄█▌█▌▪▄█▀█▌▪▄█▀
 ▀▀▀▀ ▀▀▀▀▀  █▪▀▀▀.▀   .▀▀▀  ▀▀▀ ▀▀▀  ▀▀▀ ·▀▀▀ •·▀▀▀ • V 2.0
                                Code by varel security
''')

parsed_url = urlparse(args.url)
if parsed_url.scheme not in ["https", "http"]:
    print(Fore.LIGHTRED_EX, "[!] Masukan https:// atau http://\n")
    sys.exit()

if parsed_url.scheme in ["https", "http"] and not parsed_url.path.endswith('/'):
    print(Fore.LIGHTRED_EX, "[!] URL harus diakhiri dengan /\n")
    sys.exit()

wordlist = open(args.wordlist, "r")
lists = wordlist.readlines()

def fuzz(file):
    try:
        x = r.get(f'{args.url}{file}', verify=True, follow_redirects=True)
        url_path = (f'[STATUS : {x.status_code}] [{args.url}{file}]\n')
        if x.status_code in [200, 201, 202, 203, 204, 205, 206, 207, 208]:
            print(Fore.LIGHTGREEN_EX, f"[STATUS: {x.status_code}] [Size : {len(x.content)}]\t {args.url}{file}")
            a = open(f'200-OK.{args.output}', 'a')
            a.write(url_path)
            a.close()

        elif x.status_code in [301, 302, 303, 304, 305, 306, 307, 308] and x.history:
            for resp in x.history:
                print(Fore.LIGHTBLUE_EX, f"[STATUS: {x.status_code}] [Size : {len(x.content)}]\t {args.url}{file} -> {x,url_path} Redirect -> {resp.url}")
                b = open(f'301-REDIRECT.{args.output}', 'a')
                b.write(url_path)
                b.close()

        elif x.status_code == 403:
            print(Fore.LIGHTMAGENTA_EX, f"[STATUS: {x.status_code}] [Size : {len(x.content)}]\t {args.url}{file}")

    except:
        pass

Threads = []
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print(f'::: Starting fuzzing {dt_string}')
print(f'::: Scope    : {args.url}')
print(f'::: Wordlist : {args.wordlist}')
print(f'::: Output   : {args.output}')
print(f'::: Thread   : {args.thread}')
print('')

for i in lists:
    file = i.strip()
    Threads.append(Thread(target=fuzz, args=(file,)))

for i in range(0, len(Threads), args.thread):

    for threads in Threads[i:i+args.thread]:
        threads.start()

    for threads in Threads[i:i+args.thread]:
        threads.join()

print('')
print(Fore.LIGHTYELLOW_EX, f'[Stop Fuzzing {dt_string}]')

