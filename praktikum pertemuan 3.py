#i = 1
#while i <= 15:
#    print(i)
#    if i % 3 == 0 and i % 5 == 0:
#        print("Fizz Buzz")
#    elif i % 3 == 0:
#        print('Fizz')
#    elif i % 5 == 0:
#        print ('Buzz')
#    i += 1

#i = 1
#for i in range (16):
#    print(i)
#    if i % 3 == 0 and i % 5 == 0:
#        print("Fizz Buzz")
#    elif i % 3 == 0:
#        print('Fizz')
#    elif i % 5 == 0:
#        print ('Buzz')
#    i += 1

#animals = ["Kodok acumalakama", "kucing", "anjing"]
#for x in animals:
#    print(x)

#def ini_fungsi(fname, lname):
#  return lname

#nama = ini_fungsi ('Novialika', 'dyon putri')
#print(nama)

#tambah saldo
#def tambah_saldo(saldo_awal, saldo_masuk):
#  return saldo_awal + saldo_masuk

#total_saldo = tambah_saldo (20000, 100000)
#print (total_saldo)


#kurangi saldo
#def kurang_saldo(saldo_awal, saldo_keluar):
#  return saldo_awal - saldo_keluar

#total_saldo = kurang_saldo (20000, 1000)
#print (total_saldo)

#while True :
#    nilai = float(input('Masukkan nilai ='))
#    if (nilai>=60):
#        print ("selamat anda lulus")
#        break
#else:
#    print("tetap semangat, anda gagal")

#rows = int(input("input rows: "))

#for i in range(1, rows, 1):
#    print(" " * (rows - i), end="")
#    for j in range(i):
#        print(2 * j + 2, end=" ")
#    print()

#rows = int(input("input rows: "))

#for i in range(rows, 1, -1):
#    print(" " * (rows - i), end="")
#    for j in range(i):
#        print(2 * j + 2, end=" ")
#    print()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits_even(num):
    total = sum(int(digit) for digit in str(num))
    return total % 2 == 0

N = int(input("Masukkan bilangan bulat positif (>3): "))

print(f"Bilangan Komposit Cantik ≤ {N} adalah:")

for i in range(4, N + 1):  # mulai dari 4 karena 4 komposit pertama
    if not is_prime(i) and sum_of_digits_even(i):
        print(i)
