class Mahasiswa:
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan

    def tampilkan_biodata(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Angkatan:", self.angkatan)

# Inisialisasi list untuk menyimpan objek Mahasiswa
daftar_mahasiswa = []

# Input data dari user
nama_mahasiswa = input("Masukkan Namamu: ")
nim_mahasiswa = input("Masukkan NIM kamu: ")
angkatan_mahasiswa = input("Masukkan Tahun Angkatanmu: ")

# Membuat objek Mahasiswa
mahasiswa = Mahasiswa(nama_mahasiswa, nim_mahasiswa, angkatan_mahasiswa)

# Menambahkan objek Mahasiswa ke dalam list
daftar_mahasiswa.append(mahasiswa)

# Menampilkan biodata mahasiswa
print("\nBiodata Mahasiswa:")
mahasiswa.tampilkan_biodata()

# Menampilkan total mahasiswa
print("\nTotal Mahasiswa:", len(daftar_mahasiswa))
