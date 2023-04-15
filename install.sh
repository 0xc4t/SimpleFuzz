echo "Installasi...."
sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt

echo "Config..."
chmod +x sfuzz
sudo mv sfuzz /usr/bin

echo "Path..."
cd ..
sudo mv SimpleFuzz /usr/share/

printf "Installasi berhasil..."
printf "jalankan tools dengan perintah, sfuzz -h"
