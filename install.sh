sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt
sudo chmod +x sfuzz
sudo cp sfuzz /usr/bin
sudo cp sfuzz /usr/local/bin

echo "SUCCESS"
