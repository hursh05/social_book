import pandas as pd
import numpy as np

# Step 2: Create DataFrame from a dictionary
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'C': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
}

df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

# Step 3: Filter rows where values in column 'A' are greater than 5
filtered_df = df[df['A'] > 5]
print("\nFiltered DataFrame (where column A > 5):")
print(filtered_df)

# Step 4: Filter rows where column A > 5 and column B < 50
filtered_df_2 = df[(df['A'] > 5) & (df['B'] < 50)]
print("\nFiltered DataFrame (where column A > 5 and column B < 50):")
print(filtered_df_2)

# Step 5: Replace value 10 with 999 in column 'A'
df['A'] = df['A'].replace(10, 999)
print("\nDataFrame after replacing 10 with 999 in column A:")
print(df)

# Step 6: Create a second DataFrame with random data (same columns)
data2 = {
    'A': np.random.randint(1, 20, 10),
    'B': np.random.randint(10, 200, 10),
    'C': np.random.randint(100, 2000, 10)
}

df2 = pd.DataFrame(data2)

# Append df2 to df using pd.concat()
appended_df = pd.concat([df, df2], ignore_index=True)
print("\nAppended DataFrame:")
print(appended_df)
