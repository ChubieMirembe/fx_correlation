import pandas as pd     

df = pd.read_csv("correlation.csv")

pair_1 = input("Enter the first pair: ").upper()
pair_2 = input("Enter the second pair: ").upper()
t_frame = input("Enter the timeframe: ").lower()

df1 = (df[df.pair1 == (pair_1)])
df2 = (df1[df1.pair2 == (pair_2)])
df3 = (df2[t_frame])

print(df3)
print("Anything above above 80 (positive or negative) has a high correlation")