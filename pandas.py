


"""

MOVIES DATA ANALYSIS BY USING ITS RELESING YEAR AND IMDB AND GENRE


Original file is located at
    https://colab.research.google.com/drive/1EiLU8YUDZ1g2r6l0L7K1v_RwZ8tNIOUS




4: Data analysis with csv file"""

import pandas  as pd
data=pd.read_csv('/content/Untitled spreadsheet - Sheet1.csv')
df=data.describe()
data.head()

data.describe()

avg_votes=data["imdb_votes"].mean()
avg_votes

avg_rating = data["imdb_score"].mean()
avg_rating

avg_runtime = data["runtime"].mean()
avg_runtime

fill=data[data['release_year']>2004]
fill

"""1.which are the top 10 watched movie and show"""

top10=data.nlargest(10,'imdb_votes')
top10

top=data.nlargest()

"""#3. Top 10 movie which have  highest  rating"""

top=data.nlargest(10,'imdb_score')
top10

"""4. which are the top movie have avg run time"""

top10=data.nlargest(5,'runtime')
top10

df2=data[data['release_year']>2006].nlargest(5,'runtime')
df2

"""flopshows in netflix"""

flopshow=data[data['imdb_score']<5]
flopshow

"""#..Sorting"""

short=data[data['runtime']>90]
a=short.sort_values(by=['imdb_score'])
a

short=data[data['runtime']>90].nlargest(5,'imdb_score')
short

def categerise(imdb_score):
  if imdb_score>9:
    return "diamond"
  elif imdb_score>7 and imdb_score<8:
    return "gold"
  elif imdb_score>5 and imdb_score<7:
    return "silver"
  elif imdb_score<5:
    return "bronze"
  else:
    return "okk"
data['id'] = data["imdb_score"].map(categerise)
data

