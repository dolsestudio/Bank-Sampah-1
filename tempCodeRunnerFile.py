from anggota import tambah_anggota, cari_anggota_by_id, tampilkan_anggota, edit_anggota
from tabungansampah import tambah_tabungan

def tampil_menu():
    print("=========================================")
    print("** Program Pengelolaan Tabungan Sampah **")
    print("=========================================")
    print("Pilihan menu:")
    print("1. Pengelolaan Keanggotaan")
    print("   1a. Penambahan Data Anggota")
    print("   1b. Pengubahan Data Anggota")
    print("   1c. Pencarian Data Anggota")
    print("2. Pengelolaan Tabungan Anggota")
    print("   2a. Penambahan Tabungan")
    print("   2b. Penarikan Tabungan")
    print("   2c. Menampilkan Data Tabungan")
    print("9. Exit")


def main():
    while True:
        tampil_menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1a":
            print("Penambahan Data Anggota")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            telepon = input("Nomor Telepon: ")
            tambah_anggota(nama, alamat, telepon)

        elif pilihan == "1b":
            print("Pencarian Data Anggota")
            idanggota = input("Masukkan ID Anggota: ")
            anggota = cari_anggota_by_id(idanggota)
            tampilkan_anggota(anggota)
            input("Tekan Enter untuk melanjutkan.")

        elif pilihan == "1c":
            print("Pengubahan Data Anggota")
            edit_anggota()

        elif pilihan == "2a":
            print("Penambahan Tabungan")
            idanggota = input("Input ID Anggota: ")
            tambah_tabungan(idanggota)

        elif pilihan == "2b":
            print("Penarikan Tabungan")

        elif pilihan == "2c":
            print("Menampilkan Data Tabungan")

        elif pilihan == "9":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid.")



if __name__ == "__main__":
    main()
