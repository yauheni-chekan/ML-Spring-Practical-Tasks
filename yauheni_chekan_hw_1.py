import pandas as pd

df = pd.read_csv("/content/EDA HW Dataset.csv")

df.head()

df.shape

df.info()

df.dtypes

numerical = df.select_dtypes('number').columns
categorical = df.select_dtypes(object).columns

print(f"Numericals: {[i for i in numerical]}\nCategoricals: {[i for i in categorical]}")

"""---
The most frequent car name is "ford pinto". It is refered 6 times in the dataset.
"""

df["name"].value_counts().head(1)

"""---
There are no completely duplicated rows in the dataset.
"""

df[df.duplicated()]

"""---
The 'displacement' 'horsepower' correlation coefficient is 0.897, meaning that there is a strong positive correlation between engine displacement and the horsepower.
"""

df[["displacement", "horsepower"]].corr()

"""---
There are 305 unique car names in the dataset.
"""

df["name"].nunique()

"""---
The most effective car in terms of fuel consumption out of
- plymouth custom suburb
- volvo 264gl
- cadillac seville
- buick skylark 320

is Volvo 264 GL that can make 17 miles per 1 gallon of fuel.
"""

cars = ['plymouth custom suburb', 'volvo 264gl', 'cadillac seville', 'buick skylark 320']
df[df['name'].isin(cars)].groupby('name')['mpg'].mean().sort_values(ascending=False).head(1)

"""---
The lowest horsepower in japanese cars is Mazda DLC Deluxe having 52 horsepower.
"""

df[df["origin"].isin(["japan"])].groupby("name")['horsepower'].mean().sort_values().head(1)

"""---
The lowest MPG in japanese cars is 18 miles per gallon of fuel.
"""

df[df["origin"].isin(["japan"])].groupby("name")['mpg'].mean().sort_values().head(1)

total_european_cars = len(df[df["origin"] == "europe"])
european_cars_with_8_cylinders = (df[df["origin"] == "europe"]["cylinders"] == 8).sum()
percentage = (european_cars_with_8_cylinders / total_european_cars) * 100
print(f"The percentage of European cars with 8 cylinders is: {percentage:.2f}%")

"""---
The largest range of acceleration (in terms of standard deviation) have cars with 4 cylinders
"""

df.groupby('cylinders')['acceleration'].std().idxmax()

american_cars_horsepower_avg = df[df["origin"] == "usa"]["horsepower"].mean()
european_cars_horsepower_avg = df[df["origin"] == "europe"]["horsepower"].mean()
print(f"On average, european cars have {'more' if european_cars_horsepower_avg > american_cars_horsepower_avg else 'less'} horsepower than american")
