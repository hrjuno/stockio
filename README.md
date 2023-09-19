Nama           : Harjuno Abdullah

Kelas          : PBP C

Link Adaptable : https://stockio.adaptable.app/main/

---
# Tugas 3
<details>
<summary>1) Perbedaan antara form `POST` dan form `GET` dalam Django</summary>

  * **DESKRIPSI**
      * POST
        Browser mengemas data formulir, memproses dalam bentuk code untuk pengiriman, dan mengirimkannya ke server. Respon diterima setelah pengolahan di sisi server.
      * GET
  
  * **PENGGUNAAN**
      * POST
        Digunakan untuk permintaan yang dapat mengubah keadaan sistem, seperti operasi yang mempengaruhi database.
      * GET
        Digunakan untuk permintaan yang tidak mempengaruhi keadaan sistem, seperti permintaan pencarian atau operasi lainnya.

  * **METODE PENGIRIMAN**  
      * POST
        Data  dikirim sebagai bagian dari permintaan HTTP POST. Data ini tidak akan muncul di URL dan biasanya digunakan untuk mengirim data yang bersifat sensitif atau besar, seperti kata sandi atau unggahan file.
      * GET
        Data dikirim sebagai parameter dalam URL. Data ini akan terlihat di baris URL dan biasanya digunakan untuk mengirim data yang tidak sensitif, seperti parameter pencarian atau filter.  

  * **KEAMANAN**
      * POST
        Lebih aman karena informasi yang mengandung data sensitif tidak terlihat dalam URL dan tidak mudah diakses oleh pihak ketiga.
      * GET
        Kurang aman untuk data sensitif dan operasi sistem penting karena data dikirimkan dalam URL dan dapat terlihat oleh orang lain.

  * **CACHING**
      * POST
        POST tidak dapat disimpan dalam cache, karena permintaan POST dapat mengubah data server.
      * GET
        GET dapat disimpan dalam cache, karena permintaan GET bersifat idempoten (tidak mengubah data server). Namun, ini juga berarti bahwa permintaan GET dapat disajikan dari cache dan tidak selalu mengambil data terbaru dari server.
</details>

<details>
<summary>2) Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data</summary>

  * **XML (eXtensible Markup Language)**
      * Tujuan Utama
        XML digunakan untuk menyimpan dan mempertukarkan data terstruktur antar sistem. Ini memungkinkan untuk mendefinisikan struktur data khusus sesuai kebutuhan.
      * Keunggulan
        Cocok untuk data yang kompleks dan terstruktur dengan kebutuhan validasi yang ketat. Dapat digunakan dalam berbagai konteks seperti konfigurasi, pertukaran data, dan penyimpanan terstruktur.
      * Kekurangan
        Lebih berat dan kompleks dalam hal sintaksis, memerlukan lebih banyak karakter untuk mendefinisikan elemen dan struktur data. 
 
  * **JSON (JavaScript Object Notation)**
      * Tujuan Utama
        JSON terutama digunakan untuk pertukaran data di lingkungan yang lebih ringan dan efisien seperti web dan aplikasi seluler. Ini adalah format data ringan yang memanfaatkan sintaksis JavaScript.
      * Keunggulan
        Lebih ringan dan lebih efisien dalam hal ukuran file dan penggunaan bandwidth. Memiliki format yang lebih mudah dibaca oleh manusia dan lebih mudah diproses oleh mesin.
      * Kekurangan
        Tidak mendukung validasi bawaan, membutuhkan pendekatan manual untuk memastikan data sesuai dengan struktur yang diinginkan. 
    
  * **HTML (Hypertext Markup Language)**
      * Tujuan Utama
        HTML digunakan untuk membuat struktur dan tata letak halaman web, serta menentukan cara konten disajikan di browser.
      * Keunggulan
        Cocok untuk menampilkan konten dan interaksi pengguna di browser. Memiliki kemampuan bawaan untuk menampilkan gambar, video, tautan, formulir, dan elemen UI lainnya.
      * Kekurangan
        Fokus utama pada presentasi dan tata letak, bukan penyimpanan atau pertukaran data terstruktur.

