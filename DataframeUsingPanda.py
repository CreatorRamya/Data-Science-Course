import pandas as pd
import numpy as np

exam_date = {'name': ['Yashasvi', 'Sakina', 'Elvira', 'Rooney', 'Tejashree', 'Alexandra', 'Zainab', 'Sai', 'Joshua', 'Tamara'],
             'score': [20, 8, 17.5, np.nan, 12, 15, 21.5, 19, 4, 10],
             'attempts': [1, 3, 2, 1, 2, 1, 1, 2, 3, 1],
             'qualify': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no' ]}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_date, index=labels)
print("A summary of the basic information about this Dataframe and its data:")
print(df.info())