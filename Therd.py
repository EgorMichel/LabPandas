import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)

info = pd.read_excel('Third/students_info.xlsx')
results = pd.read_html('Third/results_ejudge.html')[0]

data = info.merge(results, left_on='login', right_on='User').astype({'group_faculty': str, 'group_out': str})

fig, axs = plt.subplots(1, 2, figsize=(9, 6))
res = data.groupby('group_faculty').mean().loc[:, 'Solved']
res.plot(kind='bar', ax=axs[0], title="group_faculty")

res = data.groupby('group_out').mean().loc[:, 'Solved']
res.plot(kind='bar', ax=axs[1], title="group_out")

print(data.loc[data['H'] >= 10].loc[data['G'] >= 10])
plt.show()
