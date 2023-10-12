Nama           : Harjuno Abdullah

Kelas          : PBP C

Link Aplikasi  : [harjuno-abdullah-tugas.pbp.cs.ui.ac.id](harjuno-abdullah-tugas.pbp.cs.ui.ac.id)

---
# Tugas 6
<details>
<summary>1) Perbedaan antara asynchronous programming dengan synchronous programming</summary>



</details>

<details>
<summary>2) Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini</summary>



</details>

<details>
<summary>3) Penerapan asynchronous programming pada AJAX</summary>



</details>

<details>
<summary>4) Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan</summary>



</details>

<details>
<summary>5) Cara mengimplementasikan checklist tugas secara step-by-step</summary>



</details>

Referensi:
- https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-5
- 

---
# Tugas 5
<details>
<summary>1) Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya</summary>

1. **Element Selector (Tag Selector):**

    * Manfaat: Memilih semua elemen dengan tag yang spesifik
    * Waktu Penggunaan: Ketika ingin menerapkan gaya yang sama pada semua elemen dengan tag tertentu.

2. **Descendant Selector (Space):**
    
    * Manfaat: Memilih elemen yang merupakan anak atau keturunan dari elemen tertentu.
    * Waktu Penggunaan: Ketika ingin menerapkan gaya pada elemen yang berada di dalam elemen tertentu.

3. **ID Selector (#nama-id):**

    * Manfaat: Memilih elemen dengan ID yang spesifik.
    * Waktu Penggunaan: ketika ingin menerapkan gaya atau perilaku unik pada satu elemen tertentu.

4. **Class Selector (.nama-kelas):**

    * Manfaat: Memilih elemen berdasarkan kelas yang diberikan
    * Waktu Penggunaan: Ketika ingin menerapkan gaya yang sama pada beberapa elemen atau grup elemen.

5. **Universal Selector (*):**
    
    * Manfaat: Memilih semua elemen di halaman.
    * Waktu Penggunaan: Ketika mereset atau menetapkan gaya default untuk semua elemen di halaman.

6. **Adjacent Sibling Selector (+):**

    * Manfaat: Memilih elemen yang sejajar (saudara sejajar) dari elemen tertentu.
    * Waktu Penggunaan: Ketika ingin menerapkan gaya pada elemen yang berada tepat setelah elemen lain dari jenis yang sama.

7. **Pseudo-Class Selector (:pseudo-class):**

    * Manfaat: Memilih elemen berdasarkan keadaan atau perilaku tertentu (seperti :hover, :active, dsb.)
    * Waktu Penggunaan: Ketika ingin menerapkan gaya berdasarkan interaksi pengguna atau keadaan elemen.

</details>

<details>
<summary>2) HTML5 Tag yang saya ketahui</summary>

  * !DOCTYPE: Digunakan untuk mendefinisikan jenis dokumen HTML yang digunakan.
  * html: Tag ini menandai awal dan akhir dari dokumen HTML.
  * head: Berisi informasi terkait dokumen HTML, seperti meta informasi dan tautan ke stylesheet.
  * title: Digunakan di dalam untuk menentukan judul halaman web yang akan ditampilkan di jendela atau tab browser.
  * body: Menandai area utama dokumen yang berisi konten yang ditampilkan kepada pengguna.
  * h1, h2, ..., h6: Tag ini digunakan untuk menandai judul atau heading di halaman web, di mana h1 adalah yang tertinggi dan h6 adalah yang terendah.
  * p: Menandai paragraf dalam dokumen.
  * a: Membuat tautan ke halaman web lain atau alamat email.
  * img: Menampilkan gambar dalam dokumen HTML.
  * button: Digunakan untuk membuat tombol yang dapat di-klik oleh pengguna.
  * div: Menandai sebagian dokumen yang dapat digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML.
  * span: Sama seperti, tetapi digunakan untuk mengelompokkan elemen dalam baris atau sekelompok elemen dalam satu baris.
  * form: Digunakan untuk membuat formulir yang dapat mengirim data ke server.

</details>

<details>
<summary>3) Perbedaan antara margin dan padding</summary>

Margin dan padding adalah dua properti dalam CSS yang digunakan untuk mengatur tata letak elemen HTML dan mengendalikan ruang di sekitar elemen tersebut. Perbedaan utama antara margin dan padding adalah di mana mereka diterapkan dan bagaimana mereka memengaruhi tata letak elemen:

