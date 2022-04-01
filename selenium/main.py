# Import Library
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time

# Inisialisasi Selenium agar fullscreen
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

# Install Selenium Driver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Buka website Techinasia
driver.get('https://www.techinasia.com/jobs/search?country_name[]=Indonesia')\
# Set timer agar tidak terdeteksi BOT
time.sleep(1)

# Karena Techinsia ini "Infinite Scroll", jadi harus di scroll sampai selesai dahulu
# Aagar semua data dapat terambil
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Menggunakan BeautifulSoup parser dengan format "lxml"
soup = BeautifulSoup(driver.page_source, 'lxml')

# Mencari "Card" dari setiap listing untuk di ambil datanya
job_lists = soup.find_all('div', class_='jsx-1749311545 container')

# Inisialisasi variabel 
# Langsung menggunakan pandas DataFrame
job_data = pd.DataFrame({'Link': [],
                         'Position': [],
                         'Company': [],
                         'Location': [],
                         'Salary': [],
                         'Published Date': []})

# Looping semua card dari `job_lists` untuk di ambil satu-persatu datanya
for job_list in job_lists:
    # Inisialisasi full link techinasia, untuk digabungkan dengan link dari listing job
    full_link = 'https://www.techinasia.com'

    # Mencari link dari listing job
    base_link = job_list.find('b', class_='jsx-1749311545')
    position = base_link.find('a').text
    # Mengambil link
    link = base_link.find('a').get('href')
    # Menggabungkan link dari listing job dengan full link techinasia
    full_job_link = full_link + link

    # Menentukan base atau container dari card job listing
    base_details = job_list.find('div', class_='jsx-1749311545 details')
    # Mencari posisi pekerjaan / Title
    position = base_details.find_all('a')[0].text
    # Mencari nama perusahaan 
    company = base_details.find_all('a')[1].text
    # Mencari lokasi perusahaan
    location = base_details.find_all('div', class_='jsx-1749311545')[2].text
    # Mencari tanggal listing tersebut di buat
    published_date = job_list.find(
        'span', class_='jsx-1022654950 published-at').text

    # Menentukan base atau container dari informasi Meta
    base_additional_data = job_list.find(
        'ul', class_='jsx-1749311545 additional-meta')
    # Mencari industri perusahaan
    industry = base_additional_data.find_all(
        'li', class_='jsx-1749311545')[1].text
    # Mencari tipe pekerjaan tersebut (i.e Full Time, Freelance, Etc)
    job_type = base_additional_data.find_all(
        'li', class_='jsx-1749311545')[2].text

    # Menggunakan try-except untuk bagian salary
    # Karena tidak semua dari listring tersebut mempunyai informasi salary
    # Apabila tidak menggunakan ini akan terjadi error, karena selenium tidak menemukannya
    try:
        salary = job_list.find_all(
            'div', class_='jsx-1749311545 compensation')[0].text
    except:
        salary = 'NA'

    # Setelah semua ditemukan
    # Data tersebut dimasukan ke dalam `job_data` 
    job_data = job_data.append(
        {'Link': full_job_link,
         'Position': position,
         'Company': company,
         'Location': location,
         'Salary': salary,
         'Published Date': published_date}, ignore_index=True)

# Export ke .json
job_data.to_json('data-json-table.json', orient='table')
job_data.to_json('data-json-index.json', orient='index')
