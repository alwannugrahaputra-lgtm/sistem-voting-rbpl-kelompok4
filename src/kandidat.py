class Kandidat:
    def __init__(self, nama):
        self.nama = nama
        self.jumlah_suara = 0

    def tambah_suara(self):
        self.jumlah_suara += 1