1. **Margin**

  * Margin adalah ruang di luar elemen, yang berarti ia memengaruhi jarak antara elemen tersebut dan elemen-elemen lain di sekitarnya.
  * Margin digunakan untuk mengatur jarak antara elemen dengan elemen-elemen lain di sekitarnya, sehingga memengaruhi tata letak elemen tersebut terhadap elemen-elemen lainnya.
  * Margin dapat digunakan untuk mengatur jarak vertikal dan horizontal, serta dapat memiliki nilai negatif jika ingin menggeser elemen ke atas atau ke kiri elemen yang berdekatan.

2. **Padding**

  * Padding adalah ruang di dalam elemen, yang berarti ia memengaruhi ruang antara batas elemen dan kontennya sendiri.
  * Padding digunakan untuk mengatur jarak antara konten elemen dan batas elemen tersebut, sehingga memengaruhi tampilan konten dalam elemen tersebut.
  * Padding juga dapat digunakan untuk mengatur jarak vertikal dan horizontal, tetapi tidak memengaruhi tata letak elemen terhadap elemen-elemen lain di sekitarnya.

</details>

<details>
<summary>4) Perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya</summary>

Bootstrap dan Tailwind CSS adalah dua alat yang membantu merancang tampilan situs web atau aplikasi dengan mudah. Berikut perbedaan dan situasi kapan sebaiknya menggunakan keduanya:

  1. **Cara Styling**

      * Bootstrap
        
        Bootstrap sudah memiliki komponen dengan gaya bawaan. Ini artinya, tampilan yang sudah ada dan bisa digunakan langsung, tetapi kadang-kadang sulit untuk mengubahnya tanpa penyesuaian khusus.

      * Tailwind CSS

        Tailwind CSS adalah framework yang berbasis class utilitas. Dengan Tailwind, Anda lebih bebas menentukan tampilan elemen Anda dengan menggabungkan class utilitas.

  2. **Kustomisasi**

      * Bootstrap

        Meskipun Bootstrap menyediakan tema yang bisa disesuaikan, seringkali Anda perlu menulis CSS tambahan untuk melakukan penyesuaian styling lebih mendalam.

      * Tailwind CSS

        Tailwind dirancang untuk kustomisasi yang mudah. Anda bisa mengganti styling dengan mengedit berkas konfigurasi Tailwind atau menambahkan class utilitas kustom.

  3. **Ukuran Berkas**

      * Bootstrap

        Bootstrap cenderung punya ukuran berkas yang lebih besar karena memiliki banyak komponen yang mungkin tidak semua Anda butuhkan.

      * Tailwind CSS

        Tailwind CSS biasanya lebih ringan karena hanya menyertakan class utilitas yang Anda gunakan.

  4. **Kesulitan**

      * Bootstrap

        Bootstrap bisa lebih mudah digunakan jika Anda ingin cepat membuat tampilan yang bagus tanpa harus menulis banyak kode kustom.

      * Tailwind CSS

        Tailwind mungkin agak sulit jika Anda belum terbiasa dengan class utilitas, tetapi memberi Anda lebih banyak kendali dan fleksibilitas dalam merancang tampilan.

</details>

<details>
<summary>5) Cara mengimplementasikan checklist tugas secara step-by-step</summary>

