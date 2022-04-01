# Python Scraping

Pada repo ini terdapat 2 folder utama, dimana masing-masing mempunyai metode berbeda untuk melakukan scraping.
Di folder `request`, scraping menggunkan library `request`, dan pada folder `selenium` menggunakan library `Selenium`.

## Installation

Pastikan Anda sudah melakukan installasi Python di mesin Anda.
Dan pastikan telah mempunyai package manager [pip](https://pip.pypa.io/en/stable/) untuk installasi dependensi dari masing-masing folder.

Disini saya berasumsi bahwa Anda memiliki [VSCode](https://code.visualstudio.com/). Karena untuk menjalankan file pada folder `request` membutuhkan VSCode.

Arahkan terminal pada `Parent` dari 2 folder tersebut.

```bash
pip install -r requirements.txt
```

## Usage
#### Selenium
Diasumsikan bahwa Anda ingin mencoba pada folder Selenium terlebih dahulu dan telah membuka terminal dan sudah masuk ke folder Selenium di terminal Anda. Ketikan kode di bawah ini, dan tunggu script berjalan, diperkirakan sekitar ~2 menit untuk mendapatkan hasilnya.
```python
$ python main.py
```

#### request
Silahkan untuk membuka file `main.ipynb` dari folder request ke VSCode Anda, lalu pilih opsi "Run All" pada top-bar VSCode. Silahkan tunggu script berjalan, diperkirakan sekitar ~2 menit untuk mendapatkan hasilnya.

---
Hasil dari 2 metode scraping dapat di lihat pada masing-masing foldernya.

## License
[MIT](https://choosealicense.com/licenses/mit/)