echo "Installasi...."
sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt

echo "Config..."
cp sfuzz.py sfuzz
sudo mv sfuzz /usr/bin

echo "Path..."
cd ..
mv sfuzz /usr/share/SimpleFuzz/

printf ("Installasi berhasil...")
printf ("jalankan tools dengan perintah, sfuzz -h")