- [x] **Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin**
      
      Sebelum melakukan desain pada HTML, perlu menambahkan link CSS framework dalam case ini adalah Bootstrap dan Java Scriptke dalam `templates/base.html` dan menambahkan tag `<meta name="viewport">` . Untuk menambahkannya bisa dengan menambahkan:

          ```
          <head>
              {% block meta %}
                  ...
              {% endblock meta %}

              <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

              <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>

              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
          </head>
          
          ```
      Pada halaman login, register, dan tambah inventori, desain yang saya buat kurang lebih sama, saya menggunakan inline css dengan memanggil `<style>` pada bagian atas html serta dipadukan dengan framework bootstrap. Saya menggunakan inline CSS karena menurut saya ini yang mudah disetup dan digunakan untuk pemula. Berikut adalah inline CSS yang saya tambahkan (Sebagai contoh saya menampilkan inline CSS pada halaman login)

        ```
        <style>
          body {
              background-image: url('https://cdn.cloudflare.steamstatic.com/steam/apps/865610/ss_e950f52ee4d972c135d1acbd70def74e9eb497b9.1920x1080.jpg?t=1692006226');
              background-size: cover;
              background-repeat: no-repeat;
              background-attachment: fixed;
              margin: 12px;
              padding: 12px;
              display: flex;
              justify-content: center;
              align-items: center;
              min-height: 100vh;
              position: relative; 
          }

          .logo {
              position: absolute;
              top: 12px;
              left: 22px;
              z-index: 2;
              font-size: 36px;
              font-family: 'Poppins', sans-serif;
              color: rgb(255, 179, 0);
          }

          .showcase h1,
          .showcase label,
          .showcase a {
              font-family: 'Helvetica', sans-serif;
              color: rgb(255, 255, 255);
          }

          .showcase a {
              font-family: 'Helvetica', sans-serif;
              color: #ffffff;
              text-decoration: underline; 
          }

          .showcase-bottom{
              font-family: 'Helvetica', sans-serif;
              color:rgb(164, 164, 164);
          }

          .showcase {
              text-align: center;
              background-color: #363636ac;
              border-radius: 16px;
              padding: 50px;
              width: 400px;
              text-align: center;
              padding-top: 30px;
              backdrop-filter: blur(6px);
          }

          .showcase form {
              font-family: 'Helvetica', sans-serif;
          }

          .showcase input[type="text"],
          .showcase input[type="password"] {
              font-family: 'Helvetica', sans-serif;
              color: black; 
              background-color: white;
          }

          .showcase .form-group {
          display: flex;
          flex-direction: column;
          margin-bottom: 24px;
          }

          .showcase .form-group label {
              font-family: 'Helvetica', sans-serif;
              margin-bottom: 8px;
              text-align: left; 
          }

          .showcase .form-control {
          font-family: 'Helvetica', sans-serif;
          width: 100%;
          padding: 12px; 
          border-radius: 6px;
          box-sizing: border-box;
          margin-bottom: 12px;
          font-size: 16px; 
          background-color: white;
          }

          .showcase .login-button {
              font-size: 16px;
              display: inline-flex;
              height: 56px;
              padding: 8px 48px;
              justify-content: center;
              align-items: center;
              gap: 16px;
              border-radius: 8px;
              background: var(--primary-blue, rgb(255, 179, 0));
              color: #ffffff;
              text-decoration: none;
              border: none;
              cursor: pointer;
          }

          .text-title{
              text-align: left; 
              font-size:35px;
              font-weight: 600;
              padding-bottom: 19px;
              padding-top: 15px;
          }
        </style>

        ```
      
 - [x] **Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card**

      Dalam mendesain halaman daftar inventori, kurang lebih metode yang saya gunakan sama seperti ketika mendesain halaman login, register, dan tambah inventori. Berikut inline CSS pada file main.html saya

      ```
      <style>
        body {  
            background-color: #f4f4f4;
            font-family: Helvetica, sans-serif;
        }

        h1 {
            color: #160323;
            font-size: 36px;
        }

        h2 {
            color: #333;
            font-size: 24px;
        }

        h4 {
            color: #555;
            font-size: 18px;
        }

        p {
            color: #777;
            font-size: 16px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table, th, td {
            border: 1px solid #888888;
        }

        th, td {
            padding: 12px;
            text-align: left;
        }

        table tr:last-child td {
            background-color: rgb(84, 84, 84);
            color: #ffffff;
        }

        button {
            background-color: rgb(227, 159, 0);
            color: #fff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: rgb(255, 198, 65);
        }

        a {
            text-decoration: none;
            color: rgb(227, 159, 0);
        }

        a:hover {
            text-decoration: underline;
        }

        .navbar {
        background-color: #313131;
        height: 4rem;
        align-content: center;
        margin-bottom: 4rem;
        }

        .navbar-button-logout {
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }

        .navbar-brand {
            font-family: 'Helvetica', sans-serif;
            font-weight: 700;
            text-align: center;
            color: rgb(255, 179, 0);
            padding-left: 1rem;
        }
      </style>
      
      ```

 - [x] **Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS**

      Untuk menambahkan penanda berbeda di akhir tabel, saya menambahkan CSS untuk last child pada `tr` dengan kode berikut:

          ```

          table tr:last-child td {
              background-color: rgb(84, 84, 84);
              color: #ffffff;
          }

          ```

