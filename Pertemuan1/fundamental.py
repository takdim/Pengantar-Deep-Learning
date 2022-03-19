#Belajar Pemrograman Python

#langkah awal ialah dengan memasang python pada komputer masing-masing
#dengan menyiapkan teks editor ataupun IDE, maka telah siap untuk melakukan pembelajaran python

#langkah pertama dalam mempelajari python ialah sebagai berikut
#Mencetak hello
print("hello")
#dengan catatan : bahwa ekstensi file akan di simpan dengan ekstensi .py


#Penulisan statemen python
print("Hello World!")
print("Belajar Python dari Nol")
nama = "aiimmm"
print(nama)

#Penulisan String pada Python
judul = "Belajar Pemrograman Python sampai Bisa"
penulis = 'aiimmm'

#atau bisa juga sebagai berikut
judul = """Belajar Python dengan Cepat"""
penulis = '''aiimmm'''

#Penulisan Blok Program Python
# blok percabangan if
username = "petanikode"
if (username == 'petanikode'):
    print("Selamat Datang")
    print("Silahkan ambil tempat duduk")

# blok percabangan for
for i in range(10):
    print(i)

#Cara Penulisan Komentar pada Python
#contoh 1 dengan menggunakan #:
# ini adalah komentar
# Ini juga komentar

#dengan menggunakan tanda petik
"Ini adalah komentar dengan tanda petik ganda"
'Ini juga komentar, tapi dengan tanda petik tunggal'
#dengan menggunakan triple tanda petik
"""ini contoh penggunaan komentar"""

#Mengenal Tipe Data
#Variabel merupakan tempat menyimpan data, sedangkan tipe data adalah jenis data yang terseimpan dalam variabel.

#Aturan Penulisan Variabel

#1. Nama variabel boleh diawali menggunakan huruf atau garis bawah (_), contoh: nama, _nama, namaKu, nama_variabel.
#2. Karakter selanjutnya dapat berupa huruf, garis bawah (_) atau angka, contoh: __nama, n2, nilai1.
#3. Karakter pada nama variabel bersifat sensitif (case-sensitif). Artinya huruf besar dan kecil dibedakan. Misalnya, variabel_Ku dan variabel_ku, keduanya adalah variabel yang berbeda.
#4. Nama variabel tidak boleh menggunakan kata kunci yang sudah ada dalam python seperti if, while, for, dsb.

#Tipe data
nama_ku = "aiimmm" #<<string
umur = 20 #<< integer
tinggi = 183.22 #<< float
jenis_kelamin = 'L' #<< char
menyala = True #<< boolean

#Mengenal Jenis Operator dalam Python

#Operator Aritmatika

# Ambil input untuk mengisi nilai
a = 8
b = 5

# Menggunakan operator penjumlahan
c = a + b
print ("Hasil %d + %d = %d" % (a,b,c))

# Operator Pengurangan
c = a - b
print ("Hasil %d - %d = %d" % (a,b,c))

# Operator Perkalian
c = a * b
print ("Hasil %d * %d = %d" % (a,b,c))

# Operator Pembagian
c = a / b
print ("Hasil %d / %d = %d" % (a,b,c))

# Operator Sisa Bagi
c = a % b
print ("Hasil %d %% %d = %d" % (a,b,c))

# Operator Pangkat
c = a ** b
print ("Hasil %d ** %d = %d" % (a,b,c))

#Operator Penugasan
umur = 18
# Ambil input untuk mengisi nilai
a = 10
# ^ 
# | contoh operator penugasan untuk mengisi nilai

print ("Nilai a = %d" % a)

# Coba kita jumlahkan nilai a dengan opertor penugasan
a += 5
# ^
# |
# contoh operator penugasan untuk menjumlahkan

# Setelah nilai a ditambah 5, coba kita lihat isinya
print ("Nilai setelah ditambah 5:")
print ("a = %d" % a)

# tambahkan dengan 2
a += 2

# kurangi 3
a -= 3

# kali 10
a *= 10

# bagi dengan 4
a /= 4

# pangkat 10
a **= 10

# Berapakah nilai a sekarang?
print ("Nilai a adalah %d" % a)

#Operator Pembanding
a = 10
b = 8

# apakah a sama dengan b?
c = a == b
print ("Apakah %d == %d: %r" % (a,b,c))

# apakah a < b?
c = a < b
print ("Apakah %d < %d: %r" % (a,b,c))

# apakah a > b?
c = a > b
print ("Apakah %d > %d: %r" % (a,b,c))

# apakah a <= b?
c = a <= b
print ("Apakah %d <= %d: %r" % (a,b,c))

# apakah a >= b?
c = a >= b
print ("Apakah %d >= %d: %r" % (a,b,c))

# apakah a != b?
c = a != b
print ("Apakah %d != %d: %r" % (a,b,c))

#Operator Logika

a = True
b = False

# Logika AND
c = a and b
print ("%r and %r = %r" % (a,b,c))

# Logika OR
c = a or b
print ("%r or %r = %r" % (a,b,c))

# Logika Not
c = not a
print ("not %r  = %r" % (a,c))

#Operator Bitwise
a = 4
b = 5

# Operasi AND
c = a & b
print ("a & b = %s" % c)

# Operasi OR
c = a | b
print ("a | b = %s" % c)

# Operasi XOR
c = a ^ b
print ("a ^ b = %s" % c)

# Operasi Not
c = ~a
print ("~a = %s" % c)

# Operasi shift left (tukar posisi biner)
c = a << b
print ("a << b = %s" % c)

# Operasi shift right (tukar posisi biner)
c = a >> b 
print ("a >> b = %s" % c)
