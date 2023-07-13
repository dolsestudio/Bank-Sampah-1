import json
import random

def tambah_anggota(nama, alamat, telepon):
    anggota = {}
    anggota["idanggota"] = generate_idanggota()
    anggota["nama"] = nama
    anggota["alamat"] = alamat
    anggota["tanggal"] = get_current_date()
    anggota["telepon"] = telepon

    with open("anggotas.json", "r") as file:
        data = json.load(file)
        data[anggota["idanggota"]] = anggota

    with open("anggotas.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Berhasil menambahkan data anggota.")
    input("Tekan Enter untuk melanjutkan.")

def generate_idanggota():
    with open("anggotas.json", "r") as file:
        data = json.load(file)
        existing_ids = list(data.keys())

    idanggota = random.randint(10000, 99999)
    while str(idanggota) in existing_ids:
        idanggota = random.randint(10000, 99999)

    return str(idanggota)

def get_current_date():
    import datetime
    return datetime.date.today().strftime("%Y-%m-%d")

def cari_anggota_by_id(idanggota):
    with open("anggotas.json", "r") as file:
        data = json.load(file)

    if idanggota in data:
        return data[idanggota]
    else:
        return {}

def tampilkan_anggota(anggota):
    if anggota:
        print("ID Anggota:", anggota["idanggota"])
        print("Nama:", anggota["nama"])
        print("Alamat:", anggota["alamat"])
        print("Telepon:", anggota["telepon"])
        print("Tanggal Daftar:", anggota["tanggal"])
    else:
        print("Tidak ada data anggota !")

def edit_anggota():
    idanggota = input("Ketik ID anggota yang akan diedit: ")
    anggota = cari_anggota_by_id(idanggota)

    if anggota:
        print("Nama:", anggota["nama"])
        nama = input("-> ")
        if nama != "":
            anggota["nama"] = nama

        print("Alamat:", anggota["alamat"])
        alamat = input("-> ")
        if alamat != "":
            anggota["alamat"] = alamat

        print("Telepon:", anggota["telepon"])
        telepon = input("-> ")
        if telepon != "":
            anggota["telepon"] = telepon

        with open("anggotas.json", "r") as file:
            data = json.load(file)
            data[idanggota] = anggota

        with open("anggotas.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data berhasil diubah.")
        input("Tekan Enter untuk melanjutkan.")
    else:
        print("Data anggota tidak ditemukan!")
        cari_lagi = input("Cari lagi (Y/y = Ya, T/t = Tidak)? ")
        if cari_lagi.lower() == "y" or cari_lagi == "":
            edit_anggota()

