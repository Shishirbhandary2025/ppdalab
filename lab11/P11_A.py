import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv(r"3Salary_Data.csv")
df

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_data1 = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_data1)