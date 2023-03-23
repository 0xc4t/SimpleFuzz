## SimpleFuzz

![carbon](https://user-images.githubusercontent.com/105418279/224471690-acb7220a-39bb-4220-a562-f78c9abb56bd.png)

SimpleFuzz adalah sebuah tools (alat) yang digunakan untuk melakukan proses pengujian keamanan (security testing) pada aplikasi atau sistem dengan teknik pengujian fuzzer. Fuzzer adalah teknik pengujian keamanan yang menggunakan input data yang secara otomatis dihasilkan oleh program komputer untuk menguji kelemahan (vulnerability) pada suatu aplikasi atau sistem.

SimpleFuzz ditulis dengan menggunakan bahasa pemrograman Python dan dapat dijalankan pada platform Windows, Linux, maupun macOS. Tools ini juga dilengkapi dengan beberapa fitur seperti logging, pengaturan timeout, dan kemampuan untuk mengubah jenis input data.

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
