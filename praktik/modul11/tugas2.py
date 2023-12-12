class DataObjek:
    def __init__(self, nama='', nilai=0):
        self.nama = nama
        self.nilai = nilai

    def get_nama(self):
        return self.nama

    def get_nilai(self):
        return self.nilai

    def set_nama(self, nama):
        self.nama = nama

    def set_nilai(self, nilai):
        self.nilai = nilai


# Inisialisasi objek
objek = None

while True:
    print("\n=====Program OOP =====")
    print("1. Mendeklarasikan Objek")
    print("2. Menampilkan Objek")
    print("3. Merubah Nilai Objek")
    print("4. Keluar Dari Program")

    pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")

    if pilihan == '1':
        nama = input("Masukkan Namamu: ")
        nilai = int(input("Masukkan Nilaimu: "))
        objek = DataObjek(nama, nilai)
        print("Data Berhasil Ditambahkan")

    elif pilihan == '2':
        if objek is not None:
            print("Nama:", objek.get_nama())
            print("Nilai:", objek.get_nilai())
        else:
            print("Objek belum dideklarasikan.")

    elif pilihan == '3':
        if objek is not None:
            print("Objek saat ini:")
            print("Nama:", objek.get_nama())
            print("Nilai:", objek.get_nilai())
            
            nama_baru = input("Masukkan Nama Baru: ")
            nilai_baru = int(input("Masukkan Nilai Baru: "))
            
            objek.set_nama(nama_baru)
            objek.set_nilai(nilai_baru)
            
            print("Data Berhasil Diubah")
        else:
            print("Objek belum dideklarasikan.")

    elif pilihan == '4':
        print("Keluar dari program. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3, atau 4.")
