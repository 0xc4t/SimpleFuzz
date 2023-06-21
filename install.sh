Y='\033[1;33m'
N='\033[0m'

printf "${Y}Installasi....${N}"

sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt

printf  "${Y}Config...${N}"

printf  "${Y}Path...${N}"

cd ..
sudo mv SimpleFuzz /usr/share/

printf "${Y}Installasi berhasil...${N}"

printf "${Y}jalankan tools dengan perintah, sfuzz -h ${N}"

