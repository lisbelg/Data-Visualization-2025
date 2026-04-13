import pandas as pd
import matplotlib.pyplot as plt

# Load sample data
data = pd.read_csv("sample-data.csv")

# Plot line chart
plt.plot(data["Month"], data["Sales"])

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()