</details>

<details>
<summary>3) Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern</summary>

  * **Readability**

      JSON menggunakan struktur data yang sederhana dan mudah dipahami oleh manusia. Data disusun dalam format teks yang terorganisir dengan baik, membuatnya mudah untuk dibaca dan diinterpretasikan oleh pengembang dan mesin.

  * **Efisiensi**

      JSON memiliki ukuran yang kecil dibandingkan dengan format pertukaran data lain seperti XML. Ini mengakibatkan pengiriman dan penerimaan data yang lebih cepat, menghemat waktu dan sumber daya jaringan.

  * **Keamanan**

      JSON memungkinkan penggunaan metode validasi dan sanitasi data untuk memastikan bahwa data yang diterima adalah data yang benar dan aman. Pengguna dapat menerapkan kontrol keamanan tambahan seperti enkripsi untuk melindungi data.

  * **Fleksibilitas**

      JSON mendukung struktur data yang fleksibel, memungkinkan pengembang untuk menyesuaikan format data sesuai dengan kebutuhan spesifik aplikasi. Jika diperlukan, dapat dengan mudah menambahkan atau mengubah atribut data tanpa mempengaruhi kompatibilitas dengan aplikasi lain.

  * **Kompatibilitas**
  
      JSON kompatibel dengan sebagian besar bahasa pemrograman dan platform. Ini memungkinkan aplikasi yang ditulis dalam bahasa yang berbeda untuk saling berkomunikasi dan bertukar data tanpa mengalami kendala kompatibilitas.

</details>

<details>
<summary>4) Bagaimana cara mengimplementasikan checklist pada tugas</summary>

- [x] **Membuat input `form` untuk menambahkan objek model pada app sebelumnya**

   Buat file di direktori `main` bernama `forms.py` lalu tambahkan `Product` (yang ada pada `models.py`) supaya isi dari form akan disimpan menjadi objek `Product` dengan meminta `fields` yang sesuai pada `models.py`.
   Buka file `views.py` di direktori `main` juga dan meng-import beberapa fungsi:
   ```
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse
   ```
   Lalu buat fungsi baru bernama `create_product` yang menerima parameter `request`, isi dari `create_product` adalah:
   ```
   def create_product(request):
      form = ProductForm(request.POST or None)
      
      if form.is_valid() and request.method == "POST":
         form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
      
      context = {'form': form}
      return render(request, "create_product.html", context)
   ```
   `form = ProductForm(request.POST or None)` berguna untuk membuat `ProductForm` baru dengan cara memasukkan QueryDict sesuai pada input _user_ di `request.POST`. `form.is_valid()` ditambahkan supaya dapat mengecek apakah isi input di form tersebut valid atau tidak. `form.save()` berguna untuk membuat sekaligus menyimpan data dari form. `return HttpResponseRedirect(reverse('main:show_main'))` untuk me-redirect user kembali ke halaman utama setelah menyimpan data form.
   
