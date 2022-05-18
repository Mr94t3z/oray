# library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

"""_first_
    Introduction to t-Test
"""

df = pd.read_csv(
    'https://raw.githubusercontent.com/Mr94t3z/pembelajaran-mesin/master/datasets/blood_pressure.csv')

df.info()

df.head()

mbp = df[df['sex'] == 'Male']['bp_after']
fbp = df[df['sex'] == 'Female']['bp_after']

print(round(mbp.mean(), 2))
print(round(fbp.mean(), 2))
print(round(mbp.mean()-fbp.mean(), 2))

"""_step 1_
    Buatlah hipotesis nol dan hipotesis alternatif
"""

"""_step 2_
    Tentukan tingkat signifikansi
"""

"""_step 3_
    Hitung Statistik Uji
"""

stats.ttest_ind(mbp, fbp)

t_stat, p_value = stats.ttest_ind(mbp, fbp)

print(f'The t-statistics of the test: {t_stat}')
print(f'The p-value of the test: {p_value}')

"""_step 4_
    Nilai-P dan Kesimpulan
"""

"""_last_
    Karena nilai p yang kami peroleh adalah 0,00109 < 0,005, 
    kita dapat menolak hipotesis null bahwa efek pengobatan 
    pada tekanan darah Pria dan Wanita adalah sama.
"""
