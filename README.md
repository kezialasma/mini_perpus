Nama    : Kezia Lasma Angelica

NPM     : 2206082234

Kelas   : PBP A

Link Adaptable  : https://mini-perpus.adaptable.app

<details>
<summary>TUGAS 3</summary>

1. Apa perbedaan antara form POST dan form GET dalam Django?  
    Method GET dan Post merupakan method yang digunakan untuk mengirim request HTTP ke server. Perbedaanya yaitu terletak pada tampilan URL, dimana GET akan menampilkan request HTTP pada URL, sementara POST tidak menampilkan request HTTP sehingga lebih aman untuk data yang membutuhkan privasi.  
    Contoh:  
    GET     : google.com/search?q=difference+between+post+and+get  
    POST    : https://scele.cs.ui.ac.id/user/profile.php?id=5465 (tidak menampilkan username dan password)  

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?  
    a. XML     : Menggunakan markup tags sebagai basis sintaksnya. Sifat datanya terstruktur dan memiliki validasi yang kuat sehingga biasanya digunakan untuk konfigurasi aplikasi.
    b. JSON    : Menggunakan format pasangan key dan value. JSON mempunyai struktur yang lebih sederhana dibandingkan XML, namun ukuran datanya jauh lebih efisien sehingga biasanya digunakan untuk pengembangan web yang membutuhkan pertukaran data antara server dan client.
    c. HTML     : HTML juga menggunakan markup tags sebagai basis sintaksnya, namun tujuannya adalah untuk merender tampilan sehingga biasanya digunakan untuk membuat tampilah halaman web  

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?  
    JSON sering digunakan dalam pertukaran data aplikasi web modern karena formatnya lebih sederhana dan ringkas (menjadi lebih mudah dibaca oleh mesin) sehingga komunikasi pertukaran data dapat berlangsung dengan cepat  

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
    A. Membuat input form untuk menambahkan objek model pada app sebelumnya  
        - Membuat berkas forms.py pada direktori main untuk menginisiasi fields data yang akan dibutuhkan untuk produk. Pada produk saya, saya menggunakan fields name, amount, description, price serta   
        - Menambahkan import HttpResponseRedirect, ProductForm, dan reverse pada views.py
        - Membuat fungsi createProduct dengan parameter request untuk menginisiasi formulir yang menambahkan data produk yang baru diisi pada file tersebut
        - Menambahkan variabel products = Product.objects.all() pada views.py agar seluruh objek Product tersimpan di database
        - Membuka file urls.py di direktori utama untuk melakukan import fungsi create_product serta me-routing path create_product ke urlpatterns
        - Membuat file create_product.html pada templates yang mengextend base.html. File ini akan menginisiasi tampilan untuk "Add Products"  
    B. Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.  
        - Untuk melihat dalam format HTML, buat fungsi baru pada views.py, yaitu create_item dengan request untuk merender request product
        - Kemudian membuat file create_item.html pada templates untuk membuat tampilan page "Add Items"
        - Untuk format HTML dan JSON, impor HttpResponse dan serializers pada views.py, yang dimana serializers berfungsi untuk translater objek ke model XML dan JSON  
        - Membuat fungsi show_xml dan show_JSON yang menerima parameter request dengan melakukan serialize response data ke XML atau JSON
        - Jika ingin melihat objek berdasarkan ID, maka tambahkan fungsi show_xml_by_id dan show_json_by_id dengan menambahkan parameter id kedalam fungsi  
        - Tambahkan fungsi-fungsi yang telah dibuat tadi sebagai import kedalam folder urls.py dan menambahkan path URL fungsi-fungsi tadi kedalam urlpatterns  
    C. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.  
    -  Mengimpor fungsi-fungsi yang telah dibuat kedalam urls.py dan menambahkan path url kedalam urlpatterns
    ```python
    from django.urls import path
    from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-item', create_item, name='create_item'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),  
    ]
    ```  
5. Screenshot Postman  
    A. HTML  
    ![HTML](image/html.png)
    B. XML  
    ![XML](image/xml.png)
    C. JSON  
    ![JSON](image/json.png)
    D. XML by ID
    ![XML](image/xml_2.png)
    E. JSON by ID
    ![JSON](image/json_1.png)

Referensi:
- https://aws.amazon.com/id/compare/the-difference-between-json-xml/

</details>

<details>
<summary>TUGAS 2</summary>
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
    
</details>