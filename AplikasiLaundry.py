from tabulate import tabulate

# Fungsi untuk menghitung total biaya berdasarkan berat cucian
def hitung_biaya_berat(berat, harga_per_kg):
    total_biaya = berat * harga_per_kg
    return total_biaya

# Variabel untuk menyimpan transaksi
transaksi = []

# Data jenis laundry (contoh, bisa ditambahkan jenis lainnya)
jenis_laundry = {
    "Cuci Reguler": 5000,
    "Cuci Kilat": 12000
}

# Fungsi untuk mencatat transaksi
def catat_transaksi():
    print("\n")
    print("=== Catat Transaksi ===")
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    print("Pilih jenis laundry:")
    for i, jenis in enumerate(jenis_laundry, start=1):
        print(f"{i}. {jenis} - Rp {jenis_laundry[jenis]}/kg")
    pilihan_jenis = int(input("Masukkan pilihan jenis laundry: "))
    berat_cucian = float(input("Masukkan berat cucian dalam kilogram: "))
    jenis = list(jenis_laundry.keys())[pilihan_jenis - 1]
    harga_per_kg = jenis_laundry[jenis]
    total_biaya = hitung_biaya_berat(berat_cucian, harga_per_kg)
    transaksi.append({"nama_pelanggan": nama_pelanggan, "jenis_laundry": jenis, "berat_cucian": berat_cucian, "total_biaya": total_biaya})
    print("Transaksi berhasil dicatat.")

# Fungsi untuk menampilkan riwayat transaksi
def tampilkan_riwayat_transaksi():
    print("\n")
    print("=== Riwayat Transaksi ===")
    if not transaksi:
        print("Belum ada riwayat transaksi.")
    else:
        headers = ["No", "Nama Pelanggan", "Jenis Laundry", "Berat (kg)", "Total Biaya"]
        rows = []
        for i, trx in enumerate(transaksi, start=1):
            row = [i, trx['nama_pelanggan'], trx['jenis_laundry'], trx['berat_cucian'], trx['total_biaya']]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))

# Fungsi untuk menampilkan rekap transaksi
def tampilkan_rekap_transaksi():
    print("\n")
    print("=== Rekap Transaksi ===")
    if not transaksi:
        print("Belum ada transaksi yang dicatat.")
    else:
        total_pendapatan = sum(trx["total_biaya"] for trx in transaksi)
        print(f"Total Pendapatan: Rp {total_pendapatan}")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n")
    print("=== APLIKASI LAUNDRY ===")
    print("1. Catat Transaksi")
    print("2. Jenis Laundry")
    print("3. Riwayat Transaksi")
    print("4. Rekap Transaksi")
    print("5. Selesai")

# Input pilihan menu dari pengguna
pilihan = 0
while pilihan != 5:
    tampilkan_menu()
    pilihan = int(input("Masukkan pilihan menu: "))

    if pilihan == 1:
        catat_transaksi()
    elif pilihan == 2:
        print("\n")
        print("=== Jenis Laundry ===")
        for i, jenis in enumerate(jenis_laundry, start=1):
            print(f"{i}. {jenis} - Rp {jenis_laundry[jenis]}/kg")
    elif pilihan == 3:
        tampilkan_riwayat_transaksi()
    elif pilihan == 4:
        tampilkan_rekap_transaksi()
    elif pilihan == 5:
        print("Terima kasih telah menggunakan aplikasi laundry.")
    else:
        print("Pilihan menu tidak valid. Silakan masukkan pilihan yang benar.")
