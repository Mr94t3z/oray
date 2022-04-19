# data keuangan
keuangan = {
    'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
    'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}

avg_pengeluaran = sum(keuangan['pengeluaran'])/len(keuangan['pengeluaran'])
avg_pemasukan = sum(keuangan['pemasukan'])/len(keuangan['pemasukan'])
print(avg_pengeluaran)
print(avg_pengeluaran)

# other solution
"""
all_pengeluaran = 0
all_pemasukan = 0

for i in keuangan['pengeluaran']:
    all_pengeluaran += i
for i in keuangan['pemasukan']:
    all_pemasukan += i

avg_pengeluaran = all_pengeluaran / len(keuangan['pengeluaran'])
avg_pemasukan = all_pemasukan / len(keuangan['pemasukan'])

print(avg_pengeluaran)
print(avg_pemasukan)
"""
