import json
from kandidat import Kandidat

class Voting:
    def __init__(self):
        self.daftar_kandidat = []

    def tambah_kandidat(self, nama):
        self.daftar_kandidat.append(Kandidat(nama))

    def vote(self, nomor):
        if 0 <= nomor < len(self.daftar_kandidat):
            self.daftar_kandidat[nomor].tambah_suara()
        else:
            print("Nomor kandidat tidak valid.")

    # 👇 TAMBAHKAN DI SINI
    def tampilkan_kandidat(self):
        if not self.daftar_kandidat:
            print("Belum ada kandidat.")
            return

        print("\nDaftar Kandidat:")
        for i, kandidat in enumerate(self.daftar_kandidat):
            print(f"{i}. {kandidat.nama}")

    def hitung_total_suara(self):
        return sum(k.jumlah_suara for k in self.daftar_kandidat)

    def tampilkan_statistik(self):
        total = self.hitung_total_suara()
        if total == 0:
            print("Belum ada suara.")
            return

        for kandidat in self.daftar_kandidat:
            persentase = (kandidat.jumlah_suara / total) * 100
            print(f"{kandidat.nama} - {kandidat.jumlah_suara} suara ({persentase:.2f}%)")

    def tentukan_pemenang(self):
        if not self.daftar_kandidat:
            return None
        return max(self.daftar_kandidat, key=lambda k: k.jumlah_suara)

    def simpan_data(self, filename="data.json"):
        data = [{"nama": k.nama, "suara": k.jumlah_suara} for k in self.daftar_kandidat]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.daftar_kandidat = []
                for item in data:
                    kandidat = Kandidat(item["nama"])
                    kandidat.jumlah_suara = item["suara"]
                    self.daftar_kandidat.append(kandidat)
        except FileNotFoundError:
            pass