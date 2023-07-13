import json
import random
from anggota import cari_anggota_by_id

def tambah_tabungan(idanggota):
    anggota = cari_anggota_by_id(idanggota)
    if anggota:
        print("IDAnggota:", anggota["idanggota"])
        print("Nama:", anggota["nama"])
        print("Telepon:", anggota["telepon"])
        print("Alamat:", anggota["alamat"])
        print("=============================================")
        print("Kode| Jenis Sampah    | Harga Satuan (Rp)")
        print("1   | Kardus          | 500")
        print("2   | Botol plastik   | 300")
        print("3   | Logam besi      | 800")
        print("4   | Logam tembaga   | 1000")
        print("=============================================")

        kode_sampah = input("Pilih jenis sampah: ")
        kuantitas_sampah = float(input("Kuantitas sampah: "))

        harga_satuan = cari_harga(kode_sampah)
        total = kuantitas_sampah * harga_satuan

        tabungan = {}
        tabungan["tanggal"] = get_current_date()
        tabungan["idtransaksi"] = generate_idtransaksi(idanggota)
        tabungan["tipetransaksi"] = "K"
        tabungan["sampah"] = kode_sampah
        tabungan["kuantitas"] = kuantitas_sampah
        tabungan["nilaisatuan"] = harga_satuan
        tabungan["total"] = total
        tabungan["saldo"] = get_saldo(idanggota) + total

        with open(f"tabungan{idanggota}.json", "r") as file:
            data = json.load(file)
            data.append(tabungan)

        with open(f"tabungan{idanggota}.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Pencatatan transaksi tabungan sampah berhasil.")

        ada_jenis_lain = input("Ada jenis sampah lain yang akan ditabung (Y/y = Ya, T/t = Tidak)? ")
        if ada_jenis_lain.lower() == "y" or ada_jenis_lain == "":
            tambah_tabungan(idanggota)
    else:
        print("Data anggota tidak ditemukan!")
        cari_lagi = input("Cari lagi (Y/y = Ya, T/t = Tidak)? ")
        if cari_lagi.lower() == "y" or cari_lagi == "":
            idanggota = input("Input ID Anggota: ")
            tambah_tabungan(idanggota)

def cari_harga(kode_sampah):
    with open("produksampah.json", "r") as file:
        data = json.load(file)

    if kode_sampah in data:
        return data[kode_sampah]["hargasatuan"]
    else:
        return 0

def get_saldo(idanggota):
    with open(f"tabungan{idanggota}.json", "r") as file:
        data = json.load(file)

    if data:
        return data[-1]["saldo"]
    else:
        return 0

def generate_idtransaksi(idanggota):
    with open(f"tabungan{idanggota}.json", "r") as file:
        data = json.load(file)
        existing_ids = [transaksi["idtransaksi"] for transaksi in data]

    idtransaksi = str(random.randint(1000000, 9999999))
    while idtransaksi in existing_ids:
        idtransaksi = str(random.randint(1000000, 9999999))

    return idtransaksi

def get_current_date():
    import datetime
    return datetime.date.today().strftime("%Y-%m-%d")

