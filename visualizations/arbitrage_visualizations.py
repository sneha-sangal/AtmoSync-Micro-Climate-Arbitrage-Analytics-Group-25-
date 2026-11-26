import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re

# ==========================================
# ATMOSYNC - MICRO CLIMATE ARBITRAGE ANALYTICS
# DATA LOADING + DATA VISUALIZATION
# ==========================================

print("\n===== ATMOSYNC PROJECT =====")

# STEP 1: Load CSV Dataset

folder = Path(__file__).resolve().parent

file_path = folder / "Arbitrage_All_Opportunities.csv"

if not file_path.exists():
    raise FileNotFoundError(
        f"CSV file not found: {file_path}\n"
        "Keep the CSV file in the visualizations folder."
    )

df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully!")
print("Total Records:", len(df))

print("\nDataset Shape:")
print(df.shape)

print("\nAvailable Columns:")
for col in df.columns:
    print("-", repr(col))

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
df.info()


# STEP 2: Identify Required Columns

def normalize(name):
    return re.sub(r"[^a-z0-9]", "", str(name).lower())

columns = {normalize(col): col for col in df.columns}

product_col = columns.get("product")

gap_col = next(
    (
        col for key, col in columns.items()
        if key.startswith("potentialpricegap")
    ),
    None
)

if product_col is None or gap_col is None:
    raise ValueError(
        "Required columns not found.\n"
        f"Available columns: {list(df.columns)}"
    )

print("\nProduct Column:", product_col)
print("Price Gap Column:", gap_col)


# STEP 3: Clean Required Data

df[gap_col] = pd.to_numeric(
    df[gap_col], errors="coerce"
)

chart_data = df.dropna(
    subset=[product_col, gap_col]
)


# STEP 4: Product-wise Average Price Gap

product_gap = (
    chart_data
    .groupby(product_col)[gap_col]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Price Gap by Product:")
print(product_gap)


# STEP 5: Create Bar Chart

plt.figure(figsize=(10, 6))

bars = plt.bar(
    product_gap.index.astype(str),
    product_gap.values
)

plt.title(
    "Average Price Gap by Product - AtmoSync",
    fontsize=14
)

plt.xlabel("Product")
plt.ylabel("Average Price Gap (Rs/kg)")

plt.xticks(rotation=30)

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()


# STEP 6: Save Chart

output_path = folder / "price_gap_by_product.png"

plt.savefig(output_path, dpi=300)

print("\nChart Saved Successfully!")
print("Location:", output_path)

# STEP 7: Display Chart

plt.show()

print("\n===== VISUALIZATION COMPLETED =====")
# ==========================================
# 8. POSITIVE VS NEGATIVE PROFIT MARGINS
# ==========================================

margin_col = columns.get("estimatedgrossmarginperkg")

if margin_col is None:
    raise ValueError("Estimated Gross Margin column not found!")

df[margin_col] = pd.to_numeric(
    df[margin_col], errors="coerce"
)

# Only records with available cost-supported margins
margin_data = df.dropna(subset=[margin_col])

positive = (margin_data[margin_col] > 0).sum()
negative = (margin_data[margin_col] < 0).sum()
zero = (margin_data[margin_col] == 0).sum()

print("\n===== PROFIT MARGIN ANALYSIS =====")
print("Total Cost-Supported Records:", len(margin_data))
print("Positive Margins:", positive)
print("Negative Margins:", negative)
print("Zero Margins:", zero)

# Create visualization
labels = ["Positive Margins", "Negative Margins"]
values = [positive, negative]

plt.figure(figsize=(8, 6))

bars = plt.bar(labels, values)

plt.title("Positive vs Negative Profit Margins - AtmoSync")
plt.xlabel("Margin Category")
plt.ylabel("Number of Opportunities")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(int(bar.get_height())),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    folder / "positive_negative_margins.png",
    dpi=300
)

plt.show()

print("\nMargin Visualization Saved Successfully!")
# ==========================================
# 3. PRODUCT-WISE AVERAGE GROSS MARGIN
# ==========================================

