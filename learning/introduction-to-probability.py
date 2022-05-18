import numpy as np

"""_soal 1_
    Bayangkan Anda memiliki koin dolar, Apa itu?
    Peluang mendapatkan heads setelah melempar koin?
    P(Heads) = 1/2
"""
coin = ['heads', 'tails']
np.random.choice(coin)

count = 0
total_flips = 10000

for i in range(total_flips):
    # Check if coin is heads
    if np.random.choice(coin) == 'heads':
        count += 1

print('Hasil soal 1 =', count/total_flips)

"""_soal 2_
    Berapa probabilitas mendapatkan 2 dari yang sama?
    dadu 6 sisi?
    P(Getting 2 in 1 roll) = 1/6
"""
dice = [1, 2, 3, 4, 5, 6]

count = 0
total_throws = 10000

for i in range(total_throws):
    # Check if dice is 2
    if np.random.choice(dice) == 2:
        count += 1

print('Hasil soal 2 =', count/total_throws)

"""_lanjutan soal 2_
    Berapa peluang muncul dan angka ganjil pada pelemparan sebuah dadu?
    P(Odd Number) = 3/6 = 1/2
"""
# Buat variabel bernama count yang dimulai dari 0.
count = 0

# Saya ingin menjalankan eksperimen saya 10.000 kali.
for i in range(total_throws):

    # Saya ingin memeriksa apakah lemparan dadu saya ganjil.
    if np.random.choice(dice) % 2 != 0:

        # Jika itu benar, maka tambahkan 1 untuk count.
        count += 1

# Cetak berapa kali A muncul, dibagi n.
print('Hasil lanjutan soal 2 =', count/total_throws)

"""_soal 3_
    Anda memiliki 3 koin berbobot sama. Berapa probabilitas 
    membalik semua Heads atau semua Tails?
    
    Hasil Semua Kemungkinan:
    -HHH
    -HHT
    -HTH
    -HTT
    -THH
    -THT
    -TTH
    -TTT
    
    P(All same) =  2/8 = 1/4
"""
coin = ['heads', 'tails']


def all_same(n):

    # Siapkan counter untuk melihat berapa banyak
    # keberhasilan yang kita dapatkan.
    count = 0

    # Jalankan eksperimen n kali.
    for i in range(n):

        # Lemparan koin pertama.
        first_toss = np.random.choice(coin)

        # Lemparan koin kedua.
        second_toss = np.random.choice(coin)

        # Lemparan koin ketiga.
        third_toss = np.random.choice(coin)

        # Jumlah 'heads'. Ingat Boolean True == 1 dan False == 0
        num_heads = (first_toss == 'heads') + \
            (second_toss == 'heads') + (third_toss == 'heads')

        # Jumlah 'tails'.
        num_tails = (first_toss == 'tails') + \
            (second_toss == 'tails') + (third_toss == 'tails')

        # Periksa apakah num_heads/num_tails = 3,
        # yang berarti semua heads atau semua tails
        if (num_heads == 3) or (num_tails == 3):
            count += 1

    return count / n


# menjalankan percobaan sebanyak 10.000 kali.
print('Hasil soal 3 =', all_same(10000))

"""_soal 4_
    Apa yang telah kita lihat di atas adalah ruang 
    sampel yang merupakan semua hasil yang mungkin:
    
    Himpunan adalah segala sesuatu di dalam suatu kelompok. 
    Dan notasi matematika adalah untuk merangkumnya dalam kurung kurawal.
    
    Sample Space =  {50 employees, 30 desks, 2 offices, 1 pantry, \
        2 company cars, 10 vans, 25 computers, 10 laptops}
    companyA = {50 employees, 2 company cars, 10 vans, \
        30 desks, 25 computers}
    companyB = {50 employees, 30 desks, 2 offices, 1 pantry}
    
    
"""

"""_rumus_
    companyA ∩ companyB
    companyA ∪ companyB
        companyA'
    (companyA ∪ companyB)'
"""

"""_jawaban_
    {50 employees, 30 desks}
    {50 employees, 2 company cars, 10 vans, 25 computers, 2 offices, 1 pantry}
    {2 offices, 1 pantry, 10 laptops}
    {10 laptops}
"""
