## SimpleFuzz

![carbon](https://user-images.githubusercontent.com/105418279/224471690-acb7220a-39bb-4220-a562-f78c9abb56bd.png)


SimpleFuzz adalah sebuah alat fuzzing open source yang dikembangkan oleh Varel Security untuk menguji kerentanan pada perangkat lunak. Alat ini dirancang untuk mempermudah proses pengujian fungsional pada program dengan memberikan input yang acak dan mencari respons yang tidak diharapkan.

### Installation
```
sudo apt-get install python3 python3-pip
git clone https://github.com/varelsecurity/SimpleFuzz
cd SimpleFuzz
sudo pip3 install -r requirement.txt
python3 simplefuzz.py
```

### Cara Menggunakan
```
python3 simplefuzz.py -u [Url] -w [wordlist] -o [output.txt]
```
### Testing on 

* kali linux
* ubuntu
* pydroid
