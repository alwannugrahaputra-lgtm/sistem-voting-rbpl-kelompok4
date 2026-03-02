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