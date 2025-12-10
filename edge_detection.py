"""
Program Perbandingan Operator Roberts dan Sobel untuk Deteksi Tepi
Mata Kuliah: Pengolahan Citra Digital
Implementasi: imageio + numpy + matplotlib

Nama: Yulinda Fitri 
Kelas: TI23E
"""

import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt
import time
from math import log10, sqrt
import os

# ============================================
# DEFINISI OPERATOR
# ============================================

# Operator Roberts (2x2) - Deteksi tepi diagonal
robertsX = np.array([
    [1, 0],
    [0, -1]
])

robertsY = np.array([
    [0, 1],
    [-1, 0]
])

# Operator Sobel (3x3) - Deteksi tepi horizontal dan vertikal
sobelX = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobelY = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

# ============================================
# FUNGSI DETEKSI TEPI ROBERTS
# ============================================

def roberts_edge_detection(image):
    """
    Implementasi Operator Roberts untuk deteksi tepi
    
    Parameter:
        image: numpy array - citra input dalam grayscale
        
    Return:
        Gx: gradien arah X
        Gy: gradien arah Y
        G: magnitude gradien (hasil deteksi tepi)
    """
    # Padding untuk menghindari out of bounds
    imgPad = np.pad(image, pad_width=1, mode='constant', constant_values=0)
    
    # Inisialisasi matriks gradien
    Gx = np.zeros_like(image)
    Gy = np.zeros_like(image)
    
    # Konvolusi dengan operator Roberts (2x2)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            # Ekstrak area 2x2
            area = imgPad[y:y+2, x:x+2]
            
            # Hitung gradien X dan Y
            Gx[y, x] = np.sum(area * robertsX)
            Gy[y, x] = np.sum(area * robertsY)
    
    # Hitung magnitude gradien menggunakan rumus Euclidean
    G = np.sqrt(Gx**2 + Gy**2)
    
    # Normalisasi ke range 0-255
    if G.max() != 0:
        G = (G / G.max()) * 255
    G = np.clip(G, 0, 255).astype(np.uint8)
    
    return Gx, Gy, G

# ============================================
# FUNGSI DETEKSI TEPI SOBEL
# ============================================

def sobel_edge_detection(image):
    """
    Implementasi Operator Sobel untuk deteksi tepi
    
    Parameter:
        image: numpy array - citra input dalam grayscale
        
    Return:
        Gx: gradien arah X
        Gy: gradien arah Y
        G: magnitude gradien (hasil deteksi tepi)
    """
    # Padding untuk kernel 3x3
    imgPad = np.pad(image, pad_width=1, mode='constant', constant_values=0)
    
    # Inisialisasi matriks gradien
    Gx = np.zeros_like(image)
    Gy = np.zeros_like(image)
    
    # Konvolusi dengan operator Sobel (3x3)
    for y in range(1, imgPad.shape[0]-1):
        for x in range(1, imgPad.shape[1]-1):
            # Ekstrak area 3x3
            area = imgPad[y-1:y+2, x-1:x+2]
            
            # Hitung gradien X dan Y
            Gx[y-1, x-1] = np.sum(area * sobelX)
            Gy[y-1, x-1] = np.sum(area * sobelY)
    
    # Hitung magnitude gradien menggunakan rumus Euclidean
    G = np.sqrt(Gx**2 + Gy**2)
    
    # Normalisasi ke range 0-255
    if G.max() != 0:
        G = (G / G.max()) * 255
    G = np.clip(G, 0, 255).astype(np.uint8)
    
    return Gx, Gy, G

# ============================================
# FUNGSI METRICS
# ============================================

def calculate_mse(img1, img2):
    """Menghitung Mean Squared Error"""
    return np.mean((img1.astype(float) - img2.astype(float)) ** 2)

def calculate_psnr(img1, img2):
    """Menghitung Peak Signal-to-Noise Ratio"""
    mse_val = calculate_mse(img1, img2)
    if mse_val == 0:
        return float('inf')
    return 20 * log10(255.0 / sqrt(mse_val))

# ============================================
# FUNGSI ANALISIS LENGKAP
# ============================================

