LAPORAN ANALISA
PERBANDINGAN OPERATOR ROBERTS DAN SOBEL UNTUK DETEKSI TEPI

Nama: Yulinda Fitri
Kelas: TI23E
Mata Kuliah: Pengolahan Citra Digital

1. PENDAHULUAN
1.1 Latar Belakang
Deteksi tepi merupakan teknik fundamental dalam pengolahan citra digital yang digunakan untuk mengidentifikasi batas objek dalam sebuah gambar. Dalam tugas ini, saya mengimplementasikan dan membandingkan dua operator klasik: Operator Roberts (1965) dan Operator Sobel (1968).
1.2 Tujuan
•	Mengimplementasikan Operator Roberts dan Sobel menggunakan Python dengan library imageio, numpy, dan matplotlib
•	Membandingkan hasil deteksi tepi kedua operator
•	Menganalisis kelebihan dan kekurangan masing-masing operator
1.3 Ruang Lingkup
•	Implementasi manual (from scratch) tanpa menggunakan OpenCV
•	Testing menggunakan citra foto personal beresolusi tinggi
•	Analisis kuantitatif dan kualitatif

2. LANDASAN TEORI
2.1 Operator Roberts
Operator Roberts menggunakan kernel berukuran 2×2 untuk menghitung gradien diagonal.
Kernel:
Gx = | 1   0 |        Gy = | 0   1 |
     | 0  -1 |             |-1   0 |
Karakteristik:
•	Kernel sangat kecil (2×2)
•	Mendeteksi tepi diagonal (45° dan -45°)
•	Komputasi cepat
•	Sensitif terhadap noise
2.2 Operator Sobel
Operator Sobel menggunakan kernel berukuran 3×3 dengan efek smoothing built-in.
Kernel:
Gx = |-1  0  1|        Gy = |-1 -2 -1|
     |-2  0  2|             | 0  0  0|
     |-1  0  1|             | 1  2  1|
Karakteristik:
•	Kernel lebih besar (3×3)
•	Mendeteksi tepi horizontal dan vertikal
•	Memiliki smoothing effect
•	Lebih robust terhadap noise
2.3 Formula Magnitude
Kedua operator menghitung magnitude gradien dengan rumus:
G = √(Gx² + Gy²)

3. METODOLOGI
3.1 Tools dan Library
•	Python 3.11
•	imageio v2 - untuk membaca citra
•	numpy - untuk operasi array dan konvolusi
•	matplotlib - untuk visualisasi
3.2 Data Input
•	File: IMG_5890.JPG
•	Dimensi: 3456 × 5184 piksel
•	Ukuran: 17.9 Megapixels
•	Tipe: Citra berwarna (dikonversi ke grayscale)
•	Format: JPG
3.3 Prosedur
1.	Baca citra dan konversi ke grayscale
2.	Implementasi konvolusi manual untuk Roberts
3.	Implementasi konvolusi manual untuk Sobel
4.	Hitung magnitude gradien
5.	Normalisasi hasil ke range 0-255
6.	Analisis dan visualisasi hasil

4. HASIL DAN PEMBAHASAN
4.1 Output Program
======================================================================
   PROGRAM PERBANDINGAN OPERATOR ROBERTS DAN SOBEL
======================================================================

📂 Membaca citra dari: IMG_5890.JPG
✓ Berhasil membaca citra
  - Dimensi: 3456 x 5184 piksel
  - Tipe data: float32

⚙️  Memproses Operator Roberts...
✓ Selesai dalam 917.1967 detik

