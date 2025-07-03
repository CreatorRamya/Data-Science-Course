import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.info())\
print(df.describe())
print(df.columns)

print(df['Name'])
print(df[['Name', 'Age']])
print(df[df['Age'] > 25])

df['Salary'] = [50000, 60000, 55000, 65000]

df.at[0, 'City'] = 'Boston'

df.rename(columns={'Name': 'Full Name'}, inplace=True)

print(df)

df.at[2, 'Salary'] = None

df['Salary'].fillna(0, inplace=True)

df.dropna(inplace=True)

print(df.groupby('City')['Age'].mean())

print(df['City'].value_counts())

print(df.sort_values(by='Age'))

print(df.sort_values(by='Salary', ascending=False))

df.to_csv('students.csv', index=False)

df_loaded = pd.read_csv('students.csv')
print(df_loaded)
