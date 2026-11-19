import pandas as pd
import matplotlib.pyplot as plt

# Load shipment dataset
file_path = input("Enter Shipment Details CSV file path: ")
df = pd.read_csv(file_path)

# Required columns
required_columns = [
    "Shipment_ID",
    "Product",
    "Quantity_KG",
    "Destination_City",
    "Transport_Mode",
    "Transport_Cost"
]

# Validate columns
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

# Remove missing values
df = df.dropna(subset=required_columns)

# Convert numeric columns
df["Quantity_KG"] = pd.to_numeric(
    df["Quantity_KG"], errors="coerce"
)
df["Transport_Cost"] = pd.to_numeric(
    df["Transport_Cost"], errors="coerce"
)

df = df.dropna(subset=["Quantity_KG", "Transport_Cost"])

# Display summary
print("Total Shipments:", df["Shipment_ID"].nunique())
print("Total Quantity:", df["Quantity_KG"].sum(), "KG")
print("Total Transport Cost:", df["Transport_Cost"].sum())

# Create visualizations
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Shipments by destination
destination_counts = df["Destination_City"].value_counts()
destination_counts.plot(kind="bar", ax=axes[0])
axes[0].set_title("Shipments by Destination")
axes[0].set_xlabel("Destination")
axes[0].set_ylabel("Number of Shipments")
axes[0].tick_params(axis="x", rotation=45)

# Quantity by product
product_quantity = df.groupby("Product")["Quantity_KG"].sum()
product_quantity.plot(kind="bar", ax=axes[1])
axes[1].set_title("Quantity by Product")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Quantity (KG)")
axes[1].tick_params(axis="x", rotation=45)

# Shipments by transport mode
mode_counts = df["Transport_Mode"].value_counts()
mode_counts.plot(kind="pie", autopct="%1.1f%%", ax=axes[2])
axes[2].set_title("Shipments by Transport Mode")
axes[2].set_ylabel("")

plt.tight_layout()
plt.show()
