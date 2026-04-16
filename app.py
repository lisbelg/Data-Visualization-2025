import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Sales Dashboard")
st.subheader("Streamlit Boilerplate App")

# Load data
data = pd.read_csv("sample-data.csv")

# Show raw data checkbox
if st.checkbox("Show raw data"):
    st.write(data)

# Dropdown for selecting a product
product_list = data["Product"].unique()
selected_product = st.selectbox("Select a product", product_list)

# Filter data based on selected product
filtered_data = data[data["Product"] == selected_product]

# Show filtered table
st.write("Filtered Data")
st.dataframe(filtered_data)

# Create chart
st.write("Sales Trend")
fig, ax = plt.subplots()
ax.plot(filtered_data["Month"], filtered_data["Sales"], marker="o")
ax.set_title(f"Monthly Sales for {selected_product}")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
st.pyplot(fig)