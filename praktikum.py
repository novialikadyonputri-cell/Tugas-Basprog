print('FORM PENDAFTARAN MAHASISWA BARU')
program_studi = input('Masukkan nama program studi yang dipilih : ')
kelas = input('Masukkan kelas yang dipilih (reguler, non-reguler, beasiswa) : ')
nama = input('Masukkan nama lengkap : ')
ttl = input('Masukkan tempat / tanggal lahir : ')
jenis_kelamin = input('Masukkan jenis kelamin (p/l) : ')
agama = input('Masukkan Agama : ')
status = input('Masukkan status perkawinan : ')
alamat = input('Masukkan alamat lengkap : ')
no_hp = input('Masukkan nomor telepon : ')
email = input('Masukkan email aktif : ')

print('DATA PENDAFTARAN GELOMBANG MASUK')
gelombang = int(input('Masukkan gelombang pendaftaran (1/2/3): '))

GelombangSatu = [20, 5, 0.5, 0.2]
GelombangDua = [21, 6, 0.5, 0.2]
GelombangTiga = [22, 8, 0.5, 0.2]

if gelombang == 1:
    detail = GelombangSatu
elif gelombang == 2:
    detail = GelombangDua
elif gelombang == 3:
    detail = GelombangTiga
else:
    detail = []
    print('Gelombang tidak valid!')

print('\nBIODATA MAHASISWA')
print('Program studi       :', program_studi)
print('Kelas               :', kelas)
print('Nama lengkap        :', nama)
print('Tempat/Tanggal lahir:', ttl)
print('Jenis kelamin       :', jenis_kelamin)
print('Agama               :', agama)
print('Status perkawinan   :', status)
print('Alamat lengkap      :', alamat)
print('No. telepon         :', no_hp)
print('Email               :', email)
print('Gelombang masuk     :', gelombang)


# 🔹 Definisi fungsi
def info_tagihan(detail):
    if detail:
        print('\nRINCIAN TAGIHAN (dalam juta):')
        keterangan = ['Uang Pangkal', 'SPP', 'Almamater', 'Formulir']

        total = 0
        for i in range(len(detail)):
            print(f"{keterangan[i]} : {detail[i]} juta")
            total += detail[i]

        print('-------------------------------')
        print('Total Tagihan :', total, 'juta')
    else:
        print('Tidak ada data tagihan karena gelombang tidak valid.')
        return 0


# 🔹 Pemanggilan fungsi HARUS ada
info_tagihan(detail)