</details>

Referensi:
- https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-4
- https://blog.hubspot.com/website/css-margin-vs-padding
- https://www.javatpoint.com/html-tags

---
# Tugas 4
<details>
<summary>1) Pengertian Django UserCreationForm, dan kelebihan dan kekurangannya</summary>

  UserCreationForm adalah sebuah formulir yang disediakan oleh Django, sebuah framework web Python yang populer, untuk membuat formulir pendaftaran pengguna (user registration form) dengan mudah. Formulir ini digunakan untuk mengumpulkan informasi yang diperlukan saat seorang pengguna baru mendaftar di situs web atau aplikasi Django.

  **Kelebihan UserCreationForm:**
   
   1. Mudah Digunakan
     
      UserCreationForm sudah siap pakai dan mudah digunakan. Developer hanya perlu mengimpor dan menggunakannya dalam proyek Django tanpa perlu menulis kode formulir dari awal.
      
   2. Validasi Otomatis
     
      Form ini memiliki validasi otomatis untuk memastikan bahwa pengguna mengisi semua kolom yang diperlukan dengan benar, seperti alamat email yang valid dan kata sandi yang memenuhi kriteria keamanan.
      
   3. Customizable
   
      Developer dapat dengan mudah menyesuaikan UserCreationForm sesuai dengan kebutuhan proyek dengan menambahkan atau menghapus bidang formulir atau mengganti pesan kesalahan yang ditampilkan kepada pengguna.
   
   **Kekurangan UserCreationForm:**
   
  1. Kurangnya Fleksibilitas
     
      Meskipun mudah digunakan, dalam beberapa kasus, developer mungkin memerlukan formulir pendaftaran pengguna yang sangat kustom. Dalam situasi ini, developer perlu menulis formulir sendiri daripada mengandalkan UserCreationForm.
   
  2. Tidak Memungkinkan Pendaftaran Eksternal
     
     Jika developer ingin mengintegrasikan pendaftaran pengguna melalui penyedia eksternal (misalnya, login dengan Google atau Facebook), developer perlu menulis kode tambahan untuk mengimplementasikannya.
   
   3. Tidak Memungkinkan Pendaftaran secara Anonim
      
      UserCreationForm dirancang untuk pendaftaran pengguna yang terautentikasi. Jika developer membutuhkan pendaftaran secara anonim (misalnya, untuk pengguna yang belum memiliki akun), developer perlu membuat formulir tambahan atau memodifikasi form ini secara ekstensif.
</details>

<details>
<summary>2) Perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting</summary>

  Authentication dan authorization adalah dua konsep yang penting dalam menjaga keamanan informasi dan akses ke dalam sistem. Meskipun keduanya berhubungan erat, keduanya memiliki beberapa perbedaan, seperti:

  1. **Authentication (Autentikasi)**

      * Authentication adalah proses verifikasi identitas pengguna atau entitas yang mencoba mengakses ke dalam sistem
      * Tujuan utama autentikasi adalah untuk memastikan bahwa pengguna atau entitas yang mengakses sistem adalah mereka yang telah diketahui identitasnya atau telah menjadi bagian dari sistem
      * Autentikasi biasanya melibatkan penggunaan kombinasi nama pengguna dan kata sandi, atau metode lain untuk membuktikan identitas

  2. **Authorization (Otorisasi)**

      * Authorization adalah proses yang mengatur dan mengontrol akses pengguna atau entitas yang sudah terotentikasi ke sistem atau layanan tertentu
      * Tujuan utama otorisasi adalah untuk menentukan apa yang diizinkan atau tidak diizinkan oleh pengguna atau entitas yang telah terotentikasi
      * Otorisasi melibatkan definisi aturan atau kebijakan yang menentukan tingkat akses atau izin yang diberikan kepada pengguna atau entitas, seperti hak akses baca-tulis, hak akses hanya baca, dan sebagainya

  Kesimpulannya, autentikasi adalah langkah pertama dalam mengamankan akses ke sistem dengan memeriksa identitas pengguna atau entitas, sementara otorisasi adalah langkah kedua yang mengontrol apa yang dapat dilakukan oleh pengguna atau entitas yang sudah terotentikasi. Keduanya bekerja bersama untuk memastikan bahwa hanya pengguna yang sah dan diizinkan yang dapat mengakses sumber daya atau layanan yang dimaksud dalam sistem.

