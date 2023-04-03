import os 
import argparse
from colorama import Fore

os.system('clear')
print (Fore.LIGHTGREEN_EX,f'''
                \||/
                |  @___oo
      /\  /\   / (__,,,,| SFuzz v2.0
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___))
 | \____(      )___) )___
  \______(_______;;; __;;;

[+] Fuzzing subdomain list [beta]
[+] Author : KucingMalas
''')
parser = argparse.ArgumentParser()
parser.add_argument('-l','--list', required=True, help="Masukan list url eg : url.txt")
args = parser.parse_args()

wordlist_url = open(args.list,'r')
list_url = wordlist_url.readlines()

for url in list_url:
    lists = url.strip()
    os.system(f'python3 sfuzz.py -u {lists}')