def analyze_comprehensive(roberts_result, sobel_result, roberts_time, sobel_time):
    """
    Analisis kuantitatif lengkap hasil deteksi tepi
    """
    print("\n" + "="*70)
    print("          ANALISIS KOMPARATIF ROBERTS VS SOBEL")
    print("="*70)
    
    # 1. STATISTIK DASAR
    print("\n📊 1. STATISTIK INTENSITAS TEPI")
    print("-" * 70)
    print(f"{'Metrik':<30} {'Roberts':<20} {'Sobel':<20}")
    print("-" * 70)
    print(f"{'Mean Intensity':<30} {np.mean(roberts_result):<20.2f} {np.mean(sobel_result):<20.2f}")
    print(f"{'Std Deviation':<30} {np.std(roberts_result):<20.2f} {np.std(sobel_result):<20.2f}")
    print(f"{'Min Value':<30} {np.min(roberts_result):<20} {np.min(sobel_result):<20}")
    print(f"{'Max Value':<30} {np.max(roberts_result):<20} {np.max(sobel_result):<20}")
    
    # 2. EDGE DETECTION METRICS
    threshold = 50
    roberts_edges = np.sum(roberts_result > threshold)
    sobel_edges = np.sum(sobel_result > threshold)
    
    print(f"\n🔍 2. JUMLAH PIKSEL TEPI (Threshold > {threshold})")
    print("-" * 70)
    print(f"Roberts: {roberts_edges:,} piksel")
    print(f"Sobel  : {sobel_edges:,} piksel")
    print(f"Selisih: {abs(roberts_edges - sobel_edges):,} piksel ({abs(roberts_edges - sobel_edges)/max(roberts_edges, sobel_edges)*100:.2f}%)")
    
    # 3. CORRELATION & SIMILARITY
    diff = np.abs(roberts_result.astype(float) - sobel_result.astype(float))
    correlation = np.corrcoef(roberts_result.flatten(), sobel_result.flatten())[0, 1]
    
    print(f"\n📈 3. SIMILARITY METRICS")
    print("-" * 70)
    print(f"Mean Absolute Difference : {np.mean(diff):.2f}")
    print(f"Correlation Coefficient  : {correlation:.4f}")
    print(f"MSE (Roberts vs Sobel)   : {calculate_mse(roberts_result, sobel_result):.2f}")
    print(f"PSNR (Roberts vs Sobel)  : {calculate_psnr(roberts_result, sobel_result):.2f} dB")
    
    # 4. PERFORMANCE
    print(f"\n⚡ 4. PERFORMANCE METRICS")
    print("-" * 70)
    print(f"Roberts Processing Time  : {roberts_time:.4f} seconds")
    print(f"Sobel Processing Time    : {sobel_time:.4f} seconds")
    speedup = ((sobel_time - roberts_time) / sobel_time) * 100
    print(f"Roberts Speedup          : {speedup:.2f}% faster" if speedup > 0 else f"Sobel Speedup: {-speedup:.2f}% faster")
    
    # 5. CONTRAST
    roberts_contrast = np.max(roberts_result) - np.min(roberts_result)
    sobel_contrast = np.max(sobel_result) - np.min(sobel_result)
    
    print(f"\n🎨 5. CONTRAST ANALYSIS")
    print("-" * 70)
    print(f"Roberts Contrast : {roberts_contrast}")
    print(f"Sobel Contrast   : {sobel_contrast}")
    
    print("\n" + "="*70)
    
    return diff

# ============================================
# FUNGSI VISUALISASI
# ============================================

