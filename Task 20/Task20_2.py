import pandas as pd

def sum_numbers_in_dataframe(dataframe):
    numeric_dataframe = dataframe.map(pd.to_numeric, errors='coerce')
    total_sum = numeric_dataframe.stack().sum(skipna=True)
    return total_sum


data = {'col1': [1, '2', 'three', 4],
        'col2': ['five', 6, 7, '8']}
df = pd.DataFrame(data)


result = sum_numbers_in_dataframe(df)
print("Сумма всех чисел в DataFrame:", result)