⚙️  Memproses Operator Sobel...
✓ Selesai dalam 732.9441 detik
4.2 Analisis Kuantitatif
4.2.1 Waktu Pemrosesan
Operator	Waktu (detik)	Waktu (menit)	Keterangan
Roberts	917.20	~15.3 menit	Lebih lambat
Sobel	732.94	~12.2 menit	25.14% lebih cepat ✅
Pembahasan:
Hasil ini bertentangan dengan teori yang menyatakan Roberts seharusnya lebih cepat karena kernel lebih kecil (2×2 vs 3×3).
Mengapa Sobel lebih cepat?
1.	Ukuran citra sangat besar (17.9 MP) - overhead loop iteration hampir sama
2.	Cache efficiency - operasi Sobel yang terstruktur lebih cache-friendly
3.	Memory access pattern - Sobel mungkin lebih optimal dalam akses memori
4.	Python implementation - nested loop performance tidak selalu proporsional dengan kernel size
Kesimpulan: Pada citra beresolusi tinggi, perbedaan kecepatan tidak hanya ditentukan oleh ukuran kernel, tetapi juga oleh implementasi dan karakteristik hardware.
4.2.2 Statistik Intensitas Tepi
Metrik	Roberts	Sobel	Analisis
Mean Intensity	3.75	6.10	Sobel 62.7% lebih tinggi
Std Deviation	7.23	11.44	Sobel 58.2% lebih tinggi
Min Value	0	0	Sama
Max Value	255	255	Sama
Pembahasan:
•	Roberts (mean 3.75): Intensitas sangat rendah menunjukkan deteksi tepi minimal dan sangat selektif
•	Sobel (mean 6.10): Intensitas lebih tinggi menunjukkan deteksi tepi lebih kuat dan jelas
•	Standard deviation Sobel lebih besar: Menunjukkan variasi intensitas lebih tinggi, artinya ada lebih banyak gradien dengan intensitas berbeda-beda
Kesimpulan: Sobel menghasilkan tepi yang lebih jelas dan kontras dibanding Roberts.
4.2.3 Jumlah Piksel Tepi (Threshold > 50)
Operator	Jumlah Piksel	Persentase
Roberts	47,085	0.26% dari total
Sobel	227,207	1.27% dari total
Selisih	180,122	79.28%
Pembahasan:
Perbedaan sangat signifikan! Sobel mendeteksi hampir 5 kali lebih banyak piksel sebagai tepi.
Analisis mendalam:
1.	Roberts terlalu selektif - hanya mendeteksi 0.26% piksel sebagai tepi
2.	Sobel lebih komprehensif - mendeteksi 1.27% piksel sebagai tepi
3.	79.28% perbedaan menunjukkan karakteristik yang sangat berbeda
Mengapa perbedaan begitu besar?
•	Kernel size: Sobel (3×3) melihat area lebih luas, menangkap lebih banyak gradien
•	Smoothing effect: Sobel punya weighted averaging yang membuat gradien halus tetap terdeteksi
•	Roberts focus diagonal: Banyak tepi horizontal/vertikal missed
•	Karakteristik foto: Foto natural punya banyak gradien halus yang hanya tertangkap Sobel
Kesimpulan: Untuk foto natural dengan detail kompleks, Sobel jauh superior dalam menangkap informasi tepi.
4.2.4 Similarity Metrics
Metrik	Nilai	Interpretasi
Mean Absolute Difference	3.05	Perbedaan kecil per piksel
Correlation Coefficient	0.8578	Korelasi tinggi (85.78%)
MSE	46.79	Error relatif rendah
PSNR	31.43 dB	Kualitas acceptable
Pembahasan:
Meskipun jumlah piksel tepi sangat berbeda, correlation coefficient 0.8578 menunjukkan kedua operator setuju pada lokasi tepi utama (85.78%).
Interpretasi:
•	Tepi utama konsisten - outline objek terdeteksi sama
•	Detail berbeda - perbedaan terbesar di gradien halus
•	PSNR 31.43 dB - dalam range normal untuk edge comparison
•	MAD 3.05 - rata-rata perbedaan hanya 3 intensitas per piksel
Kesimpulan: Kedua operator mengidentifikasi tepi utama dengan konsisten, tetapi berbeda dalam mendeteksi detail halus.
4.3 Analisis Kualitatif (Visual)
Berdasarkan visualisasi 12 panel yang dihasilkan:
4.3.1 Gradien X dan Y
Roberts:
•	Gradien sangat tipis seperti garis pensil
•	Banyak area kosong (hitam)
•	Detail halus tidak terlihat
•	Fokus pada kontras diagonal yang tinggi
Sobel:
•	Gradien lebih tebal dan jelas
•	Area tepi lebih terisi
•	Tekstur dan pola terdeteksi
•	Menangkap berbagai orientasi dengan baik
4.3.2 Hasil Akhir (Magnitude)
Roberts:
✗ Sangat minimalis
✗ Hanya outline utama
✗ Kehilangan banyak informasi
✗ Seperti sketsa line art sederhana
Sobel:
✓ Lengkap dan informatif
✓ Detail dan tekstur terlihat
✓ Lebih realistis
✓ Siap untuk analisis lanjutan
4.3.3 Histogram Distribusi
Roberts:
•	Puncak ekstrem di intensitas 0-10
•	Distribusi sangat sempit
•	Hampir tidak ada variasi
Sobel:
•	Distribusi lebih merata
•	Rentang intensitas lebih luas
•	Menunjukkan keberagaman tepi
4.3.4 Difference Map
Peta perbedaan menunjukkan:
•	Area dengan perbedaan tinggi: Tekstur halus, gradien rendah
•	Area dengan perbedaan rendah: Tepi tajam, outline utama
•	Pola: Perbedaan merata di seluruh citra, bukan terlokalisasi