def create_visualization(image, roberts_Gx, roberts_Gy, roberts_G, 
                        sobel_Gx, sobel_Gy, sobel_G, diff):
    """
    Membuat visualisasi lengkap hasil deteksi tepi
    """
    fig = plt.figure(figsize=(18, 12))
    
    # Row 1: Original Image dan Info
    plt.subplot(4, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('CITRA ASLI', fontsize=12, fontweight='bold', pad=10)
    plt.axis('off')
    
    plt.subplot(4, 3, 2)
    plt.text(0.5, 0.5, 'OPERATOR ROBERTS\n\n' + 
             'Kernel: 2×2\n' +
             'Orientasi: Diagonal\n' +
             'Kecepatan: Sangat Cepat\n' +
             'Noise: Sensitif Tinggi',
             ha='center', va='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    plt.axis('off')
    
    plt.subplot(4, 3, 3)
    plt.text(0.5, 0.5, 'OPERATOR SOBEL\n\n' + 
             'Kernel: 3×3\n' +
             'Orientasi: H & V\n' +
             'Kecepatan: Cepat\n' +
             'Noise: Robust',
             ha='center', va='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
    plt.axis('off')
    
    # Row 2: Roberts Gradients
    plt.subplot(4, 3, 4)
    plt.imshow(roberts_Gx, cmap='gray')
    plt.title('Roberts - Gradien X', fontsize=11)
    plt.axis('off')
    
    plt.subplot(4, 3, 5)
    plt.imshow(roberts_Gy, cmap='gray')
    plt.title('Roberts - Gradien Y', fontsize=11)
    plt.axis('off')
    
    plt.subplot(4, 3, 6)
    plt.imshow(roberts_G, cmap='gray')
    plt.title('ROBERTS - HASIL AKHIR', fontsize=11, fontweight='bold')
    plt.axis('off')
    
    # Row 3: Sobel Gradients
    plt.subplot(4, 3, 7)
    plt.imshow(sobel_Gx, cmap='gray')
    plt.title('Sobel - Gradien X', fontsize=11)
    plt.axis('off')
    
    plt.subplot(4, 3, 8)
    plt.imshow(sobel_Gy, cmap='gray')
    plt.title('Sobel - Gradien Y', fontsize=11)
    plt.axis('off')
    
    plt.subplot(4, 3, 9)
    plt.imshow(sobel_G, cmap='gray')
    plt.title('SOBEL - HASIL AKHIR', fontsize=11, fontweight='bold')
    plt.axis('off')
    
    # Row 4: Analysis
    plt.subplot(4, 3, 10)
    plt.imshow(diff, cmap='hot')
    plt.title('Absolute Difference', fontsize=11, fontweight='bold')
    plt.colorbar(fraction=0.046, pad=0.04)
    plt.axis('off')
    
    plt.subplot(4, 3, 11)
    plt.hist(roberts_G.flatten(), bins=50, alpha=0.6, label='Roberts', color='blue', edgecolor='black')
    plt.hist(sobel_G.flatten(), bins=50, alpha=0.6, label='Sobel', color='red', edgecolor='black')
    plt.title('Distribusi Intensitas', fontsize=11, fontweight='bold')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(4, 3, 12)
    categories = ['Roberts', 'Sobel']
    edge_counts = [np.sum(roberts_G > 50), np.sum(sobel_G > 50)]
    bars = plt.bar(categories, edge_counts, color=['blue', 'red'], alpha=0.7, edgecolor='black')
    plt.title('Jumlah Piksel Tepi', fontsize=11, fontweight='bold')
    plt.ylabel('Jumlah Piksel (threshold > 50)')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.suptitle('PERBANDINGAN KOMPREHENSIF: OPERATOR ROBERTS VS SOBEL', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    plt.tight_layout()
    
    return fig

# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """
    Fungsi utama program
    """
    print("="*70)
    print("   PROGRAM PERBANDINGAN OPERATOR ROBERTS DAN SOBEL")
    print("   Implementasi: imageio + numpy + matplotlib")
    print("="*70)
    
    # Path gambar - UBAH SESUAI LOKASI ANDA
    image_path = r"C:\Users\asusa\Pictures\Youlin\IMG_5890.JPG"
    
    try:
        # Baca citra
        print(f"\n📂 Membaca citra dari: {image_path}")
        image = img.imread(image_path, mode='F')
        print(f"✓ Berhasil membaca citra")
        print(f"  - Dimensi: {image.shape[0]} x {image.shape[1]} piksel")
        print(f"  - Tipe data: {image.dtype}")
        
        # Proses Roberts
        print(f"\n⚙️  Memproses Operator Roberts...")
        start_time = time.perf_counter()
        roberts_Gx, roberts_Gy, roberts_G = roberts_edge_detection(image)
        roberts_time = time.perf_counter() - start_time
        print(f"✓ Selesai dalam {roberts_time:.4f} detik")
        
        # Proses Sobel
        print(f"\n⚙️  Memproses Operator Sobel...")
        start_time = time.perf_counter()
        sobel_Gx, sobel_Gy, sobel_G = sobel_edge_detection(image)
        sobel_time = time.perf_counter() - start_time
        print(f"✓ Selesai dalam {sobel_time:.4f} detik")
        
        # Analisis
        diff = analyze_comprehensive(roberts_G, sobel_G, roberts_time, sobel_time)
        
        # Visualisasi
        print(f"\n📊 Membuat visualisasi...")
        fig = create_visualization(image, roberts_Gx, roberts_Gy, roberts_G,
                                   sobel_Gx, sobel_Gy, sobel_G, diff)
        
        # Simpan hasil
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "hasil_perbandingan_lengkap.png")
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Visualisasi disimpan: {output_path}")
        
        plt.show()
        
        print("\n" + "="*70)
        print("                  PROGRAM SELESAI")
        print("="*70)
        
    except FileNotFoundError:
        print(f"\n❌ Error: File tidak ditemukan!")
        print(f"   Path: {image_path}")
        print(f"   Silakan update variabel 'image_path' dengan path yang benar.")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print(f"   Tipe error: {type(e).__name__}")

# ============================================
# JALANKAN PROGRAM
# ============================================

if __name__ == "__main__":
    main()