# Business Data Quality Analyzer
# First Python project for GitHub

customer_data = [
{"customer_id": 101, "name": "John", "email": "john@example.com"},
{"customer_id": 102, "name": "Maria", "email": "maria@example.com"},
{"customer_id": 103, "name": "", "email": "peter@example.com"},
{"customer_id": 104, "name": "Sarah", "email": ""},
{"customer_id": 102, "name": "Maria", "email": "maria@example.com"},
]

print("Business Data Quality Report")
print("----------------------------")

# Check for missing values
for customer in customer_data:
missing_fields = []

for field, value in customer.items():
if value == "":
missing_fields.append(field)

if missing_fields:
print(
f"Customer {customer['customer_id']} has missing data: "
f"{', '.join(missing_fields)}"
)

# Check for duplicate customer IDs
customer_ids = [customer["customer_id"] for customer in customer_data]

duplicates = {
customer_id
for customer_id in customer_ids
if customer_ids.count(customer_id) > 1
}

if duplicates:
print(f"Duplicate customer IDs found: {duplicates}")
else:
print("No duplicate customer IDs found.")

print("----------------------------")
print("Data quality analysis complete.")
