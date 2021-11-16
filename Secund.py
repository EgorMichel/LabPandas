import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Second/flights.csv", sep=',').astype({'WEIGHT': int, 'PRICE': int})

count = data['CARGO'].value_counts()
print(count)
res = data.groupby('CARGO').sum()[['PRICE', 'WEIGHT']]
print(res)

fig, axs = plt.subplots(1, 2, figsize=(9, 3))

count = 0
for name in res:
    axs[count].bar(res.index.tolist(), res[name].tolist())
    axs[count].title.set_text(name)
    count += 1

plt.show()
