import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = input("Enter IoT sensor CSV file path: ")
df = pd.read_csv(file_path)

# Required columns
required_columns = [
    "Timestamp",
    "Temperature_C",
    "Humidity_Percent",
    "Vibration_Level"
]

for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

# Prepare data
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values("Timestamp")

# Remove missing values
df = df.dropna(subset=required_columns)

# Create three visualizations
fig, axes = plt.subplots(3, 1, figsize=(12, 12))

axes[0].plot(df["Timestamp"], df["Temperature_C"])
axes[0].set_title("Temperature Trend")
axes[0].set_ylabel("Temperature (°C)")

axes[1].plot(df["Timestamp"], df["Humidity_Percent"])
axes[1].set_title("Humidity Trend")
axes[1].set_ylabel("Humidity (%)")

axes[2].plot(df["Timestamp"], df["Vibration_Level"])
axes[2].set_title("Vibration Trend")
axes[2].set_ylabel("Vibration Level")

axes[2].set_xlabel("Timestamp")

plt.tight_layout()
plt.show()

# Display summary
print("\nSensor Data Summary:")
print(df[required_columns[1:]].describe())
