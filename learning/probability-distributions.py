# library
from scipy.integrate import simps
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import pandas as pd

"""_first_
    Discrete Uniform Distributon and
    Probability Mass Function
"""

dice_sides = list(range(1, 7))

dice_probability = [1/6]*6
plt.figure(1)

# Rename the labels from 1-6
plt.xticks(ticks=dice_sides, labels=[
           'one', 'two', 'three', 'four', 'five', 'six'])
# plt.show()

"""_contoh 1_
    Cumulative Distribution Function (CDF)
"""

# print(np.cumsum([1, 2, 3]))

plt.figure(2)
plt.step(dice_sides, np.cumsum(dice_probability))

# Rename the labels from 1-6
plt.xticks(ticks=dice_sides, labels=[
           'one', 'two', 'three', 'four', 'five', 'six'])

# plt.show()

"""_contoh 2_
    Bernoulli Distribution
"""

coin_outcomes = ['Heads', 'Tails']
coin_probability = [1 - .3, .3]

plt.figure(3)
plt.bar(coin_outcomes, coin_probability)

# plt.show()

"""_contoh 3_
    Binomial Distribution
"""

probability_heads = .7
n_flips = 50

coin_distribution = stats.binom(n_flips, probability_heads)
head_probabilities = list(range(0, 51))

plt.figure(4)
plt.bar(head_probabilities, coin_distribution.pmf(
    head_probabilities), color='orange')

# plt.show()

"""_contoh 4_
    Poisson Distribution
"""

n_diners = 20

diner_distribution = stats.poisson(n_diners)

possible_diners = list(range(50))
plt.figure(5)
plt.bar(possible_diners, diner_distribution.pmf(
    possible_diners), color='green')

# plt.show()

"""_second_
    Probability Density Function and
    Normal Distribution
"""

# Function to get pdf or cdf and percentiles


def plot_distn(rv, lb, ub, kind='pdf',
               percentile=np.nan, display=False):  # rv: random variable

    # range equivalent to start from lower bound to upper bound
    xs = np.linspace(lb, ub, 1000)

    if kind == 'pdf':    # probability density function
        ys = rv.pdf(xs)  # f(x)
    elif kind == 'cdf':  # cumulative density function
        ys = rv.cdf(xs)  # F(x)

    fig, ax = plt.subplots()
    plt.plot(xs, ys, linewidth=3, color='blue')

    # Display percentiles
    if kind == 'pdf' and percentile != np.nan and display == True:
        mu = 527
        sigma = 112

        # define the normal distribution and PDF
        dist = stats.norm(loc=mu, scale=sigma)

        ax.axvline(dist.ppf(percentile/100), color='red',
                   label=f'{dist.ppf(percentile/100)}')
        ax.legend()
        # plt.show()


normal_distribution = stats.norm(527, 112)

plot_distn(normal_distribution, 0, 1000)

# Score to score 5%
plot_distn(normal_distribution, 0, 1000, percentile=95, display=True)

plot_distn(normal_distribution, 0, 1000, kind='cdf')

# plt.show()

"""_third_
    Central Limit Theorem
"""

df = pd.read_csv('./train.csv')

# print(df.head())

# print(df['Age'].values)

# defining custom function


def distribution_plotter(sample_variable):
    ax = sns.displot(sample_variable, bins=50, kde=True)


distribution_plotter(df.Age)
# plt.show()

sample_mean = [np.mean(np.random.choice(df.Age, size=30))
               for random in range(1000)]
# print(sample_mean)

distribution_plotter(sample_mean)
# plt.show()

sample_mean1 = [np.mean(np.random.choice(df.Age, size=30))
                for random in range(1000)]
# print(sample_mean1)

distribution_plotter(sample_mean1)
# plt.show()

sample_mean2 = [np.mean(np.random.choice(df.Age, size=30))
                for random in range(1000)]
# print(sample_mean2)

distribution_plotter(sample_mean2)
plt.show()
