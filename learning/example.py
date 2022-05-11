"""def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)"""


"""foo = long_function_name(
    var_1, var_two,
    var_3, var_four)
"""


"""
Tipe numerik pada Python dibagi menjadi 3: int, float, complex.
"""
# Numbers
"""a = 10
print(a, "bertipe", type(a))
b = 1.7
print(b, "bertipe", type(b))
c = 1+2j
print(c, " Bertipe bilangan kompleks? ", isinstance(1+2j, complex))"""

"""x = [0]*10005  # inisialisasi array 0 sebanyak 10005; x[0]=0
x[1] = 1  # x[1]=1

for j in range(2, 10001):
    x[j] = x[j-1]+x[j-2]  # Fibonacci
print(x[10000])"""

"""x = [1, 2, 3]
x[2] = 4
x.append(5)
print(x)"""

"""binatang = ['kucing', 'rusa', 'badak', 'gajah']

del binatang[2]

print(binatang)

del binatang[2]

print(binatang)"""

"""s = "Hello World!"
print(s[4])  # ambil karakter kelima dari string s
print(s[6:11])  # ambil karakter ketujuh hingga sebelas dari string s
s[5] = "d"  # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
# ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
s = "Halo Dunia!"
print(s)"""

"""print('hai {}'.format('bro'))"""

"""nama = "Dicoding"
print("Halo, %s!" % nama)"""

"""nama = "Dicoding"
umur = 5
print("Umur %s adalah %d tahun." % (nama, umur))"""

"""angka = [7, 9, 11, 13]
print("Angka saya: %s" % angka)"""

"""import sys
print('Jumlah arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print(sys.argv[1])"""

"""print([_ for _ in range(0, 20, 5)])"""

"""a = 6
b = 4
print("Hasilnya " + str(a + b) + "6" * 3)"""

"""kalkulator"""
"""
class Kalkulator:
    #kalkulator tambah kurang

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i): return self.i + _i

    def kurang(self, _i):
        return self.i - _i

"""

"""flowers = ['mawar', 'melati', 'anggrek']
for index in range(len(flowers)):
    print('Flowers: {}'.format(flowers[index]))
"""

"""for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()"""

"""for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))
"""

"""for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print()
            break
        else:
            print("*", end="")
"""

"""for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
"""

"""jumlahbaris = 10
baris = 0
bintang = 0
while baris < jumlahbaris:
    if (bintang) >= (baris+1):
        print()
        baris = baris+1
        bintang = 0
        continue  # saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*", end="")
    bintang = bintang+1"""

"""import sys
data = ''
while(data != 'exit'):
    try:
        data = input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))"""

"""# Cara 2 List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)"""


"""# Contoh3 menemukan item yang ada di kedua list
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
    for b in list2:
        if a == b:
            duplikat.append(a)

print(duplikat)  # Output ['d','i']"""

"""# Contoh4 Implementasi dengan list comprehension
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat)  # Output: ['d','i']"""

# Contoh 5 kecilkan semua huruf
"""list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)"""

"""list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)"""

# condition_if_true if condition else condition_if_false
"""if (condition):
      condition_if_true
else:
      condition_if_false"""

"""
def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))


# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i': 7, 'j': 8})
"""

"""
def kali(nilai1, nilai2): return nilai1 * nilai2

print("Hasil : ", kali(11, 21))
print("Hasil : ", kali(2, 2))
"""

"""
def penjumlahan(a, b):
    a+b

hasil = penjumlahan(10, 10)
print(hasil)
"""

"""
#import unittest

class TestStringMethods(unittest.TestCase):

    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == '__main__':
    unittest.main()
"""

"""
def test_isalnum(self):
    self.assertTrue('c0d1ng'.isalnum())  # ini akan berhasil
    self.assertTrue('c0d!ng'.isalnum())  # ini akan gagal
"""


"""
import unittest
def koneksi_ke_db():
    print('[terhubung ke db]')


def putus_koneksi_db(db):
    print('[tidak terhubung ke db {}]'.format(db))


class User:
    username = ''
    aktif = False

    def __init__(self, db, username):  # using db sample
        self.username = username

    def set_aktif(self):
        self.aktif = True


class TestUser(unittest.TestCase):
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, 'dicoding')
        self.assertFalse(dicoding.aktif)  # tidak aktif secara default
        putus_koneksi_db(db)

    def test_user_is_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, 'dicoding')
        dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(dicoding.aktif)
        putus_koneksi_db(db)


if __name__ == '__main__':
    unittest.main()
"""

"""
# contoh JSON:
import json
x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'

# parse  x:
y = json.loads(x)

print(y["umur"])
"""

"""
import re
pola = '^a...s$'
string_tes = 'abyss'
hasil = re.match(pola, string_tes)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.")
"""

"""
#import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true',
                    help="tampilkan output")
args = parser.parse_args()

if args.output:
    print("Halo, ini merupakan sebuah output dari panggildicoding.py")

# python3 namafile.py -o
"""

"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
args = parser.parse_args()

print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama)

# python3 example.py -n or --nama Nama
"""

"""
a = 5.5
print(a, "is of type", type(a))
"""

"""
x = [10, 15, 20, 25, 30]
print(x[-3:])
"""

"""animal = ['cat', 'rabbit', 'tiger', 'wolf']
del animal[1]
print(animal)"""


"""d = "Halo Dicoding!"
print(d[5:13])
"""

"""x = 300
print(str(x).zfill(5))
"""

"""
a, b = 10, 11
a, b
print('%x and %X' % (a, b))

x = [10, 20, 30, 40, 50, 60, 70, 80]
print(x[5:])
"""

"""# my_set = (0, 'apple', 3.5).to_set()

my_set = {0, 'apple', 3.5}
print(my_set)

# my_set = (0, 'apple', 3.5).set()"""

"""
import math
print(math.pow(2, 10))  # prints 2 elevated to the 10th power
"""

"""
#import numpy as np
a = np.arange(100)
b = a[50:60:2]

print(b)
"""

"""characters = ["Iron Man", "Spider Man", "Captain America"]
# example output : [("Iron Man", "Downey), ("Spider Man", "Holland"), ("Captain America", "Evans")]
actors = ["Downey", "Holland", "Evans"]

p = [(x, y) for x in characters for y in actors]
print(p)"""

"""animals = {'a': ['ant', 'antelope', 'armadillo'], 'b': [
    'beetle', 'bear', 'bat'], 'c': ['cat', 'cougar', 'camel']}
animals = defaultdict(list, animals)
print(animals['b'])
print(animals['d'])"""

"""my_dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
letters = list(my_dictionary)
print(letters)
"""

"""
num_list = [21, 13, 19, 3, 11, 5, 18]
num_list.sort()
num_list[len(num_list) // 2]
print(num_list)
"""

"""import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a*b
d = np.dot(a, b)
print(d)
"""

"""
num_list = [1, 2, 3, 4, 5]
num_list.remove(2)
print(num_list)
"""

l = list(reversed(range(1, 11)))
print(l)
