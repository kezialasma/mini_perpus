Nama    : Kezia Lasma Angelica

NPM     : 2206082234

Kelas   : PBP A

Link Adaptable  : https://mini-perpus.adaptable.app

A.  Checklist

1. Membuat sebuah proyek Django baru:   
    a. Membuat direktori lokal yang kemudian akan menjadi direktori utama  
    b. Menyalakan virtual environment setiap akan membuat proyek baru agar dependencies untuk tiap proyek terisolasi  
    c. Menyiapkan dependencies dalam berkas requirements.txt dan menginstallnya  
    d. Membuat proyek baru dengan command `django-admin startproject`

2. Membuat aplikasi dengan nama main pada proyek tersebut: Menjalankan command `python manage.py startapp main` pada direktori utama dan mendaftarkannya pad settings.py

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main: Membuat berkas urls.py pada direktori main dan mengisi file tersebut dengan:  
    a. Mengimpor path dari django.urls untuk mendefinisikan pola URL.
    b. Menggunakan fungsi `show_main` dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
    c. Memberikan app_name untuk memberikan nama unik pada pola URL dalam aplikasi.

4.  Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib: Mengisi berkas models.py dengan 
    a. models.Model yaitu kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
    b. Product yaitu nama model yang ingin didefinisikan.
    c. Menambahkan atribut seperti nama, harga, dan deskripsi dan mengelompokkan tiap atribut kedalam tipe data yang sesuai seperti CharField, DateField, IntegerField, dan TextField.

5.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu:
    a. Mengisi berkas views.py dengan `from django.shortcuts import render`
    b. Menambahkan fungsi `def show_main(request)` yang mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
    c. Menambahkan "context" yang berisi data yang akan dikirimkan ke tampilan (berupa data nama dan kelas)
    d. Menambahkan "render" tampilan yang berisi
        - `request` yang berisi objek permintaan HTTP yang dikirim oleh pengguna.
        - `main.html` yang berisi berkas template yang akan digunakan untuk me-render tampilan.
        - `context` yang merupakan dictionary berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.

6.  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py: Menambahkan isi urls.py pada direktori proyek dengan mengimpor fungsi include dari django.urls dan rute URL dari aplikasi lain untuk diarahkan ke tampilan main melalui variabel urlpatterns

7.  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet:
    a. Membuat akun Adaptable dan menyambungkannya dengan akun GitHub
    b. Membuat "New App" dan menyambungkannya dengan repositori GitHub yang sudah ada dengan memilih "All Repositories" pada proses instalasi
    c. Memilih repositori yang akan di-deploy ke Adaptable
    d. Memilih Python App Template sebagai template deployment dan memilih PostgreSQL sebagai tipe basis data yang akan digunakan.
    e. Menyesuaikan versi Python dengan spesifikasi aplikasi dengan mengecek terlebih dulu versi python melalui penyalaan virtual environment dan menjalankan python --version.
    f. Menambahkan `python manage.py migrate && gunicorn mini_perpus.wsgi` pada bagian "Start Command"
    g. Memasukkan nama aplikasi yang akan menjadi domain untuk situs web aplikasi dan mencentang HTTP Listener on PORT
    h. Klik "Deploy App", kemudian proses deployment akan dimulai