product_margin = (
    margin_data
    .groupby(product_col)[margin_col]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== PRODUCT-WISE GROSS MARGIN =====")
print(product_margin)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    product_margin.index.astype(str),
    product_margin.values
)

plt.title("Average Estimated Gross Margin by Product - AtmoSync")
plt.xlabel("Product")
plt.ylabel("Estimated Gross Margin (Rs/kg)")

plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    folder / "product_wise_gross_margin.png",
    dpi=300
)

plt.show()

print("\nThird Visualization Saved Successfully!")
# ==========================================
# 4. SHIPMENT COUNT BY PRODUCT
# ==========================================

shipment_counts = {
    "Bananas": 113,
    "Mangoes": 109,
    "Grapes": 97,
    "Tomatoes": 96,
    "Avocados": 85
}

print("\n===== SHIPMENT COUNT BY PRODUCT =====")

for product, count in shipment_counts.items():
    print(product, ":", count)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    shipment_counts.keys(),
    shipment_counts.values()
)

plt.title("Shipment Count by Product - AtmoSync")
plt.xlabel("Product")
plt.ylabel("Total Shipments")

plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(int(bar.get_height())),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    folder / "shipment_count_by_product.png",
    dpi=300
)

plt.show()

print("\nFourth Visualization Saved Successfully!")
# ==========================================
# 5. TOP 10 PRICE OPPORTUNITIES
# ==========================================

top_10 = df.dropna(subset=[gap_col]).copy()

top_10[gap_col] = pd.to_numeric(
    top_10[gap_col], errors="coerce"
)

top_10 = top_10.dropna(
    subset=[gap_col]
).nlargest(10, gap_col)

origin_col = columns.get("origincity")
destination_col = columns.get("destinationcity")

labels = []

date_col = columns.get("date")

for i, (_, row) in enumerate(top_10.iterrows(), start=1):
    product = str(row[product_col])
    origin = str(row[origin_col])
    destination = str(row[destination_col])
    date = str(row[date_col])

    labels.append(
        f"{i}. {product} | {origin} to {destination} | {date}"
    )

print("\n===== TOP 10 PRICE OPPORTUNITIES =====")
print(top_10[[product_col, gap_col]])

plt.figure(figsize=(14, 10))

plt.barh(labels[::-1], top_10[gap_col].values[::-1])

plt.title("Top 10 Price Opportunities - AtmoSync")
plt.xlabel("Potential Price Gap (Rs/kg)")
plt.ylabel("Product and Route")
plt.yticks(fontsize=9)
plt.tight_layout()

plt.savefig(
    folder / "top_10_price_opportunities.png",
    dpi=300
)

plt.show()

print("\nFifth Visualization Saved Successfully!")
# ==========================================
# 6. CITY-WISE PRODUCT PRICE COMPARISON
# ==========================================

price_file = folder / "City_Product_Prices.csv"

city_prices = pd.read_csv(price_file)

# Identify product column
product_column = next(
    (col for col in city_prices.columns
     if col.strip().lower() == "product"),
    None
)

if product_column is None:
    raise ValueError("Product column not found!")

# Identify city columns
city_columns = [
    col for col in city_prices.columns
    if col != product_column
]

# Convert prices into numeric values
price_matrix = city_prices[city_columns].apply(
    pd.to_numeric, errors="coerce"
)

# Plot Heatmap
plt.figure(
    figsize=(max(12, len(city_columns) * 1.1), 7)
)

plt.imshow(
    price_matrix.values,
    aspect="auto",
    cmap="YlOrRd"
)

plt.colorbar(label="Product Price (Rs/kg)")

plt.xticks(
    range(len(city_columns)),
    city_columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(city_prices)),
    city_prices[product_column]
)

plt.title("City-wise Product Price Comparison - AtmoSync")
plt.xlabel("Cities")
plt.ylabel("Products")

