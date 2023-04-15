Y='\033[1;33m'
N='\033[0m'

echo "${Y}Installasi....${N}"
sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt

echo "${Y}Config...${N}"
chmod +x sfuzz
chmod +x msfuzz
sudo mv sfuzz msfuzz /usr/bin

echo "${Y}Path...${N}"
cd ..
sudo mv SimpleFuzz /usr/share/

printf "${Y}Installasi berhasil...${N}"
printf "${Y}jalankan tools dengan perintah, sfuzz -h dan msfuzz -h ${N}"
