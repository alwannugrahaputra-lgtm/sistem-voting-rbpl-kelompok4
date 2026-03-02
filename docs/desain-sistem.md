# Desain Sistem Voting

## Deskripsi Umum
Aplikasi ini merupakan sistem voting berbasis CLI menggunakan Python.

## Struktur File

- kandidat.py → Menyimpan class Kandidat
- voting.py → Berisi logika sistem voting
- main.py → Interface utama program
- test_voting.py → Unit test sistem

## Alur Program

User memilih menu →
Input kandidat atau voting →
Data diproses oleh class Voting →
Output ditampilkan berupa statistik atau pemenang.

## Konsep IPO

Input:
- Nama kandidat
- Pilihan voting

Process:
- Penambahan suara
- Perhitungan total suara
- Perhitungan persentase

Output:
- Statistik suara
- Pemenang