# Display price values
for i in range(len(city_prices)):
    for j in range(len(city_columns)):
        value = price_matrix.iloc[i, j]

        if pd.notna(value):
            plt.text(
                j, i, f"{value:.1f}",
                ha="center",
                va="center",
                fontsize=7
            )

plt.tight_layout()

plt.savefig(
    folder / "city_wise_product_price_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nSixth Visualization Saved Successfully!")
# ==========================================
# 7. ROUTE COST COMPARISON
# ==========================================

route_file = folder / "Route_Cost_Scenarios.csv"

route_df = pd.read_csv(route_file)

# Clean column names
route_df.columns = route_df.columns.str.strip()

# Identify columns
def find_route_column(possible_names):
    for col in route_df.columns:
        clean = col.lower().replace("_", " ").strip()
        if clean in possible_names:
            return col
    raise ValueError(
        f"Required column not found. Available: {list(route_df.columns)}"
    )

origin = find_route_column(["origin city"])
destination = find_route_column(["destination city"])
min_cost = find_route_column(
    ["minimum route cost", "min route cost"]
)
max_cost = find_route_column(
    ["maximum route cost", "max route cost"]
)

# Convert costs to numeric
route_df[min_cost] = pd.to_numeric(
    route_df[min_cost], errors="coerce"
)

route_df[max_cost] = pd.to_numeric(
    route_df[max_cost], errors="coerce"
)

route_df = route_df.dropna(
    subset=[origin, destination, min_cost, max_cost]
)

# Select top 10 routes by maximum cost
top_routes = route_df.nlargest(10, max_cost).copy()

labels = (
    top_routes[origin].astype(str)
    + " to "
    + top_routes[destination].astype(str)
)

print("\n===== TOP 10 ROUTE COST COMPARISON =====")
print(top_routes[[origin, destination, min_cost, max_cost]])

# Plot
x = range(len(top_routes))
width = 0.38

plt.figure(figsize=(13, 8))

plt.bar(
    [i - width/2 for i in x],
    top_routes[min_cost],
    width,
    label="Minimum Route Cost"
)

plt.bar(
    [i + width/2 for i in x],
    top_routes[max_cost],
    width,
    label="Maximum Route Cost"
)

plt.title("Top 10 Route Cost Comparison - AtmoSync")
plt.xlabel("Routes")
plt.ylabel("Estimated Route Cost (Rs)")
plt.xticks(
    list(x),
    labels,
    rotation=45,
    ha="right"
)

plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()

plt.savefig(
    folder / "route_cost_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nSeventh Visualization Saved Successfully!")
# 8. Container Type and Capacity Analysis

import pandas as pd
import matplotlib.pyplot as plt

file_path = folder / "Container_Capacity_Summary.csv"

df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace("_", " ")

# Clean container type names
df["container type"] = (
    df["container type"].astype(str).str.replace("_", " ").str.strip()
)

