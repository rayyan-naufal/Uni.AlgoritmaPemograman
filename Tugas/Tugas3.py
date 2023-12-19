def is_palindrome(s):
    # Menghilangkan spasi dan mengubah ke huruf kecil
    cleaned_str = ''.join(s.lower().split())
    
    start = 0
    end = len(cleaned_str) - 1
    
    while start < end:
        if cleaned_str[start] != cleaned_str[end]:
            return False
        start += 1
        end -= 1

    return True

kata = input('Masukkan Sebuah Kalimat: ')

if is_palindrome(kata):
    print(f'Kalimat "{kata}" adalah palindrom.')
else:
    print(f'Kalimat "{kata}" bukan palindrom.')
