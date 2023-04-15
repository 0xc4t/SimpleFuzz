echo "Installasi...."
sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt

echo "Config..."
chmod +x sfuzz
chmod +x msfuzz
sudo mv sfuzz msfuzz /usr/bin

echo "Path..."
cd ..
sudo mv SimpleFuzz /usr/share/

printf "Installasi berhasil..."
printf "jalankan tools dengan perintah, sfuzz -h"
