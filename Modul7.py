def check(p):
    if p % 10 == 1 and p != 11:
        hasil = (str(p) + "st")
    elif p % 10 == 2 and p != 12:
        hasil = (str(p) + "nd")
    elif p % 10 == 3 and p != 13:
        hasil = (str(p) + "rd")
    else:
        hasil = (str(p) + "th")
    return hasil

def ordinal_number():
    angka = " "
    while angka != "":
        angka = int( input("Masukan angka: "))
        if angka != 0:
            print(check(angka))
        else:
            print("Terima kasih telah menggunakan program saya")
            break
            
            
print(f"""
Ordinal Number
ketik 0 untuk menghentikan program
""")        
     
ordinal_number()

