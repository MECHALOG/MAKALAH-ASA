import matplotlib.pyplot as plt
import numpy as np

# 1. DATA HASIL EKSPERIMEN
algoritma = ['Greedy', 'Dynamic\nProgramming', 'Farthest\nStrategy']


total_nilai = [495, 525, 510]


waktu_eksekusi = [0.008, 0.342, 0.045]


# 2. PENGATURAN VISUALISASI GRAFIK
# Membuat area gambar dengan 1 baris dan 2 kolom (bersebelahan)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Menentukan warna (Biru untuk Greedy, Oranye untuk DP, Hijau untuk Farthest)
colors = ['#2196F3', '#FF9800', '#4CAF50']

# --- GRAFIK 1: TOTAL NILAI SURVIVAL ---
bars1 = ax1.bar(algoritma, total_nilai, color=colors)
ax1.set_title('Perbandingan Total Nilai Survival\n(Optimalitas - Lebih Tinggi Lebih Baik)', fontsize=14, fontweight='bold', pad=15)
ax1.set_ylabel('Total Skor Utilitas', fontsize=12)
ax1.set_ylim(0, max(total_nilai) + 50) # Memberikan ruang kosong di atas bar
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Menambahkan label teks angka tepat di atas masing-masing bar
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval),
             ha='center', va='bottom', fontweight='bold', fontsize=12)

# --- GRAFIK 2: WAKTU EKSEKUSI ---
bars2 = ax2.bar(algoritma, waktu_eksekusi, color=colors)
ax2.set_title('Perbandingan Waktu Eksekusi\n(Efisiensi - Lebih Rendah Lebih Baik)', fontsize=14, fontweight='bold', pad=15)
ax2.set_ylabel('Waktu (Milidetik)', fontsize=12)
ax2.set_ylim(0, max(waktu_eksekusi) + 0.05)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Menambahkan label teks angka tepat di atas masing-masing bar
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.005, f"{yval} ms",
             ha='center', va='bottom', fontweight='bold', fontsize=12)

# 3. MENAMPILKAN GRAFIK
# Merapikan jarak antar grafik agar tidak bertumpuk
plt.tight_layout()

# Perintah untuk memunculkan gambar visualisasi di Colab
plt.show()