import pandas as pd
import matplotlib.pyplot as plt

# Load the IoT sensor dataset
file_path = input("Enter the path of IoT sensor CSV file: ")

df = pd.read_csv(file_path)

# Convert timestamp into datetime format
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Sort records by timestamp
df = df.sort_values("Timestamp")

# Check required columns
if "Temperature_C" not in df.columns:
    raise ValueError("Temperature_C column not found!")

# Calculate average temperature
average_temp = df["Temperature_C"].mean()

print("Average Temperature:", round(average_temp, 2), "°C")
print("Total Records:", len(df))

# Create temperature visualization
plt.figure(figsize=(12, 6))

plt.plot(
    df["Timestamp"],
    df["Temperature_C"],
    label="Temperature",
    alpha=0.6
)

plt.axhline(
    average_temp,
    linestyle="--",
    label="Average Temperature"
)

plt.title("IoT Sensor Temperature Analysis")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
