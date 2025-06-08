# Visualisasi Rumah 3D dengan Plotly

Repositori ini berisi kode Python untuk membuat model 3D sederhana sebuah rumah menggunakan library Plotly dan manipulasi koordinat 3D dasar.

## Deskripsi

Kode ini membangun model 3D sebuah rumah sederhana dengan komponen-komponen utama:

- Dinding kiri (persegi)
- Dinding kanan (persegi panjang)
- Dinding depan dan belakang (persegi panjang)
- Atap segitiga depan dan belakang
- Atap miring kiri dan kanan (persegi panjang)
- Lantai bawah (persegi panjang)

Model dibentuk dari kumpulan titik koordinat 3D yang kemudian dimanipulasi dengan fungsi transformasi seperti translasi, skala, dan rotasi. Hasil akhirnya divisualisasikan menggunakan `go.Mesh3d` dari Plotly dengan pewarnaan yang berbeda untuk tiap bagian.

## Cara Kerja Kode

1. **Fungsi Transformasi**  
   Kode memiliki tiga fungsi transformasi utama untuk memanipulasi koordinat titik:
   - `translate(points, dx, dy, dz)`: Menggeser titik sepanjang sumbu x, y, dan z.
   - `scale(points, sx, sy, sz)`: Mengubah skala titik pada masing-masing sumbu.
   - `rotate_z(points, angle_deg)`: Merotasi titik terhadap sumbu z sebesar sudut tertentu (derajat).

2. **Definisi Bentuk Geometri**  
   Titik-titik koordinat dinding, atap, dan lantai didefinisikan dalam bentuk list 3D.

3. **Penggabungan dan Triangulasi**  
   Semua bentuk digabungkan dan dilakukan triangulasi manual untuk membentuk mesh 3D yang bisa divisualisasikan.

4. **Visualisasi**  
   Menggunakan `plotly.graph_objects.Mesh3d` untuk menggambar model 3D dengan warna dan opacity yang telah ditentukan.

5. **Output**  
   Visualisasi ditampilkan di browser dan juga disimpan dalam file `rumah3d.html`.

## Prasyarat

- Python 3.x
- Library `plotly` dan `numpy`  
  Instalasi:  
  ```bash
  pip install plotly numpy
