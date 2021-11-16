import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)

info = pd.read_excel('Third/students_info.xlsx')
results = pd.read_html('Third/results_ejudge.html')[0]

data = info.merge(results, left_on='login', right_on='User').astype({'group_faculty': str, 'group_out': str})

fig, axs = plt.subplots(1, 2, figsize=(9, 3))
res = data.groupby('group_faculty').mean().loc[:, 'Solved']
axs[0].bar(res.index.tolist(), res.tolist(), tick_label=[str(i) for i in res.index.tolist()])
axs[0].title.set_text('group_faculty')

res = data.groupby('group_out').mean().loc[:, 'Solved']
axs[1].bar(res.index.tolist(), res.tolist(), tick_label=[str(i) for i in res.index.tolist()])
axs[1].title.set_text('group_out')

result = data[data['H'] >= 10]
print(result[result['G'] >= 10])
plt.show()
