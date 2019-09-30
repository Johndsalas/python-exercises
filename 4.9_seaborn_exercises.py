# Create a file named 4.9_seaborn_exercises.py for this exercise.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
# Use the iris database to answer the following quesitons:
from env import host, user, password

database = "iris_db"

def get_db_url(user,host,password,database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
    return url

url = get_db_url(user,host,password,database)

database_name = "iris_db"
query = """ SELECT * FROM measurements """

im = pd.read_sql(query, url)

print(im.head(1))


# What does the distribution of petal lengths look like?

std_petal_length = im.petal_length.std()

std_petal_length

# Is there a correlation between petal length and petal width?

lenght_width_correlation = im['petal_length'].corr(im['petal_width'])

print(lenght_width_correlation)

# Would it be reasonable to predict species based on sepal width and sepal length?

means_by_species = im.groupby('species_id').agg('mean')

means_by_species

std_by_species = im.groupby('species_id').agg('std')

std_by_species
'''
No, defference between average sepal length of species is too small.
'''

# Which features would be best used to predict species?

means_by_species = im.groupby('species_id').agg('mean')

means_by_species

std_by_species = im.groupby('species_id').agg('std')

std_by_species
'''
measurement id values are grater than two standard deveation apart
''' 
# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. 
# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. 
# What do you notice?

a = sns.load_dataset('anscombe')

x = a['x'].describe()

y = a['y'].describe()

# Plot the x and y values from the anscombe data. 
# Each dataset should be in a separate column.

sns.distplot(a.x)

sns.distplot(a.y)

sns.relplot(x='x', y='y',data=a)

# Load the InsectSprays dataset and read it's documentation. 
# Create a boxplot that shows the effectiveness of the different insect sprays.
from pydataset import data

i = data('InsectSprays')

i

from pydataset import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

# Load the InsectSprays dataset and read it's documentation. 
# Create a boxplot that shows the effectiveness of the different insect sprays.
from pydataset import data

i = data('InsectSprays')

i

#plt.subplot(223)
sns.boxplot(data=i, y='count', x='spray')
plt.title('Effectiveness of Insect Sprays')


# Load the swiss dataset and read it's documentation. 
# Create visualizations to answer the following questions:

s = data('swiss')

s

# Create an attribute named is_catholic 
# that holds a boolean value of whether or not the province is Catholic. 
# (Choose a cutoff point for what constitutes catholic)

s['is_catholic'] = s.Catholic > 50

s

# Does whether or not a province is Catholic influence fertility?

s.corr(method ='pearson') # Yes

# What measure correlates most strongly with fertility?

s.corr(method ='pearson') # Education

# Using the chipotle dataset from the previous exercise, 
# create a bar chart that shows the 4 most popular items and the revenue produced by each.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from pydataset import data
import seaborn as sns

from env import host, user, password

database = "chipotle"

def get_db_url(user,host,password,database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
    return url

url = get_db_url(user,host,password,database)

database_name = "chipotle"
query = """ SELECT * FROM orders """

c = pd.read_sql(query, url)

c['item_price'] = c.item_price.apply(lambda n: float(n.replace('$','')))

top_items = c[['item_name','item_price']].groupby('item_name').agg('sum').sort_values('item_price',ascending=False)

top_4 = top_items.head(4)

top_4 = top_4.reset_index()

top_4

c_graph = sns.barplot(x='item_name', y='item_price', data=top_4)

c_graph

# Load the sleepstudy data and read it's documentation. 
# Use seaborn to create a line chart of all the individual subject's reaction times 
# and a more prominant line showing the average change in reaction time.

sl = data('sleepstudy')

sl = sns.lineplot(x="timepoint", y="signal", data=fmri)