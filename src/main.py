from voting import Voting

def main():
    voting = Voting()
    voting.load_data()

    while True:
        print("\n=== SISTEM VOTING ===")
        print("1. Tambah Kandidat")
        print("2. Voting")
        print("3. Tampilkan Statistik")
        print("4. Tentukan Pemenang")
        print("5. Simpan & Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama kandidat: ")
            voting.tambah_kandidat(nama)

        elif pilihan == "2":
            voting.tampilkan_kandidat()
            nomor = int(input("Pilih nomor kandidat: "))
            voting.vote(nomor)

        elif pilihan == "3":
            voting.tampilkan_statistik()

        elif pilihan == "4":
            pemenang = voting.tentukan_pemenang()
            if pemenang:
                print(f"Pemenang: {pemenang.nama}")
            else:
                print("Belum ada kandidat.")

        elif pilihan == "5":
            voting.simpan_data()
            print("Data disimpan. Keluar...")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()