- [x] **Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID**
      
    * HTML

      Dalam folder `templates` di root folder dan buat file HTML baru dengan nama `base.html` sebagai template dasar yang digunakan sebagai kerangka umum untuk halaman-halaman web lainnya pada proyek. Pada `base.html` isi dengan:
      ```
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
          <head>
              <meta charset="UTF-8" />
              <meta
                  name="viewport"
                  content="width=device-width, initial-scale=1.0"
              />
              {% block meta %}
              {% endblock meta %}
          </head>
      
          <body>
              {% block content %}
              {% endblock content %}
          </body>
      </html>
      ```
      Buka file `settings.py` yang ada di subdirektori `stockio` dan cari variabel `TEMPLATES` lalu tambahkan code ini supaya `base.html` data dideteksi sebagai template:
      ```
      'DIRS': [BASE_DIR / 'templates']
      ```
      Pada subdirektori `templates` yang ada di `main` ubah `main.html` menjadi:
      ```
      {% extends 'base.html' %}

      {% block content %}
          <h1>STOCKIO</h1>
          <h2>Selling physical copies of movies</h2>

          <h4>App Name: {{ app_name }}</h4>

          <h4>Name: {{ name }}</h4>

          <h4>Class: {{ class }}</h4>
      {% endblock content %}
      ```
      Pada file `views.py` ubah fungsi `show_main` dengan menambahkan `products = Product.objects.all()` untuk mengambil seluruh objek Product yang ada di _database_ lalu tambahkan `'products': products` pada variabel `context` untuk menampilkan seluruh objek Product yang ada di _database
      Buat file baru dengan nama `create_product.html` di direktori `main/templates`. Isi dengan kode:
      ```
      {% extends 'base.html' %} 
   
      {% block content %}
      <h1>Add New Product</h1>
      
      <form method="POST">
          {% csrf_token %}
          <table>
              {{ form.as_table }}
              <tr>
                  <td></td>
                  <td>
                      <input type="submit" value="Add Product"/>
                  </td>
              </tr>
          </table>
      </form>
      
      {% endblock %}
      ```
      `<form method="POST">` untuk menandakan block mana yang digunakan untuk form dengan metode POST. `{% csrf_token %}` bertanggung jawab menjadi token untuk menjaga keamanan supaya tercegah dari serangan berbahaya. `{{ form.as_table }}` untuk menampilan fields pada form yang sudah dibuat di file `forms.py` sebagai tabel. `<input type="submit" value="Add Product"/>` menjadi tombol submit untuk mengirimkan request ke view `create_product(request)`.
      Buka file `main.html` dan tambahkan kode di dalam `{% block content %}` supaya dapat menampilkan data produk dalam bentuk tabel sekaligus tombol "Add New Product" yang akan me-redirect ke halaman form:
      ```
      ...
      <table>
          <tr>
              <th>Movie Title</th>
              <th>Amount</th>
              <th>Synopsis</th>
          </tr>
      
          {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
      
          {% for product in products %}
          <tr>
              <td>{{product.name}}</td>
              <td>{{product.amount}}</td>
              <td>{{product.price}}</td>
              <td>{{product.description}}</td>
          </tr>
          {% endfor %}
      </table>
      
      <br />
      
      <a href="{% url 'main:create_product' %}">
          <button>
              Add New Product
          </button>
      </a>
      
      {% endblock content %}
      ```

    * Serializer untuk XML dan JSON

      Buka file `views.py` pada direktori `main` lalu impor fungsi `HttpResponse` dan fungsi `Serializer` yang digunakan untuk menerjemahkan objek model menjadi format lain (seperti XML atau JSON).

    * XML

      Buat fungsi `show_xml` yang menerima parameter _request_ dan buat variabel `data` yang akan menyimpan hasil query dari seluruh data yang ada di `Product` lalu return functionnya adalah `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi dalam format XML dan parameter `content_type="application/xml".`.

    * JSON

      Buka file `views.py` di folder `main` lalu buat fungsi baru bernama `show_json` dengan variabel `data` yang akan menyimpan seluruh hasil query data yang ada pada `Product`. Tambahkan return function berupa `HttpResponse` yang memiliki paramater data hasil query yang udah diserialisasi menjadi JSON dan parameter `content_type="application/json"`.

    * ID XML dan JSON

      Buka file `views.py` di folder `main` lalu buat fungsi baru bernama `show_xml_by_id` dan `show_json_by_id` dengan variabel `data` yang akan menyimpan hasil query data dengan id tertentu yang ada pada `Product`. Tambahkan return function berupa `HttpResponse` yang memiliki paramater data hasil query yang udah diserialisasi menjadi JSON atau XML dan parameter `content_type` yang sesuai dengan format XML atau JSON (format XML: `"application/xml"` atau format JSON: `"application/json"`).

- [x] **Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2**

    Buka file `urls.py` pada folder `main` dan impor fungsi `create_product, show_xml, show_json` tadi dari `views.py` sekaligus tambahkan path url:
   ```
   ...
   path('create-product', create_product, name='create_product'),
   path('xml/', show_xml, name='show_xml'),
   path('json/', show_json, name='show_json')
   path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
   path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
   ...
   ```
   ke dalam variabel `urlpatterns` untuk bisa menggunakan fungsi yang sudah diimpor tadi.

</details>

<details>
<summary>Screenshots Postman</summary>

* **HTML**

  ![HTML](https://github.com/hrjuno/stockio/assets/121445072/22b2032e-9179-4a72-9b75-620903309437)

* **XML**

  ![XML](https://github.com/hrjuno/stockio/assets/121445072/8a635e1d-a0f5-41a1-a0a1-1d1d6107d2f3)

* **JSON**
  
  ![JSON](https://github.com/hrjuno/stockio/assets/121445072/f48f9a10-6dd1-4952-9b99-455afa2228af)

* **XML by ID**

  ![XML_by_ID](https://github.com/hrjuno/stockio/assets/121445072/483ce8fd-8a4c-4d89-904f-2f814caf1159)

* **JSON by ID**

  ![JSON_by_ID](https://github.com/hrjuno/stockio/assets/121445072/c112a72a-3b8f-4dc5-8463-aac753a883f4)

</details>

Referensi:
- https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-2
- https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/
- https://brandmed.com/blog/development/the-power-of-json-whats-behind-the-popularity
- https://www.w3schools.com/tags/ref_httpmethods.asp
- https://www.guru99.com/json-vs-xml-difference.html

---
# Tugas 2
<details>
<summary>1) Bagaimana cara mengimplementasikan checklist pada tugas</summary>

- [x] **Membuat sebuah proyek Django baru**

   Langkah pertama dilakukan dengan membuat direktori baru dengan nama stockio dan mengaktifkan Virtual Environment pada direktori tersebut, hal ini dilakukan untuk isolasi saat pemasangan dependencies (yang berisi library, framework, atau package untuk membantu proses pengembangan) antara proyek proyek yang berbeda. Lalu, kita buat proyek Django dan mengonfigurasi proyek dengan mengubah `ALLOWED_HOSTS` di file `settings.py` supaya kita terdaftar menjadi host yang memiliki izin untuk mengakses aplikasi web.

- [x] **Membuat aplikasi dengan nama `main` pada proyek tersebut**

  Kita dapat membuat aplikasi bernama `main` dalam proyek tersebut dengan menjalankan perintah:
  ```
  python manage.py startapp main
  ```
  pada direktori utama stockio untuk membuat folder bernama `main` yang berisikan struktur awal aplikasi `main` milik kita.
      
- [x]  **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`**

  Lalu untuk memasukkan aplikasi `main` yang telah kita buat tadi ke dalam proyek _stockio_, kita membuka file `settings.py` dan menambahkan `'main'` (nama aplikasi yang kita buat tadi) pada variabel `INSTALLED_APPS`. Hal ini dilakukan untuk mendaftarkan aplikasi `main` ke dalam proyek stockio.  
         
