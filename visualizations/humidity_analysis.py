import pandas as pd
import matplotlib.pyplot as plt

# Load IoT sensor dataset
file_path = input("Enter the path of IoT sensor CSV file: ")

df = pd.read_csv(file_path)

# Convert timestamp
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Check required column
if "Humidity_Percent" not in df.columns:
    raise ValueError("Humidity_Percent column not found!")

# Remove missing humidity values
df = df.dropna(subset=["Humidity_Percent"])

# Sort data by timestamp
df = df.sort_values("Timestamp")

# Calculate average humidity
average_humidity = df["Humidity_Percent"].mean()

print("Average Humidity:", round(average_humidity, 2), "%")
print("Total Records:", len(df))

# Create humidity visualization
plt.figure(figsize=(12, 6))

plt.plot(
    df["Timestamp"],
    df["Humidity_Percent"],
    label="Humidity",
    alpha=0.6
)

plt.axhline(
    average_humidity,
    linestyle="--",
    label="Average Humidity"
)

plt.title("IoT Sensor Humidity Analysis")
plt.xlabel("Timestamp")
plt.ylabel("Humidity (%)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
