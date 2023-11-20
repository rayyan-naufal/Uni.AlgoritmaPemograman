def rekursif(jumlah, index=1, total=0):
    if index <= jumlah:
        angka = int(input(f"Masukkan bilangan ke-{index}: "))
        total += angka
        return rekursif(jumlah, index + 1, total)
    else:
        return total

jumlah_input = int(input("Masukkan Jumlah: "))
hasil_penjumlahan = rekursif(jumlah_input)
print(f"Hasil dari penjumlahan adalah: {hasil_penjumlahan}")
