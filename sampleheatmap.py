#from Bradley to generate a heatmap showing genre preference intensity by region, normalized to 100%

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the csv file
df = pd.read_csv("db/vgsales.csv")

# Calculate the total region sales
region_sales = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
print(region_sales)

# Normalize each region sale to 100%
region_sales_normalized = region_sales / region_sales.sum() * 100

# Generate the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(region_sales_normalized, annot=True, cmap='coolwarm', fmt=".1f")

plt.title("Genre Preference Intensity by Region (Normalized to 100%)")
plt.xlabel("Region")
plt.ylabel("Genre")
plt.show()

# Generate multiple heatmaps with different colour schemes to choose the most suitable one

for cmap in ["YlGnBu", "coolwarm", "viridis", "magma", "RdYlBu"]:
    plt.figure(figsize=(10,6))
    sns.heatmap(region_sales_normalized, cmap=cmap, annot=True)
    plt.title(f"Heatmap with cmap = {cmap}")
    plt.show()