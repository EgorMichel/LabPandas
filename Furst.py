import pandas as pd
data = pd.read_csv("First/transactions.csv", sep=',')
data = data[data['STATUS'] == 'OK'].astype({'SUM': int}).sort_values(by=['SUM'], ascending=False)
print(data.iloc[0:3, :])
print(data[data['CONTRACTOR'] == 'Umbrella, Inc'].loc[:, 'SUM'].sum())
