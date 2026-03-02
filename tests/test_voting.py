import unittest
import sys
import os

# Supaya bisa import dari folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from voting import Voting


class TestVoting(unittest.TestCase):

    def setUp(self):
        self.voting = Voting()
        self.voting.tambah_kandidat("Andi")
        self.voting.tambah_kandidat("Budi")

    def test_tambah_kandidat(self):
        self.assertEqual(len(self.voting.daftar_kandidat), 2)

    def test_vote(self):
        self.voting.vote(0)
        self.assertEqual(self.voting.daftar_kandidat[0].jumlah_suara, 1)

    def test_hitung_total_suara(self):
        self.voting.vote(0)
        self.voting.vote(1)
        self.assertEqual(self.voting.hitung_total_suara(), 2)

    def test_tentukan_pemenang(self):
        self.voting.vote(0)
        self.voting.vote(0)
        pemenang = self.voting.tentukan_pemenang()
        self.assertEqual(pemenang.nama, "Andi")

    def test_vote_invalid(self):
        self.voting.vote(10)
        self.assertEqual(self.voting.hitung_total_suara(), 0)


if __name__ == "__main__":
    unittest.main()