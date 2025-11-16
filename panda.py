import pandas as pd

data = {"scores": [10, 12, 15, 18, 200, 14, 13]}
df = pd.DataFrame(data)

Q1 = df["scores"].quantile(0.25)
Q3 = df["scores"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["scores"] < Q1 - 1.5 * IQR) | (df["scores"] > Q3 + 1.5 * IQR)]
print(outliers)
