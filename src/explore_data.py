import pandas as pd

df = pd.read_csv("./data/games.csv")

# This line makes a new boolean column titled home_win based on weather or not the result column is > 0
df["home_win"] = df["result"] > 0

# This line will remove all columns where the result is equal to zero
# This is to remove ties which are not needed for the goal
df = df[df["result"] != 0]