# Convert numeric columns
numeric_columns = [
    "total containers",
    "average capacity",
    "minimum capacity",
    "maximum capacity"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Create two charts
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Chart 1: Total containers
axes[0].bar(
    df["container type"],
    df["total containers"]
)

axes[0].set_title("Total Containers by Type - AtmoSync")
axes[0].set_xlabel("Container Type")
axes[0].set_ylabel("Total Containers")
axes[0].grid(axis="y", linestyle="--", alpha=0.4)

# Chart 2: Capacity comparison
x = range(len(df))
width = 0.25

axes[1].bar(
    [i - width for i in x],
    df["minimum capacity"],
    width,
    label="Minimum Capacity"
)

axes[1].bar(
    x,
    df["average capacity"],
    width,
    label="Average Capacity"
)

axes[1].bar(
    [i + width for i in x],
    df["maximum capacity"],
    width,
    label="Maximum Capacity"
)

axes[1].set_title("Capacity Comparison by Container Type - AtmoSync")
axes[1].set_xlabel("Container Type")
axes[1].set_ylabel("Capacity (kg)")
axes[1].set_xticks(list(x))
axes[1].set_xticklabels(df["container type"])
axes[1].legend()
axes[1].grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(folder / "container_capacity_analysis.png", dpi=300)
plt.show()
# 9. Sensor Performance Analysis

file_path = folder / "Sensor_Container_Combined.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace("_", " ")

# Convert sensor values to numeric
sensor_columns = [
    "average temperature",
    "average humidity",
    "average vibration"
]

for col in sensor_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Create three charts
fig, axes = plt.subplots(1, 3, figsize=(17, 7))

chart_details = [
    ("average temperature", "Top 10 Containers by Average Temperature",
     "Temperature (°C)", "Average Temperature"),
    ("average humidity", "Top 10 Containers by Average Humidity",
     "Humidity (%)", "Average Humidity"),
    ("average vibration", "Top 10 Containers by Average Vibration",
     "Vibration", "Average Vibration")
]

for ax, (column, title, ylabel, color) in zip(axes, chart_details):
    top_data = df.nlargest(10, column).sort_values(column)

    ax.barh(
        top_data["container id"].astype(str),
        top_data[column]
    )

    ax.bar_label(
        ax.containers[-1],
        fmt="%.1f",
        padding=3,
        fontsize=8
    )

    ax.set_title(title)
    ax.set_xlabel(ylabel)
    ax.set_ylabel("Container ID")
    ax.grid(axis="x", linestyle="--", alpha=0.4)

plt.suptitle("Sensor Performance Analysis - AtmoSync", fontsize=16)
plt.tight_layout()

plt.savefig(folder / "sensor_performance_analysis.png", dpi=300)
plt.show()
# 10. Shipment Analysis

file_path = folder / "Shipment_Analysis_Data.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace("_", " ")

# Create route column
df["route"] = (
    df["origin city"].astype(str) + " → " +
    df["destination city"].astype(str)
)

# Convert numeric columns
df["expected transit days"] = pd.to_numeric(
    df["expected transit days"], errors="coerce"
)

# Create three charts
fig, axes = plt.subplots(1, 3, figsize=(19, 7))

# Chart 1: Shipments by Transport Mode
mode_counts = df["transport mode"].value_counts()

axes[0].bar(mode_counts.index.astype(str), mode_counts.values)
axes[0].set_title("Shipments by Transport Mode")
axes[0].set_xlabel("Transport Mode")
axes[0].set_ylabel("Number of Shipments")
axes[0].tick_params(axis="x", rotation=30)
axes[0].grid(axis="y", linestyle="--", alpha=0.4)

# Chart 2: Top 10 Shipping Routes
route_counts = df["route"].value_counts().head(10).sort_values()

axes[1].barh(route_counts.index, route_counts.values)
axes[1].set_title("Top 10 Shipping Routes")
axes[1].set_xlabel("Number of Shipments")
axes[1].set_ylabel("Route")
axes[1].grid(axis="x", linestyle="--", alpha=0.4)

# Chart 3: Average Expected Transit Days
avg_transit = (
    df.groupby("transport mode")["expected transit days"]
    .mean()
    .dropna()
)

axes[2].bar(avg_transit.index.astype(str), avg_transit.values)
axes[2].set_title("Average Expected Transit Days by Mode")
axes[2].set_xlabel("Transport Mode")
axes[2].set_ylabel("Average Transit Days")
axes[2].tick_params(axis="x", rotation=30)
axes[2].grid(axis="y", linestyle="--", alpha=0.4)

plt.suptitle("Shipment Analysis - AtmoSync", fontsize=16)
plt.tight_layout()

plt.savefig(folder / "shipment_analysis.png", dpi=300)
plt.show()
# 11. Same-Day Price Comparison Analysis

file_path = folder / "Same_Day_Price_Comparison.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace("_", " ")

# Convert price columns to numeric
numeric_columns = [
    "lowest price",
    "highest price",
    "potential price gap"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Group data by product
product_data = df.groupby("product").agg({
    "lowest price": "mean",
    "highest price": "mean",
    "potential price gap": "mean"
}).reset_index()

# Create three charts
fig, axes = plt.subplots(1, 3, figsize=(19, 7))

# Chart 1: Average Potential Price Gap by Product
gap_data = product_data.sort_values("potential price gap")

axes[0].barh(
    gap_data["product"],
    gap_data["potential price gap"]
)
axes[0].set_title("Average Potential Price Gap by Product")
axes[0].set_xlabel("Price Gap")
axes[0].set_ylabel("Product")
axes[0].grid(axis="x", linestyle="--", alpha=0.4)

# Chart 2: Lowest vs Highest Average Price
x = range(len(product_data))
width = 0.35

axes[1].bar(
    [i - width/2 for i in x],
    product_data["lowest price"],
    width,
    label="Lowest Price"
)

axes[1].bar(
    [i + width/2 for i in x],
    product_data["highest price"],
    width,
    label="Highest Price"
)

axes[1].set_title("Lowest vs Highest Average Price")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Average Price")
axes[1].set_xticks(list(x))
axes[1].set_xticklabels(product_data["product"], rotation=30)
axes[1].legend()
axes[1].grid(axis="y", linestyle="--", alpha=0.4)

# Chart 3: Top 10 Price Opportunities
top_10 = df.nlargest(10, "potential price gap").copy()
top_10["label"] = (
    top_10["product"].astype(str) + " - " +
    top_10["lowest price city"].astype(str) + " to " +
    top_10["highest price city"].astype(str)
)

top_10 = top_10.sort_values("potential price gap")

axes[2].barh(
    top_10["label"],
    top_10["potential price gap"]
)
axes[2].set_title("Top 10 Highest Price Opportunities")
axes[2].set_xlabel("Potential Price Gap")
axes[2].set_ylabel("Product and Cities")
axes[2].tick_params(axis="y", labelsize=7)
axes[2].grid(axis="x", linestyle="--", alpha=0.4)

plt.suptitle("Same-Day Price Comparison - AtmoSync", fontsize=16)
plt.tight_layout()

plt.savefig(folder / "same_day_price_comparison.png", dpi=300)
plt.show()
# 12. Final Combined Project Overview

# Load existing datasets
shipment_df = pd.read_csv(folder / "Shipment_Analysis_Data.csv")
price_df = pd.read_csv(folder / "Same_Day_Price_Comparison.csv")
sensor_df = pd.read_csv(folder / "Sensor_Container_Combined.csv")
route_df = pd.read_csv(folder / "Route_Cost_Scenarios.csv")

# Clean column names
for data in [shipment_df, price_df, sensor_df, route_df]:
    data.columns = (
        data.columns.str.strip()
        .str.lower()
        .str.replace("_", " ")
    )

# Calculate project metrics
total_shipments = len(shipment_df)
total_price_comparisons = len(price_df)
total_containers = sensor_df["container id"].nunique()
total_routes = len(route_df)

# Create overview figure
fig, ax = plt.subplots(figsize=(12, 8))

ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

ax.text(
    6, 7.3,
    "AtmoSync - Final Project Overview",
    ha="center",
    fontsize=20,
    fontweight="bold"
)

# KPI cards
metrics = [
    ("TOTAL SHIPMENTS", total_shipments, 1, 4.5),
    ("PRICE COMPARISONS", total_price_comparisons, 6.5, 4.5),
    ("TOTAL CONTAINERS", total_containers, 1, 1.5),
    ("ROUTE RECORDS", total_routes, 6.5, 1.5)
]

for title, value, x, y in metrics:
    ax.add_patch(
        plt.Rectangle(
            (x, y), 4.5, 2,
            fill=False,
            linewidth=2
        )
    )

    ax.text(
        x + 2.25, y + 1.35,
        title,
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

    ax.text(
        x + 2.25, y + 0.55,
        f"{value:,}",
        ha="center",
        fontsize=25,
        fontweight="bold"
    )

ax.text(
    6, 0.6,
    "Data Analytics | Sensor Monitoring | Price Comparison | Route Analysis",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    folder / "final_project_overview.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()