- [x]  **Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut**
      
  * `name` sebagai nama item dengan tipe `CharField`.
  * `amount` sebagai jumlah item dengan tipe `IntegerField`.
  * `description` sebagai deskripsi item dengan tipe `TextField`.
     
    Modifikasi file `models.py` pada aplikasi `main` untuk membuat model baru, kita membuat class Product sebagai nama model yang akan kita buat. Lalu kita menambahkan atribut `name` dengan tipe data `CharField`, `amount` dengan tipe data `IntegerField`, dan `description` dengan tipe data `TextField`. Agar Django dapat mengetahui bila terjadi perubahan pada model, perlu dilakukan migrasi, untuk membuat migrasi model, kita dapat jalankan perintah:
    ```
    python manage.py makemigrations
    ```
    lalu untuk menerapkan migrasi tersebut ke dalam basis data lokal, kita jalankan perintah:
    ```
    python manage.py migrate
    ```
    Sehingga perubahan model akan diketahui oleh Django.
    
- [x] **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**

  Buka file `views.py` pada aplikasi `main`, lalu impor fungsi `render` dari `django.shortcuts` untuk me-render tampilan HTML sesuai dengan data yang diberikan. Kemudian kita buat fungsi `show_main` yang menerima parameter `request`, fungsi ini akan melayani permintaan HTTP dan memberikan tampilan yang sesuai. Buat variabel `context` sebagai _dictionary_ yang berisi data yang akan dikirimkan ke tampilan, dalam tugas ini ada tiga data yaitu:
  * `app_name`: Data nama app
  * `name`: Data nama
  * `class`: Data kelas
  lalu tambahkan `return render(request, "main.html", context)` sehingga tampilan `main.html` akan ter-render dengan menggunakan fungsi `render` yang menggunakan parameter `context` sebagai data yang akan diteruskan ke tampilan sehingga penampilan dinamis.
      
