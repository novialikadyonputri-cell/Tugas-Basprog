#print ("nama : Novialika Dyon Putri")
#print ("NIM : 20220801374")
#print("Kelas : KJ101")

#Menghitung kecepatan jarak

#def hitung_kecepatan():
#    jarak = float(input('masukkan jarak ='))
#   waktu = float(input('masukkan waktu ='))
#    kecepatan = jarak * waktu
#    print("kecepatan :", kecepatan)
#hitung_kecepatan()

#Menghitung Konversi Detik

#detik = float(input('Masukkan nilai detik ='))
#menit = float(detik/60)
#jam = float(detik/3600)

#print (detik, 'detik diubah ke menit =', menit, 'menit')
#print (detik, 'detik diubah ke jam =', jam, 'jam')

#Menghitung Konversi jam

#jam = float(input('Masukkan nilai jam ='))
#menit = float(jam*60)
#detik = float(jam*3600)

#print (jam, 'jam diubah ke menit =', menit, 'menit')
#print (jam, 'jam diubah ke detik =', detik, 'detik')

#Menghitung Konversi Tahun

#tahun = int(input('Masukkan jumlah tahun ='))
#bulan = int(tahun*12)
#hari = int(tahun*365)

#print (tahun, 'tahun diubah ke bulan =', bulan, 'bulan')
#print (tahun, 'tahun diubah ke hari =', hari, 'hari')

#Menghitung Konversi Suhu, Input Celcius

#Celcius = float(input ("Masukkan Celcius ="))
#Reamur = float (0.8 * Celcius)
#Kelvin = float (Celcius + 273.15)
#Rankine = float (Celcius+273.15)*1.8

#print ('Derajat Reamur =', Reamur)
#print ('Derajat Fahrenheit =', Fahrenheit)
#print ('Derajat Kelvin =', Kelvin)
#print ('Derajat Rankine =', Rankine)

#Menghitung Konversi Suhu, Input Reamur

#Reamur = float(input ("Masukkan Reamur ="))
#Fahrenheit = float (2.25 * Reamur) + 32
#Kelvin = float (Reamur / 0.8) + 273.15
#Rankine = float (Reamur * 1.8) + 491.67
#Celcius = float(Reamur * 1.25)

#print ('Derajat Celsius =', Celcius)
#print ('Derajat Fahrenheit =', Fahrenheit)
#print ('Derajat Kelvin =', Kelvin)
#print ('Derajat Rankine =', Rankine)

#Menghitung Konversi Suhu, Input Fahrenheit

#Fahrenheit = float(input ("Masukkan Fahrenheit ="))
#Reamur = float (Fahrenheit - 32) * 4/9
#Kelvin = float (Fahrenheit - 32) * 5/9 + 273.15
#Rankine = float (Fahrenheit + 459.67)
#Celcius = float(Fahrenheit - 32) * 5/9

#print ('Derajat Celsius =', Celcius)
#print ('Derajat Reamur =', Reamur)
#print ('Derajat Kelvin =', Kelvin)
#print ('Derajat Rankine =', Rankine)

# Menghitung Konversi Suhu, Input Kelvin

#Kelvin = float(input("Masukkan Kelvin = "))

#Celcius = Kelvin - 273.15
#Reamur = (Kelvin - 273.15) * 4/5
#Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
#Rankine = Kelvin * 1.8

#print('Derajat Celcius =', Celcius)
#print('Derajat Reamur =', Reamur)
#print('Derajat Fahrenheit =', Fahrenheit)
#print('Derajat Rankine =', Rankine)

# Menghitung Konversi Suhu, Input Rankine

#Rankine = float(input("Masukkan Rankine = "))

#Fahrenheit = Rankine - 459.67
#Celcius = (Rankine - 491.67) * 5/9
#Reamur = (Rankine - 491.67) * 4/9
#Kelvin = Rankine * 5/9

#print('Derajat Celcius =', Celcius)
#print('Derajat Reamur =', Reamur)
#print('Derajat Fahrenheit =', Fahrenheit)
#print('Derajat Kelvin =', Kelvin)

Konversi Suhu (C, R, F, K, Rankine)

print("=== Program Konversi Suhu ===")
print("Pilih input suhu:")
print("1. Celcius (C)")
print("2. Reamur (R)")
print("3. Fahrenheit (F)")
print("4. Kelvin (K)")
print("5. Rankine (Ra)")

pilih = int(input("Masukkan pilihan (1-5): "))
nilai = float(input("Masukkan nilai suhu: "))

if pilih == 1:  # Input Celcius
    C = nilai
    R = C * 4/5
    F = C * 9/5 + 32
    K = C + 273.15
    Ra = (C + 273.15) * 9/5

elif pilih == 2:  # Input Reamur
    R = nilai
    C = R * 5/4
    F = R * 9/4 + 32
    K = R * 5/4 + 273.15
   Ra = (R * 5/4 + 273.15) * 9/5

#elif pilih == 3:  # Input Fahrenheit
#    F = nilai
#    C = (F - 32) * 5/9
#   R = (F - 32) * 4/9
#    K = (F - 32) * 5/9 + 273.15
#    Ra = F + 459.67

#elif pilih == 4:  # Input Kelvin
#    K = nilai
#    C = K - 273.15
#    R = (K - 273.15) * 4/5
#    F = (K - 273.15) * 9/5 + 32
#    Ra = K * 9/5

#elif pilih == 5:  # Input Rankine
#    Ra = nilai
#    K = Ra * 5/9
#    C = K - 273.15
#    R = (K - 273.15) * 4/5
#    F = Ra - 459.67

#else:
#    print("Pilihan tidak valid!")
#    exit()

#print("\n=== Hasil Konversi ===")
#print("Celcius     =", C)
#print("Reamur      =", R)
#print("Fahrenheit  =", F)
#print("Kelvin      =", K)
#print("Rankine     =", Ra)

# Konversi Waktu (Detik, Menit, Jam)

print("=== Program Konversi Waktu ===")
print("Pilih input waktu:")
print("1. Detik")
print("2. Menit")
print("3. Jam")

pilih = int(input("Masukkan pilihan (1-3): "))
nilai = float(input("Masukkan nilai waktu: "))

if pilih == 1:  # Input Detik
    detik = nilai
    menit = detik / 60
    jam = detik / 3600

elif pilih == 2:  # Input Menit
    menit = nilai
    detik = menit * 60
    jam = menit / 60

elif pilih == 3:  # Input Jam
    jam = nilai
    menit = jam * 60
    detik = jam * 3600

else:
    print("Pilihan tidak valid!")
    exit()

print("\n=== Hasil Konversi ===")
print("Detik =", detik)
print("Menit =", menit)
print("Jam   =", jam)
