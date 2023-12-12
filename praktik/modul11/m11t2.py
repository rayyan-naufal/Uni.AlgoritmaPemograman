class Student:
    def __init__(self, nama=None, nilai=None):
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

# Fungsi untuk menampilkan menu
def display_menu():
    print("\n===Program OOP===")
    print("1. Mendeklarasikan Objek")
    print("2. Menampilkan Objek")
    print("3. Merubah Nilai Objek")
    print("4. Menghapus Objek")
    print("5. Keluar Dari Program")

# Fungsi untuk mendeklarasikan objek
def declare_object():
    global student  # Declare student as a global variable
    nama = input("Masukkan Namamu: ")
    nilai = int(input("Masukkan Nilaimu: "))
    student = Student(nama, nilai)
    print("Data Berhasil Ditambahkan")

# Fungsi untuk menampilkan objek
def display_object():
    global student  # Use the global variable
    if student:
        print(f"Nama: {student.get_nama()}")
        print(f"Nilai: {student.get_nilai()}")
    else:
        print("Objek belum dideklarasikan.")

# Fungsi untuk merubah nilai objek
def modify_object():
    global student  # Use the global variable
    if student:
        choice = input("Apa yang ingin diubah (Nama/Nilai): ")
        if choice.lower() == "nama":
            new_nama = input("Masukkan Nama Baru: ")
            student.set_nama(new_nama)
            print("Data Nama Berhasil Dirubah")
        elif choice.lower() == "nilai":
            new_nilai = int(input("Masukkan Nilai Baru: "))
            student.set_nilai(new_nilai)
            print("Data Nilai Berhasil Dirubah")
    else:
        print("Objek belum dideklarasikan.")

# Fungsi untuk menghapus objek
def delete_object():
    global student  # Use the global variable
    if student:
        del student
        print("Data Berhasil Dihapus")
    else:
        print("Objek belum dideklarasikan.")

# Main program
student = None

while True:
    display_menu()
    choice = input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): ")

    if choice == "1":
        declare_object()
    elif choice == "2":
        display_object()
    elif choice == "3":
        modify_object()
    elif choice == "4":
        delete_object()
        student = None
    elif choice == "5":
        print("Terima Kasih Sudah Menggunakan Program Saya")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka 1-5.")
