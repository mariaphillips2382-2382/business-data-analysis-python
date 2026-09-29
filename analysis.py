import pandas as pd

# Load customer data
file_path = "data/customers.csv"
df = pd.read_csv(file_path)

print("BUSINESS DATA QUALITY & KPI REPORTING")
print("-----------------------------------")

# Total records
total_records = len(df)
print(f"Total customer records: {total_records}")

# Customer status analysis
print("\nCustomer Status:")
status_counts = df["status"].value_counts(dropna=False)

for status, count in status_counts.items():
  status_name = "Missing" if pd.isna(status) else status
  print(f"- {status_name}: {count}")

# Missing data analysis
print("\nMissing Values:")
missing_values = df.isnull().sum()

total_missing = 0

for column, count in missing_values.items():
  if count > 0:
    print(f"- {column}: {count}")
    total_missing_records += count

# Duplicate customer IDs
duplicate_ids = df[df.duplicated("customer_id", keep=False)]

print("\nDuplicate Customer IDs:")

if duplicate_ids.empty:
  print("None found")
else:
  unique_duplicates = duplicate_ids["customer_id"].unique()
  print(unique_duplicates)

# Data quality KPI
records_with_missing_data = df.isnull().any(axis=1).sum()

data_quality_issue_rate = (
records_with_missing_data / total_records
) * 100

print("\nData Quality KPIs:")
print(f"- Records with missing data: {records_with_missing_data}")
print(f"- Total missing values: {total_missing}")
print(f"- Data quality issue rate: {data_quality_issue_rate:.1f}%")
print(f"- Duplicate customer IDs: {duplicate_ids['customer_id'].nunique()}")

print("-----------------------------------")
print("Analysis complete.")
