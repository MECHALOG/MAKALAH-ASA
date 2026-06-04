import matplotlib.pyplot as plt

# Algoritma Greedy (Fokus rasio v/w tertinggi)
greedy_w = [0, 2, 6, 11, 21, 27, 35, 45]
greedy_v = [0, 70, 145, 240, 325, 390, 445, 495]
greedy_labels = ['Start', 'Inhaler', 'Granat', 'Gloo Wall', 'Medkit', 'Landmine', 'Vest', 'Peluru SMG']

# Dynamic Programming (Kombinasi Optimal Mutlak)
dp_w = [0, 5, 15, 17, 21, 29, 35, 50]
dp_v = [0, 95, 180, 250, 325, 380, 445, 505]
dp_labels = ['Start', 'Gloo Wall', 'Medkit', 'Inhaler', 'Granat', 'Vest', 'Landmine', 'Peluru AR']

# Farthest Strategy (Adaptif berdasar waktu pertemuan item)
farthest_w = [0, 10, 25, 30, 34, 44, 50]
farthest_v = [0, 85, 145, 240, 315, 365, 430]
farthest_labels = ['Start', 'Medkit', 'Peluru AR', 'Gloo Wall', 'Granat', 'Peluru SMG', 'Landmine']
 
# 2. PENGATURAN VISUALISASI GRAFIK (1 Baris, 3 Kolom)
fig, axes = plt.subplots(1, 3, figsize=(22, 6))

def plot_knapsack_path(ax, w, v, labels, title, color):
    # Menggambar garis rute akumulasi
    ax.plot(w, v, color=color, linewidth=2, zorder=1)

    # Titik Start (Kotak Merah)
    ax.scatter(w[0], v[0], color='red', marker='s', s=100, label='Tas Kosong (0,0)', zorder=2)

    # Titik Item (Lingkaran Warna)
    ax.scatter(w[1:], v[1:], color=color, marker='o', s=100, zorder=2)

    # Menambahkan label teks pada setiap titik
    for i, txt in enumerate(labels):
        # Penyesuaian posisi teks agar tidak bertumpuk dengan garis
        y_offset = -12 if i % 2 == 0 else 10
        ax.annotate(txt, (w[i], v[i]),
                    textcoords="offset points",
                    xytext=(8, y_offset),
                    ha='left', fontsize=10, fontweight='bold')

    # Atribut Grafik
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Kapasitas Tas Terpakai (W)', fontsize=11)
    ax.set_ylabel('Total Nilai Survival (V)', fontsize=11)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='lower right')

    # Batas Sumbu (Dilebihkan sedikit agar titik tidak terpotong tepi)
    ax.set_xlim(-3, 55)
    ax.set_ylim(-20, 550)

# 3. MENGGAMBAR KETIGA GRAFIK
plot_knapsack_path(axes[0], greedy_w, greedy_v, greedy_labels,
                   'Rute Akumulasi Item (Greedy)\nTotal Nilai: 495 unit', '#3498db') # Biru

plot_knapsack_path(axes[1], dp_w, dp_v, dp_labels,
                   'Rute Akumulasi Item (DP)\nTotal Nilai: 505 unit', '#e67e22') # Oranye

plot_knapsack_path(axes[2], farthest_w, farthest_v, farthest_labels,
                   'Rute Akumulasi Item (Farthest)\nTotal Nilai: 430 unit', '#2ecc71') # Hijau

plt.tight_layout()
plt.show()