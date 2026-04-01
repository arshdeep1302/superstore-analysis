import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# LOAD DATA (CHANGE PATH IF NEEDED)
# =========================
file_path = r'C:\Users\DELL\Downloads\SampleSuperstore.csv'
df = pd.read_csv(file_path)

# =========================
# CLEANING
# =========================
df.columns = df.columns.str.strip()
df.drop_duplicates(inplace=True)

# =========================
# KPI
# =========================
print("\n===== KPI =====")
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print("Total Quantity:", df['Quantity'].sum())

# =========================
# OUTPUT FOLDER (SIMPLE)
# =========================
output_folder = 'outputs/charts'
os.makedirs(output_folder, exist_ok=True)

# =========================
# CHART 1: Quantity by Category
# =========================
plt.figure()
df.groupby('Category')['Quantity'].sum().plot(kind='barh')
plt.title('Quantity by Category')
plt.tight_layout()
plt.savefig(f'{output_folder}/quantity_category.png')
plt.close()

# =========================
# CHART 2: Profit by Region
# =========================
plt.figure()
df.groupby('Region')['Profit'].sum().plot(kind='bar')
plt.title('Profit by Region')
plt.tight_layout()
plt.savefig(f'{output_folder}/profit_region.png')
plt.close()

# =========================
# CHART 3: Discount vs Profit
# =========================
plt.figure()
plt.scatter(df['Discount'], df['Profit'])
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig(f'{output_folder}/discount_vs_profit.png')
plt.close()

# =========================
# CHART 4: Sales by Category
# =========================
plt.figure()
df.groupby('Category')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig(f'{output_folder}/sales_category.png')
plt.close()

# =========================
# DONE
# =========================
print("\n✅ Done! Charts saved in outputs/charts")