5. PEMBAHASAN MENDALAM
5.1 Mengapa Roberts "Gagal" pada Citra Ini?
1. Kernel Terlalu Kecil
•	Kernel 2×2 hanya melihat 4 piksel sekaligus
•	Kehilangan informasi konteks sekitar
•	Tidak cukup untuk foto beresolusi tinggi (17.9 MP)
2. Tidak Ada Smoothing
•	Foto natural selalu punya noise
•	Roberts langsung detect tanpa filtering
•	Hasilnya: noise diabaikan TAPI detail juga hilang
3. Fokus Diagonal
•	Roberts optimal untuk tepi 45° dan -45°
•	Foto punya tepi di berbagai arah
•	Banyak tepi horizontal/vertikal terlewat
4. Threshold Terlalu Strict
•	Untuk mencapai intensitas >50, butuh kontras sangat tinggi
•	Gradien halus (10-40) tidak terhitung
•	Informasi penting hilang
5.2 Mengapa Sobel Unggul?
1. Kernel Size Optimal
•	3×3 = sweet spot antara detail dan konteks
•	9 piksel memberikan informasi lebih lengkap
•	Masih cukup cepat untuk diproses
2. Weighted Smoothing
•	Koefisien [1, 2, 1] memberikan averaging cerdas
•	Center pixel diberi bobot lebih (×2)
•	Noise diredam, detail penting dipertahankan
3. Horizontal & Vertical Focus
•	Struktur dalam foto umumnya H&V
•	Architecture, people, objects = banyak H&V edges
•	Universal untuk berbagai objek
4. Better Gradient Capture
•	Mampu mendeteksi gradien halus (low contrast)
•	Tidak hanya hitam-putih, tapi juga abu-abu
•	Lebih informatif untuk analisis lanjut
5.3 Temuan Menarik
Plot Twist: Sobel Lebih Cepat!
Ini adalah temuan paling menarik dari eksperimen ini:
Expected (dari teori):
•	Roberts lebih cepat karena kernel kecil
Reality (dari testing):
•	Sobel 25.14% lebih cepat!
Pelajaran:
•	Teori ≠ Praktik dalam real-world implementation
•	Ukuran citra matters - pada citra besar, faktor lain lebih dominan
•	Implementation matters - algoritma "simple" tidak selalu "fast"
•	Always test! - jangan asumsikan dari teori saja

6. KESIMPULAN
6.1 Kesimpulan Umum
Berdasarkan implementasi dan analisis yang telah dilakukan terhadap citra IMG_5890.JPG (3456×5184 pixels), dapat disimpulkan:
1.	Performance: Sobel Menang ✅
o	Sobel 25.14% lebih cepat (732.94 vs 917.20 detik)
o	Bertentangan dengan teori, membuktikan pentingnya real testing
2.	Jumlah Deteksi: Sobel Menang ✅
o	Sobel mendeteksi 5x lebih banyak tepi (227,207 vs 47,085 piksel)
o	Lebih informatif dan lengkap
3.	Kualitas Deteksi: Sobel Menang ✅
o	Mean intensity lebih tinggi (6.10 vs 3.75)
o	Standard deviation lebih besar (variasi lebih kaya)
o	Tepi lebih jelas dan kontras
4.	Consistency: Tie 🤝
o	Correlation 85.78% menunjukkan agreement tinggi pada tepi utama
o	Perbedaan utama di detail halus
6.2 Rekomendasi Penggunaan
Gunakan Roberts jika:
❌ TIDAK DIREKOMENDASIKAN untuk:
•	Foto natural (seperti test case ini)
•	Citra beresolusi tinggi
•	Aplikasi yang memerlukan detail lengkap
✅ Mungkin cocok untuk:
•	Line drawing atau CAD
•	Citra synthetic dengan tepi sangat tajam
•	Situasi dengan constraint memory ekstrem
Gunakan Sobel jika:
✅ SANGAT DIREKOMENDASIKAN untuk:
•	Foto natural (landscape, portrait, etc.)
•	Citra dengan detail dan tekstur kompleks
•	Preprocessing untuk computer vision
•	Object detection dan segmentation
•	Analisis yang memerlukan informasi lengkap
6.3 Kontribusi dan Pembelajaran
Yang dipelajari dari project ini:
1.	Implementasi dari Scratch
o	Memahami cara kerja konvolusi
o	Belajar manipulasi array dengan NumPy
o	Praktik algoritma matematika
2.	Critical Thinking
o	Tidak blindly percaya teori
o	Pentingnya empirical testing
o	Analisis mendalam untuk mencari "why"
3.	Real-World Application
o	Context matters dalam pemilihan algoritma
o	Trade-off antara berbagai faktor
o	No "one size fits all" solution
4.	Scientific Method
o	Hypothesis → Experiment → Analysis → Conclusion
o	Data-driven decision making
o	Honest reporting (even unexpected results)
6.4 Keterbatasan dan Saran
Keterbatasan penelitian ini:
•	Hanya testing pada 1 citra
•	Implementasi belum dioptimasi (bisa lebih cepat dengan vectorization)
•	Belum membandingkan dengan operator lain (Canny, Prewitt)
Saran untuk pengembangan:
1.	Test pada berbagai jenis citra (medical, satellite, industrial)
2.	Implementasi optimasi (vectorization, GPU acceleration)
3.	Perbandingan dengan operator modern dan deep learning
4.	Develop adaptive operator selection

7. REFERENSI
1.	Roberts, L. G. (1965). Machine Perception of Three-Dimensional Solids. PhD Thesis, MIT.
2.	Sobel, I., & Feldman, G. (1968). A 3x3 Isotropic Gradient Operator for Image Processing. Stanford Artificial Intelligence Project.
3.	Gonzalez, R. C., & Woods, R. E. (2018). Digital Image Processing (4th Edition). Pearson.
4.	NumPy Documentation. (2024). NumPy User Guide. https://numpy.org/doc/
5.	Materi Kuliah Pengolahan Citra Digital - Pertemuan 9: Segmentasi Citra
