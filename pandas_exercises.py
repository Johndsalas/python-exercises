# Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

from pydataset import data
import pandas as pd


mpg = data('mpg')

mpg.info()

#On average, which manufacturer has the best miles per gallon?
mpg['average_mileage'] = mpg[['cty', 'hwy']].mean(axis=1)

mpg1 = mpg.groupby('manufacturer').agg('mean')

mpg1[['average_mileage']].sort_values('average_mileage', ascending=False).head(1)

#How many different manufacturers are there?

mpg1.shape[0]

#How many different models are there?

mpg_models = mpg.groupby('model').agg('mean')

mpg_models[[]]

mpg_models.shape[0]

#Do automatic or manual cars have better miles per gallon?

trans_mile = mpg[['trans','average_mileage']]

mpg=mpg.assign(trans_2=trans_mile.trans.apply(lambda n: n[:-4]))

mpg.groupby('trans_2')['hwy'].mean()

# Joining and Merging
# Copy the users and roles dataframes from the examples above.

import pandas as pd
import numpy as np

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# What do you think a right join would look like? 

pd.merge(users, roles, left_on='role_id', right_on='id', how='right')

#An outer join? 
pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')

# What happens if you drop the foreign keys from the dataframes and try to merge them?
#users = users.drop(['id', 'role_id'], axis=1)
#roles = roles.drop(['id'], axis=1)
                   
pd.merge(users, roles,how='outer')

# Create a function named get_db_url. It should accept a username, hostname, password, and database name 
# and return a url formatted like in the examples in this lesson.
# Use your function to obtain a connection to the employees database.


import pandas as pd
from env import host, user, password

database = "sakila"

def get_db_url(user,host,password,database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
    return url

url = get_db_url(user,host,password,database)

database_name = "sakila"
query = """ SELECT * FROM actor """

df = pd.read_sql(query, url)

print(df)

# Once you have successfully run a query:
# Intentionally make a typo in the database url. What kind of error message do you see?
'''
NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:myssql.pymysql
'''
# Intentionally make an error in your SQL query. What does the error message look like?
'''
ProgrammingError: (pymysql.err.ProgrammingError) (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ROM actor' at line 1")
[SQL:  SELECT * ROM actor ]
(Background on this error at: http://sqlalche.me/e/f405)
'''
# Read the employees and titles tables into two separate dataframes

import pandas as pd
from env import host, user, password

def get_db_url(user,host,password,database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
    return url

# get database for employees
database = "employees"
url = get_db_url(user,host,password,database)

query = """ SELECT * FROM employees """

df_emp = pd.read_sql(query, url)


# get database for title 
database_name = "employees"
url = get_db_url(user,host,password,database)

query = """ SELECT * FROM titles """

df_tab = pd.read_sql(query, url)

# print data bases
print(df_emp)

print(df_tab)

# Visualize the number of employees with each title.

emp_tab = pd.merge(df_emp,df_tab, left_on='emp_no', right_on='emp_no', how='inner')

emp_tab_group = emp_tab.groupby('title').agg('count')

print(emp_tab_group[['emp_no']])

# Join the employees and titles dataframes together.

emp_tab = pd.merge(df_emp,df_tab, left_on='emp_no', right_on='emp_no', how='right')

print(emp_tab)

# Visualize how frequently employees change titles.



# For each title, find the hire date of the employee that was hired most recently with that title.

emp_tab_hire = emp_tab.groupby('title').agg('max')

print(emp_tab_hire[['hire_date']])
# Write the code necessary to create a cross tabulation of the number of titles by department.
# (Hint: this will involve a combination of SQL and python/pandas code)
import pandas as pd
from env import host, user, password

def get_db_url(user,host,password,database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
    return url

# get database for employees
database = "employees"
url = get_db_url(user,host,password,database)

query = """ SELECT * FROM departments """

df_departments = pd.read_sql(query, url)
print(df_departments)

department_count =df_departments.groupby('dept_name').agg('count')
print(department_count)

titles_count = emp_tab.groupby('title').agg('count')[['emp_no']]
print(titles_count)

title_per_dept = pd.crosstab(department_count,titles_count)


# Use your get_db_url function to help you explore the data from the chipotle database.
# Use the data to answer the following questions:

import pandas as pd
from env import host, user, password

def get_db_url(user,host,password,database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
    return url

# get database for employees
database = "chipotle"
url = get_db_url(user,host,password,database)

query = """ SELECT * FROM orders """

df_chipotle = pd.read_sql(query, url)
print(df_chipotle)

# What is the total price for each order?

df_chipotle['item_price'] = df_chipotle.item_price.apply(lambda n: float(n.replace('$','')))

df_chipotle

df_price_per_order = df_chipotle.groupby('order_id').agg('sum')[['item_price']]

df_price_per_order


# What are the most popular 3 items?

df_chipotle_popular =  df_chipotle.groupby('item_name').agg(sum).sort_values('quantity', ascending=False)[['quantity']]

df_chipotle_popular.head(3)
# Which item has produced the most revenue?

df_chipotle_revenue = df_chipotle.groupby('item_name').agg(sum).sort_values('item_price', ascending=False)[['item_price']]

df_chipotle_revenue.head(1)

