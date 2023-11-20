def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_user_input():
    while True:
        try:
            user_input = int(input("Masukkan angka: "))
            return user_input
        except ValueError:
            print("Masukkan harus berupa angka.")

def main():
    angka = get_user_input()
    if is_prime(angka):
        print(f"{angka} adalah bilangan prima.")
    else:
        print(f"{angka} bukan bilangan prima.")

if __name__ == "__main__":
    main()
