import time

# ==========================================
# 1. PERSIAPAN DATA (Variabel yang sebelumnya hilang)
# ==========================================
items = [
    {"nama": "Gloo Wall", "berat": 5, "nilai": 95},
    {"nama": "Medkit", "berat": 10, "nilai": 85},
    {"nama": "Inhaler", "berat": 2, "nilai": 70},
    {"nama": "Peluru AR", "berat": 15, "nilai": 60},
    {"nama": "Peluru SMG", "berat": 10, "nilai": 50},
    {"nama": "Granat", "berat": 4, "nilai": 75},
    {"nama": "Stock Lv3", "berat": 3, "nilai": 40},
    {"nama": "Vest Repair", "berat": 8, "nilai": 55},
    {"nama": "Landmine", "berat": 6, "nilai": 65},
    {"nama": "Treatment Ammo", "berat": 5, "nilai": 30}
]
KAPASITAS_TAS = 50

def greedy_looting(items, capacity):
    # Menghitung rasio dan mengurutkan secara menurun (descending)
    sorted_items = sorted(items, key=lambda x: x['nilai'] / x['berat'], reverse=True)

    total_nilai = 0
    total_berat = 0
    terpilih = []

    for item in sorted_items:
        if total_berat + item['berat'] <= capacity:
            terpilih.append(item['nama'])
            total_nilai += item['nilai']
            total_berat += item['berat']

    return terpilih, total_nilai, total_berat

# Eksekusi & Pengukuran Waktu
start_time = time.perf_counter()
hasil_greedy, nilai_greedy, berat_greedy = greedy_looting(items, KAPASITAS_TAS)
end_time = time.perf_counter()

waktu_greedy = (end_time - start_time) * 1000 # konversi ke milidetik
print("=== HASIL ALGORITMA GREEDY ===")
print(f"Item Terpilih: {hasil_greedy}")
print(f"Total Nilai Survival: {nilai_greedy}")
print(f"Total Kapasitas Terpakai: {berat_greedy}/{KAPASITAS_TAS}")
print(f"Waktu Eksekusi: {waktu_greedy:.4f} ms\n")



def dp_looting(items, capacity):
    n = len(items)
    # Membuat matriks DP
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Mengisi matriks DP
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i-1]['berat'] <= w:
                dp[i][w] = max(items[i-1]['nilai'] + dp[i-1][w - items[i-1]['berat']], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Proses Backtracking untuk mencari tahu item apa saja yang dimasukkan
    terpilih = []
    w = capacity
    total_berat = 0
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            terpilih.append(items[i-1]['nama'])
            w -= items[i-1]['berat']
            total_berat += items[i-1]['berat']

    return terpilih, dp[n][capacity], total_berat

# Eksekusi & Pengukuran Waktu
start_time = time.perf_counter()
hasil_dp, nilai_dp, berat_dp = dp_looting(items, KAPASITAS_TAS)
end_time = time.perf_counter()

waktu_dp = (end_time - start_time) * 1000
print("=== HASIL DYNAMIC PROGRAMMING ===")
print(f"Item Terpilih: {hasil_dp[::-1]}") # Dibalik agar urutannya dari awal
print(f"Total Nilai Survival: {nilai_dp}")
print(f"Total Kapasitas Terpakai: {berat_dp}/{KAPASITAS_TAS}")
print(f"Waktu Eksekusi: {waktu_dp:.4f} ms\n")



# Array stream mensimulasikan urutan barang yang ditemui pemain saat berlari di map
stream_looting = [
    {"nama": "Medkit", "berat": 10, "nilai": 85},
    {"nama": "Peluru AR", "berat": 15, "nilai": 60},
    {"nama": "Gloo Wall", "berat": 5, "nilai": 95},
    {"nama": "Granat", "berat": 4, "nilai": 75},
    {"nama": "Medkit", "berat": 10, "nilai": 85},      # Medkit ditemui lagi
    {"nama": "Inhaler", "berat": 2, "nilai": 70},
    {"nama": "Peluru SMG", "berat": 10, "nilai": 50},
    {"nama": "Vest Repair", "berat": 8, "nilai": 55},
    {"nama": "Gloo Wall", "berat": 5, "nilai": 95},    # Gloo wall ditemui lagi
    {"nama": "Landmine", "berat": 6, "nilai": 65}
]

def farthest_strategy_looting(stream, capacity):
    tas = []
    total_berat = 0
    total_nilai = 0

    for i in range(len(stream)):
        item_sekarang = stream[i]

        # Jika kapasitas masih cukup, langsung masukkan ke tas
        if total_berat + item_sekarang['berat'] <= capacity:
            tas.append(item_sekarang)
            total_berat += item_sekarang['berat']
            total_nilai += item_sekarang['nilai']
        else:
            # Jika tas penuh, cek barang mana yang paling jauh dibutuhkan di sisa perjalanan
            sisa_stream = stream[i+1:]
            farthest_idx = -1
            item_to_drop = None

            for barang_di_tas in tas:
                try:
                    # Cari urutan kemunculan barang ini di masa depan
                    idx_masa_depan = next(index for (index, d) in enumerate(sisa_stream) if d["nama"] == barang_di_tas["nama"])
                except StopIteration:
                    # Jika tidak ditemukan di masa depan, anggap jaraknya tak terhingga
                    idx_masa_depan = float('inf')

                # Temukan barang yang letaknya paling jauh (atau tidak terpakai lagi)
                if idx_masa_depan > farthest_idx:
                    farthest_idx = idx_masa_depan
                    item_to_drop = barang_di_tas

            # Ganti barang tersebut dengan barang baru JIKA beratnya muat
            if item_to_drop and item_sekarang['berat'] <= item_to_drop['berat']:
                tas.remove(item_to_drop)
                total_berat -= item_to_drop['berat']
                total_nilai -= item_to_drop['nilai']

                tas.append(item_sekarang)
                total_berat += item_sekarang['berat']
                total_nilai += item_sekarang['nilai']

    nama_terpilih = [b['nama'] for b in tas]
    return nama_terpilih, total_nilai, total_berat

# Eksekusi & Pengukuran Waktu
start_time = time.perf_counter()
hasil_farthest, nilai_farthest, berat_farthest = farthest_strategy_looting(stream_looting, KAPASITAS_TAS)
end_time = time.perf_counter()

waktu_farthest = (end_time - start_time) * 1000
print("=== HASIL FARTHEST STRATEGY ===")
print(f"Item Terakhir di Tas: {hasil_farthest}")
print(f"Total Nilai Survival: {nilai_farthest}")
print(f"Total Kapasitas Terpakai: {berat_farthest}/{KAPASITAS_TAS}")
print(f"Waktu Eksekusi: {waktu_farthest:.4f} ms\n")