</details>

<details>
<summary>3) Definisi cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna</summary>

Cookies adalah sejumlah kecil data yang disimpan oleh server web di komputer pengguna melalui peramban (browser) pengguna saat berinteraksi dengan sebuah situs web. Cookies digunakan dalam konteks aplikasi web untuk menyimpan informasi tertentu yang dapat diakses kembali oleh server web ketika pengguna kembali mengunjungi situs tersebut. Cookies memiliki beberapa fungsi utama dalam aplikasi web, termasuk:

1. **Manajemen Sesi**

    Cookies sering digunakan untuk mengidentifikasi sesi pengguna. Ketika seorang pengguna masuk ke dalam situs web, server web akan membuat cookie yang berisi identifikasi unik untuk sesi tersebut. Dengan demikian, server dapat mempertahankan konteks sesi pengguna selama kunjungan berlangsung, yang memungkinkan pengguna untuk tetap masuk atau mempertahankan data lainnya seperti keranjang belanja.

2. **Penyimpanan Preferensi Pengguna**

    Cookies dapat digunakan untuk menyimpan preferensi pengguna, seperti bahasa yang dipilih atau tema tampilan yang diinginkan. Ini memungkinkan situs web untuk menyajikan pengalaman yang disesuaikan dengan preferensi masing-masing pengguna.

3. **Pelacakan Aktivitas Pengguna**

    Cookies juga sering digunakan untuk pelacakan aktivitas pengguna, seperti halaman yang dikunjungi atau item yang dilihat. Ini berguna untuk analisis penggunaan situs web dan pemasaran.

4. **Autentikasi**

    Cookies dapat digunakan untuk mengingat informasi otentikasi pengguna, seperti detail masuk pengguna, sehingga pengguna tidak perlu masuk kembali setiap kali mereka mengunjungi situs.

Django, sebagai framework web Python, menyediakan cara yang nyaman untuk mengelola data sesi pengguna menggunakan cookies. Django menyediakan modul `django.contrib.sessions.middleware.SessionMiddleware` yang mengatur manajemen sesi pengguna secara otomatis. Berikut adalah cara Django menggunakan cookies untuk mengelola data sesi pengguna:

1. **Pengaturan Sesi**

    Pengguna dapat mengonfigurasi pengaturan sesi di dalam berkas settings.py proyek Django. Pengguna dapat mengatur penyimpanan sesi (defaultnya adalah dalam database), waktu kadaluwarsa sesi, dan konfigurasi lainnya terkait sesi.

2. **Membaca dan Menyimpan Data Sesi**

    Django menyediakan API yang memudahkan pengguna untuk menyimpan dan mengakses data sesi pengguna. Pengguna dapat menyimpan data ke dalam sesi dengan mudah, dan data ini akan dienkripsi dan disimpan dalam cookie pada sisi pengguna.

3. **Middleware**

    Middleware sesi diaktifkan dengan menambahkan SessionMiddleware ke dalam daftar middleware di pengaturan Django. Middleware ini akan mengelola cookies dan data sesi secara otomatis.

</details>

<details>
<summary>4) Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?</summary>

Penggunaan cookies dalam pengembangan web memiliki risiko potensial yang harus diwaspadai, dan keamanannya sangat tergantung pada bagaimana cookies digunakan dan dikonfigurasi dalam aplikasi website pengguna. Berikut adalah beberapa risiko potensial terkait dengan penggunaan cookies:

   1. **Cross-Site Scripting (XSS)**

         Penyerangan XSS dapat memungkinkan penyerang menyuntikkan kode berbahaya ke dalam halaman web yang akan diakses oleh pengguna lain. Kode berbahaya ini dapat digunakan untuk mencuri cookies pengguna. Mencegah XSS adalah penting untuk melindungi cookies dan data sensitif lainnya.

   2. **Privasi Pengguna**

         Cookies dapat digunakan untuk melacak aktivitas pengguna secara online, yang dapat menciptakan masalah privasi. Oleh karena itu, penting untuk memiliki kebijakan privasi yang jelas dan memberikan pengguna opsi untuk mengontrol cookies.

   3. **Cookies Tampering**

         Pengguna dapat mencoba memodifikasi nilai cookies yang tersimpan di perangkat mereka untuk mengakses atau memanipulasi data sesi atau informasi lain yang disimpan dalam cookies. Oleh karena itu, penting untuk mengamankan cookies dan menerapkan tanda tangan (signing) pada cookies.

   4. **Cross-Site Request Forgery (CSRF)**

         Penyerangan CSRF dapat memaksa pengguna yang sudah diautentikasi untuk melakukan tindakan tertentu tanpa izin mereka, seperti mengirim permintaan yang menggunakan cookies mereka. Menggunakan mekanisme anti-CSRF adalah penting untuk melindungi cookies dari penyerangan ini.

   5. **Cookie Sniffing**

         Penyadap (sniffer) di jaringan dapat mencoba mencuri informasi cookies saat dikirimkan antara perangkat pengguna dan server. Untuk mengatasi ini, cookies harus dienkripsi jika berisi informasi sensitif.

