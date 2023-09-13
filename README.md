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


B.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 

![alt text](bagan.jpg)  
    Pertama, client akan membuat request ke URL aplikasi Django melalui internet. Kemudian, urls.py akan memetakan request tersebut melalui route yang menghubungkan URL yang diminta dengan fungsi atau kelas tampilan yang akan menanganinya. Lalu, views.py akan menerima permintaan dan memprosesnya sesuai dengan logika aplikasi. Misal dalam halaman profil, views akan memeriksa data pengguna yang diminta dan mempersiapkan data tersebut untuk ditampilkan. Selanjutnya views.py akan berinteraksi dengan models.py untuk mengakses atau memperbarui data di database. Setelah memproses data, views akan menggunakan template HTML yang berisi struktur dan elemen-elemen HTML untuk menyusun halaman web dengan mengisi data yang diperlukan. Setelah halaman web selesai dibuat, aplikasi akan mengirimkannya sebagai respons (response) kembali kepada client yang mengakses URL tersebut melalui internet dengan tampilan yang sesuai dengan request.  

C. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?  
    Virtual environment dibutuhkan untuk mengisolasi dependencies dari suatu proyek, yang dimana dependencies tersebut tercatat pada requirements.txt. Hal ini akan memudahkan developer dalam mengelola berbagai proyek karena tiap proyek akan memiliki environment dan dependenciesnya masing-masing yang sudah terpisah. Sebenarnya, aplikasi web berbasis Django tetap dapat dibuat tanpa menggunakan virtual environment jika hanya dilakukan pada server local. Namun, hal ini akan sulit dilakukan jika kita akan melakukan deploy project menggunakan online hoster karena online hoster perlu menyesuaikan dependencies yang diperlukan proyek dengan mesin hosting.

D. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya  
    a. MVC (Model-View-Controller):  
        - Model: Komponen yang mengatur dan mengelola logika aplikasi, data, validasi, dan interaksi.
        - View (Tampilan): Komponen yang mengontrol bagaimana data yang dikelola oleh model akan ditampilkan dengan menyiapkan komponenen-komponen yang akan terlibat seperti text boxes, dropdowns, dan lainnya.
        - Controller (Kontroler): Sebagai penengah dari Model dan View yang bertugas untuk memproses logika dan permintaan yang masuk dan berinteraksi dengan View untuk me-render output.
    b. MVT (Model-View-Template):  
        - Model: Sama seperti dalam Model dalam MVC yang bertugas mengelola data dan aplikasi.
        View (Tampilan): Berperan sebagai pengatur tampilan dengan mengambil data dari model untuk ditampilkan kepada pengguna
        - Template: Mengatur tampilan atau antarmuka pengguna dengan memisahkan kode HTML dari logika aplikasi untuk merancang tampilan yang diisi dengan data dari Model melalui View.
    c. MVVM (Model-View-ViewModel):
    - Model (Model): Sama seperti Model dalam MVC dan MVT yang bertugas mengelola data dan logika aplikasi.
    - View (Tampilan): Bertanggung jawab untuk menyiapkan elemen yang akan ditampilkan dan menerima input dari user.
    - ViewModel (Model Tampilan): Menjadi jembatan antara Model dan View yang mengontrol interaksi dari View  
    d. Perbedaan:  
    Pada MVC, terdapat controller yang mengendalikan Model dan View yang ditulis dengan kode spesifik untuk mengontrol. Sementara pada MVT, terdapat View yang menerima request dan mengembalikan respon dari HTTP dan Controller pada MVT sudah diatur oleh frameworknya sendiri.
    MVT adalah sebuah adaptasi dari MVC yang lebih khusus untuk kerangka kerja Django. Pada MVVM, logika yang digunakan yaitu data-binding, yang memudahkan dalam membuat perubahan pada aplikasi dibanding dengan MVC yang kodenya berlapis-lapis.