- [x] **Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**
      
  Kita mengonfigurasi routing URL proyek stockio dengan menambahkan rute URL `urls.py` pada direktori proyek `stockio` yang akan kita hubungkan ke tampilan `main`. Impor fungsi `include` dari `django.urls`, fungsi ini akan mengimpor URL dari aplikasi lain (kasus ini aplikasi `main`) ke dalam file `urls.py` proyek stockio. Tambahkan rute URL `path('main/', include('main.urls'))` pada variabel `urlpatterns`, path URL `'main/'` akan diarahkan ke rute URL yang dibuat tadi pada file `urls.py` di aplikasi `main`. File `urls.py` pada aplikasi `main` bertugas untuk mengatur rute URL spesifik yang dibutuhkan oleh fitur-fitur aplikasi `main` sedangkan `urls.py` pada proyek stockio bertugas untuk mengarahkan rute URL proyek dan akan mengimpor rute URL dari file `urls.py` aplikasi-aplikasi bila dibutuhkan.
  
  Konfigurasikan routing URL aplikasi `main` dengan membuat file `urls.py` pada direktori `main`, file ini yang akan mengatur rute URL milik aplikasi `main`. Impor fungsi `path` dari `django.urls`, fungsi ini berguna untuk membuat URL. Impor juga fungsi `show_main` dari `main.views` untuk menampilkan tampilan ketika URL terkait diakses. Buat nama `app_name` untuk memberikan nama unik pada pola URL pada aplikasi. Gunakan fungsi `show_main` untuk menampilkan URL terkait ketika diakses dengan membuat variabel `urlpatterns` menjadi:
   ```
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```

- [x] **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

  Pastikan file proyek stockio sudah memiliki repositori di `GitHub` dengan nama `stockio`. Kita buka website Adaptable lalu pilih `Create New App` dan pilih opsi `Connect Git Repository` kemudian pilih repository `stockio`, pilih branch `main` lalu pilih `Python App Template` sebagai Deploy Template-nya, Gunakan Database Type `Postgre SQL` dan pilih python version sesuai dengan yang digunakan (`3.10`) dan mengisi start command dengan perintah `python manage.py migrate && gunicorn stockio.wsgi`. Masukkan nama aplikasi, yaitu `stockio`, nama ini juga akan menjadi nama domainnya, terakhir centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment.
</details>

<details>
<summary>2) Membuat bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</summary>


![image_2023-09-13_00-32-40](https://github.com/hrjuno/stockio/assets/121445072/15051235-d2df-44c4-a8a7-6ab2e94e95f8)

  Penjelasan:
  1. Client membuka browser untuk mengakses website, kemudian `Client (browser)` mengirimkan HTTP request ke URL tertentu dan ditangkap oleh `urls.py`
  2. URL Router mengarahkan alamat proyek sesuai permintaan client `urls.py`, dari sini diarahkan menuju fungsi yang berada di `views.py`
  3. Views `views.py` menyusun apa saja yang akan ditampilkan ke template `html`, data yang diproses diambil dari database yang telah disusun dengan ORM di dalam `models.py`
  4. Views `views.py` menyusun apa saja yang akan ditampilkan ke template `html`, data yang diproses diambil dari database yang telah disusun dengan ORM di dalam `models.py`
  5. Hasil render `HTML` oleh `views.py` akan menghasilkan response yang dikirim kembali ke `Client (browser)`, kemudian Client mendapatkan response dari web server
</details>

<details>
<summary>3) Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</summary>


  Virtual environment digunakan dalam pengembangan perangkat lunak, termasuk pengembangan aplikasi web berbasis Django, untuk beberapa alasan penting, seperti memungkinkan environment yang terisolasi untuk setiap proyek, menghindari konflik dependencies, memudahkan berbagi proyek dengan orang lain, memudahkan pengelolaan paket Python yang digunakan oleh proyek, membantu pengujian proyek dalam environment yang terisolasi, serta mencegah paket antar proyek tercampur dan mengurangi risiko masalah yang tidak diketahui.

  Meskipun kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, mengelola dependencies dan proyek-proyek Anda akan lebih rumit dan berpotensi tinggi menimbulkan masalah. Oleh karena itu, sangat disarankan untuk selalu menggunakan virtual environment dalam pengembangan Django atau proyek Python lainnya.
