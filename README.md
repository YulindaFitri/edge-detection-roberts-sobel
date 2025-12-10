**🔍 Deteksi Tepi: Roberts vs Sobel**

*Implementasi dan perbandingan operator Roberts dan Sobel untuk deteksi tepi menggunakan Python*

*Tugas Pengolahan Citra Digital | TI23E*


**📖 Tentang Project**

Project ini adalah implementasi from scratch (tanpa OpenCV) dari dua operator klasik deteksi tepi:

•	🔷 Operator Roberts (1965) - Kernel 2×2, cepat tapi sensitif

•	🔶 Operator Sobel (1968) - Kernel 3×3, robust dan stabil

Program ini membandingkan kedua operator secara lengkap dengan analisis kuantitatif dan visualisasi 12 panel.



**🎯 Fitur**

✅ Implementasi Manual - Pure NumPy, no OpenCV

✅ Analisis Lengkap - 8+ metrics kuantitatif

✅ Visualisasi Keren - 12 panel comparison

✅ Auto Save - Output tersimpan otomatis

✅ Dokumentasi Lengkap - Code comments & laporan



**🚀 Quick Start**

1. Install Dependencies
   
pip install numpy imageio matplotlib

2. Clone Repository
   
git clone https://github.com/[username]/edge-detection-roberts-sobel.git

cd edge-detection-roberts-sobel

3. Edit Path Gambar
   
Buka edge_detection.py dan ubah:

image_path = r"C:\path\to\your\image.jpg"  # Ganti dengan path gambar kamu

4. Run Program
   
python edge_detection.py

5. Lihat Hasil
   
•	✅ Console: Analisis lengkap dengan metrics

•	✅ Output folder: Visualisasi 12 panel (PNG, 300 DPI)



**📁 Struktur Project**

edge-detection-roberts-sobel/

│

├── edge_detection.py          # Program utama

├── README.md                  # Documentation (file ini)

├── LAPORAN.md                 # Analisis lengkap & detail

│

└── output/

    └── hasil_perbandingan_lengkap.png  # Visualisasi 12 panel



**🎨 Output Visualisasi**

Program menghasilkan visualisasi 12 panel yang berisi:

Baris 1: Citra asli + Info specs kedua operator

Baris 2: Roberts (Gradien X, Y, Magnitude)

Baris 3: Sobel (Gradien X, Y, Magnitude)

Baris 4: Difference map, Histogram, Bar chart

Format: PNG, 300 DPI (publication quality)



**🔬 Analisis Lengkap**

Untuk analisis mendalam, pembahasan detail, dan interpretasi hasil, lihat:

👉 LAPORAN.md

Berisi:

•	Landasan teori lengkap

•	Metodologi detail

•	Analisis kuantitatif & kualitatif

•	Pembahasan mendalam

•	Kesimpulan dan rekomendasi

•	Referensi akademik



**🛠️ Tech Stack**

•	Language: Python 3.11

•	Libraries: 

o	imageio v2 - Image I/O

o	numpy - Array operations & convolution

o	matplotlib - Data visualization

•	No OpenCV! - Pure implementation untuk learning



**📞 Contact**

Yulinda Fitri

Teknik Informatika - TI23E

•	📧 Email: yulinda.fitri_ti23@nusaputra.ac.id



**🙏 Acknowledgments**

•	Dosen PCD - Untuk guidance & pembelajaran



**📜 License**

Project ini dibuat untuk keperluan akademik (Tugas PCD).