</details>

<details>
<summary>5) Cara mengimplementasikan checklist tugas secara step-by-step</summary>

- [x] **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar**

  1. **Registrasi**
    
    Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `register` dan memiliki parameter `request`. Lalu impor `redirect`, `UserCreationForm`, dan `messages`. Isi dari fungsi `register` adalah:
    ```
    def register(request):
      form = UserCreationForm()

      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)
    ```
    `form = UserCreationForm(request.POST)` untuk membuat variabel `form` yang dimana ia adalah `UserCreationForm` lalu kita masukkan QueryDict sesuai input dari user pada `request.POST`. `form.is_valid()` berguna untuk melakukan validasi pada input form. `form.save()` supaya data dari form dapat tersimpan. User dapat mengetahui apabila berhasil me-register dengan melihat pesan pada web karena kita menggunakan `messages.success(request, 'Your account has been successfully created!')`. Setelah user berhasil mendaftar, user akan kembali dari halaman register, jadi, kita menambahkan kode `return redirect('main:show_main')`.
    Halaman register akan kita buat dengan file `register.html` yang ada di folder `main/templates` dengan isi:
    ```
    {% extends 'base.html' %}
    
    {% block meta %}
        <title>Register</title>
    {% endblock meta %}
    
    {% block content %}  
    
    <div class = "login">
    
          <h1>Register</h1>  
    
            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>
    
        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}
    
    </div>  
    
    {% endblock content %}
    ```
    Tambahkan path url milik halaman register ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `register` dari `views.py` dan tambahkan `path('register/', register, name='register')` pada variabel `urlpatterns`.
    
    
  2. **Login**

    Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `login_user` yang menerima parameter `request`. Lalu impor `authenticate` dan `login`. Isi dari fungsi `login` adalah:
    ```
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```
    `authenticate(request, username=username, password=password` berguna untuk melakukan autentikasi user dengan menggunakan username dan password yang diterima dari `request` yang dikirim user saat ingin login.
    Halaman login akan kita buat dengan file `login.html` yang ada di folder `main/templates` dengan isi:
    ```
    {% extends 'base.html' %}
    
    {% block meta %}
        <title>Login</title>
    {% endblock meta %}
    
    {% block content %}

    <div class = "login">
    
        <h1>Login</h1>
    
        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>
    
                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>
    
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
    
    </div>

    {% endblock content %}
    ```
    Tambahkan path url milik halaman login ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `login` dari `views.py` dan tambahkan `path('login/', login_user, name='login')` pada variabel `urlpatterns`.

  3. **Logout**
    
    Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `logout_user` yang menerima parameter `request`. Lalu impor `logout`. Isi dari fungsi `logout_user` adalah:
    ```
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
    `logout(request)` akan menghapus sesi pengguna yang saat ini sudah masuk. Lalu user akan kembali ke halaman login dengan `return redirect('main:login')`.
    Tambahkan:
    ```
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```
    Setelah hyperlink tag untuk Add New Product yang ada di file `main.html`.
    Tambahkan path url milik halaman logout ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `logout_user` dari `views.py` dan tambahkan `path('logout/', logout_user, name='logout')` pada variabel `urlpatterns`.

- [x] **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal**

  Pada halaman pertama login terdapat tombol `Register Now` untuk membuat akun baru. Kita dapat membuat akun  baru dengan memasukkan username dan password yang sesuai ketentuan dan meng-click tombol daftar. Setelah membuat akun kita bisa login pada halaman pertama tadi dan memasukkan username dan password dari akun baru kita. setelah login, kita dapat menambah produk sesuai keinginan.

- [x] **Menghubungkan model Item dengan User**

  Buka `models.py` yang ada di direktori `main` lalu impor `User` dari `django.contrib.auth.models`. Pada model `Product` yang ada tambahkan kode:

    ```
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```

  Hal ini dilakukan supaya kita menghubungkan satu produk dengan satu user menggunakan relationship, jadi sebuah produk pasti terasosiasi dengan user.
  Buka `viwes.py` yang ada di direktori `main` dan modifikasi fungsi `create_product` menjadi:

    ```
    def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
      product = form.save(commit=False)
      product.user = request.user
      product.save()
      return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```

  `commit=False` berfungsi supaya Django tidak langsung menyimpan objek yang dibuat dari form ke database sehingga kita dapat memodifikasi objek tersebut dahulu. Kita mengisi field `user` dengan objek `User` dari return nilai `request.user` yang sudah terautentikasi untuk menandakan bahwa objek tersebut milik pengguna yang sedang login.
  Ubah fungsi `show_main` menjadi:

    ```
    def show_main(request):
        products = Product.objects.filter(user=request.user)
    
        context = {
            'name': request.user.username,
        ...
    ...
    ```

  Hal ini dilakukan agar objek `Product` yang terasosiasi dengan user yang sedang login dapat ditampilkan. Kita menyaring seluruh objek dan hanya mengambil `Product` yang field `user` terisi dengan objek `User` yang sama dengan user yang sedang login. Untuk menampilkan username user yang login pada halaman main kita menggunakan `request.user.username`.
  Kita lakukan migrasi model dengan `python manage.py makemigration` dan muncul error, untuk mengatasinya pilih 1 supaya kita menetapkan default value untuk field user pada semua row yang dibuat pada di basis data, ketik angka 1 untuk menetapkan user dengan ID 1 (user yang baru kita buat tadi) pada model yang ada. Lakukan `python manage.py migrate` untuk mengaplikasikan migrasi.

- [x] **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi**

  Buka file `views.py` yang ada di direktori `main` dan impor `HttpResponseRedirect`, `reverse`, dan `datetime`. Kita tambahkan fungsi untuk menambahkan cookie yang bernama `last_login` pada fungsi `login_user`, fungsi `last_login` digunakan untuk mengetahui kapan terakhir kali user login. Cara ini dilakukan dengan mengganti kode yang ada pada conditional `if user is not None` menjadi:

   ```
   ...
   if user is not None:
       login(request, user)
       response = HttpResponseRedirect(reverse("main:show_main")) 
       response.set_cookie('last_login', str(datetime.datetime.now()))
       return response
   ...
   ```

  `login(request, user)` berguna supaya logint terlebih dahulu. Untuk membuat response, kita menggunakan variabel `response` dan mengisinya dengan `HttpResponseRedirect(reverse("main:show_main"))`. `response.setcookie('last_login', str(datetime.datetime.now()))` berfungsi untuk membuat cookie `last_login` dan menambahkannya ke response tadi.
  Pada fungsi `show_main` tambahkan `'last_login': request.COOKIES['last_login']` pada variabel `context` supaya kita bisa menambahkan informasi cookie last_login pada response yang akan ditampilkan di web `main.html`.
  Untuk menghapus cookie `last_login` ketika user `logout` kita modifikasi code `logout_user` menjadi:

   ```
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   ```
  Lalu pada `main.html` tambahkan:
   ```
   ...
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ...
   ```
  Untuk menampilkan data last login.

</details>

Referensi:
- https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-3
- https://www-javatpoint-com.translate.goog/django-usercreationform?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc
- https://diginews.id/apa-perbedaan-antara-otentikasi-dan-otorisasi/
- https://www.niagahoster.co.id/blog/cookies-adalah/

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

  Meskipun kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, mengelola dependencies dan proyek-proyek akan lebih rumit dan berpotensi tinggi menimbulkan masalah. Oleh karena itu, sangat disarankan untuk selalu menggunakan virtual environment dalam pengembangan Django atau proyek Python lainnya.
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
