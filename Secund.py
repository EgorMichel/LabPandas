import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Second/flights.csv", sep=',').astype({'WEIGHT': int, 'PRICE': int})

count = data['CARGO'].value_counts()
print(count)
res = data.groupby('CARGO').sum()[['PRICE', 'WEIGHT']]
print(res)

fig, axs = plt.subplots(1, figsize=(9, 9))
res.plot(kind='bar', ax=axs, title="name")
plt.show()
