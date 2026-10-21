data_barang = [
    {"nama": "Laptop", "harga": 7500000, "stok": 5},
    {"nama": "Mouse", "harga": 75000, "stok": 20},
    {"nama": "Keyboard", "harga": 150000, "stok": 10},
    {"nama": "Monitor", "harga": 1500000, "stok": 8},
    {"nama": "Flashdisk", "harga": 50000, "stok": 15}
]

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    stok = int(input("Masukkan jumlah stok: "))

    data_barang.append({
        "nama": nama,
        "harga": harga,
        "stok": stok
    })
    print("Barang berhasil ditambahkan!")

def tampilkan_barang():
    if not data_barang:
        print("Data barang masih kosong.")
        return

    print("\n=== DAFTAR BARANG ===")
    for i, barang in enumerate(data_barang, start=1):
        print(f"{i}. Nama  : {barang['nama']}")
        print(f"   Harga : Rp{barang['harga']}")
        print(f"   Stok  : {barang['stok']}")

def cari_barang():
    nama = input("Masukkan nama barang yang dicari: ")

    for barang in data_barang:
        if barang["nama"].lower() == nama.lower():
            print("Barang ditemukan:", barang)
            return

    print("Barang tidak ditemukan.")

def hapus_barang():
    nama = input("Masukkan nama barang yang dihapus: ")

    for barang in data_barang:
        if barang["nama"].lower() == nama.lower():
            data_barang.remove(barang)
            print("Barang berhasil dihapus!")
            return

    print("Barang tidak ditemukan.")

while True:
    print("\n=== SISTEM PENDATAAN BARANG ===")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Cari Barang")
    print("4. Hapus Barang")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        cari_barang()
    elif pilihan == "4":
        hapus_barang()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
