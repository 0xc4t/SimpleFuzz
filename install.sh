Y='\033[1;33m'
N='\033[0m'

echo"${Y}Installasi....${N}"

sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt


echo "${Y}Path...${N}"

sudo cp sfuzz /usr/bin
sudo cp sfuzz /usr/local/bin

echo"${Y}Installasi berhasil...${N}"

echo"${Y}jalankan tools dengan perintah, sfuzz -h ${N}"

