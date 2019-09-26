import pandas as pd
from env import host, user, password
url = f'mysql+pymysql://{user}:{password}@{host}/employees'
df = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
print(df)


import pandas as pd
from env import host, user, password

database_name = "sakila"

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

query = """ SELECT * FROM actor WHERE first_name = 'penelope' """

df = pd.read_sql(query, url)

print(df)


groupby != dataframe unless .agg('measurement')

