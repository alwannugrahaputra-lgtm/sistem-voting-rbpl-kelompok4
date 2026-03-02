from voting import Voting

def main():
    voting = Voting()

    while True:
        print("\n=== SISTEM VOTING ===")
        print("1. Tambah Kandidat")
        print("2. Voting")
        print("3. Tampilkan Hasil")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama kandidat: ")
            voting.tambah_kandidat(nama)

        elif pilihan == "2":
            voting.tampilkan_hasil()
            nomor = int(input("Pilih nomor kandidat: "))
            voting.vote(nomor)

        elif pilihan == "3":
            voting.tampilkan_hasil()

        elif pilihan == "4":
            break

if __name__ == "__main__":
    main()