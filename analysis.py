# Business Data Quality Analyzer
# First Python project for GitHub

import pandas as pd

# Load customer data
file_path = "data/customers.csv"
df = pd.read_csv(file_path)

print("Business Data Quality Report")
print("----------------------------")

# Display number of records
print(f"Total records: {len(df)}")

# Check for missing values
print("\nMissing values:")
missing_values = df.isnull().sum()

for column, count in missing_values.items():
  if count > 0:
    print(f"- {column}: {count}")

# Check for duplicate customer IDs
duplicate_ids = df[df.duplicated("customer_id", keep=False)]

print("\nDuplicate customer IDs:")

if duplicate_ids.empty:
  print("None found")
else:
  print(duplicate_ids["customer_id"].unique())

print("----------------------------")
print("Data quality analysis complete.")