</details>

<details>
<summary>4) Apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya?</summary>


  MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi. Mereka memiliki konsep dasar yang serupa, yaitu memisahkan komponen aplikasi menjadi bagian-bagian yang berbeda untuk membantu pemahaman, pemeliharaan, dan pengujian. Namun, ada perbedaan penting dalam cara masing-masing pola ini diimplementasikan.
  
  * **MVC (Model-View-Controller)**:

      * Model: Mewakili data dan logika aplikasi.
      * View: Bertanggung jawab untuk tampilan grafis atau antarmuka pengguna.
      * Controller: Mengatur interaksi antara Model dan View serta mengatur alur aplikasi.

      **Perbedaan**:
    
      * MVC adalah pola arsitektur yang umum digunakan dalam pengembangan perangkat lunak tradisional, seperti aplikasi desktop.
      * Controller adalah inti dari MVC dan berfungsi sebagai penghubung antara Model dan View.

  * **MVT (Model-View-Template)**:
    
      * Model: Mewakili data dan logika aplikasi.
      * View: Menangani tampilan pengguna, tetapi dalam kerangka kerja Django, sebagian besar logika tampilan dikendalikan oleh Template.
      * Template: Bertanggung jawab untuk merender tampilan dan menggabungkan data dari Model.
    
      **Perbedaan**:
  
      * MVT adalah variasi dari MVC yang diterapkan secara khusus dalam kerangka kerja Django untuk pengembangan web.
      * Pada MVT, Template memiliki peran yang lebih besar dalam menangani tampilan dibandingkan dengan View.
    
  * **MVVM (Model-View-ViewModel)**:
    
      * Model: Mewakili data dan logika aplikasi.
      * View: Merupakan tampilan grafis yang dilihat oleh pengguna.
      * ViewModel: Bertanggung jawab untuk mengelola data yang akan ditampilkan di View dan berfungsi sebagai jembatan antara Model dan View.
    
      **Perbedaan**:
  
      * MVVM adalah pola arsitektur yang umum digunakan dalam pengembangan aplikasi berbasis pemrograman berorientasi objek, seperti aplikasi desktop dan aplikasi mobile.
      * ViewModel adalah inti dari MVVM dan berperan sebagai penghubung antara Model dan View dengan cara yang lebih terstruktur dan terkendali dibandingkan dengan Controller dalam MVC.
    
  Perbedaan utama antara ketiga pola ini adalah cara mereka mengelola tampilan dan koneksi antara Model dan View/Template/ViewModel. MVC adalah pola yang umum digunakan dalam pengembangan tradisional, MVT adalah varian dari MVC yang digunakan dalam kerangka kerja web Django, dan MVVM adalah pola yang sering digunakan dalam pengembangan aplikasi berbasis objek, terutama di lingkungan seperti aplikasi desktop atau mobile. Pemilihan pola tergantung pada jenis aplikasi dan kerangka kerja yang digunakan.
</details>

Referensi:
- https://pbp-fasilkom-ui.github.io/ganjil-2024/
- https://levelup.gitconnected.com/mvc-vs-mvp-vs-mvvm-35e0d4b933b4
- https://www.geeksforgeeks.org/python-virtual-environment/
