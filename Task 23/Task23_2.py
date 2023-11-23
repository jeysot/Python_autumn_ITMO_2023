import psycopg2
import pandas as pd
con = psycopg2.connect(
    database = 'postgres',
    user = 'postgres',
    password = '1989',
    host = '127.0.0.1',
    port='5432'
)

cur = con.cursor()
cur.execute('Select * from task22_1')
rows = cur.fetchall()

# Часть1
columns = [desc[0] for desc in cur.description]
formatted_desc = [str(col).ljust(40) for col in columns]
print(*formatted_desc)

for row in rows:
    formatted_row = [str(value).ljust(40) for value in row]
    print(*formatted_row)

# Часть2
df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
print(df)

con.close