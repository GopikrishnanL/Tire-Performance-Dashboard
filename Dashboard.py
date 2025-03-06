import streamlit as st
import pandas as pd
import plotly.express as px

# Load random data
df = pd.read_csv("random_tire_data.csv")

# Streamlit UI
st.title("Tire Performance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_speed = st.sidebar.multiselect("Select Speed (km/h):", df["Speed (km/h)"].unique(), default=df["Speed (km/h)"].unique())
selected_surface = st.sidebar.multiselect("Select Road Surface:", df["Road Surface"].unique(), default=df["Road Surface"].unique())

# Filter data based on selection
filtered_df = df[(df["Speed (km/h)"].isin(selected_speed)) & (df["Road Surface"].isin(selected_surface))]

# Display Data
st.subheader("Filtered Data")
st.write(filtered_df)

# Visualization - Grip vs Speed
fig1 = px.scatter(filtered_df, x="Speed (km/h)", y="Grip Level", color="Road Surface", title="Grip Level vs Speed")
st.plotly_chart(fig1)

# Visualization - Wear vs Temperature
fig2 = px.scatter(filtered_df, x="Temperature (°C)", y="Wear Level", color="Road Surface", title="Wear Level vs Temperature")
st.plotly_chart(fig2)

# Visualization - Boxplot for Grip by Surface Type
fig3 = px.box(filtered_df, x="Road Surface", y="Grip Level", title="Grip Level Distribution by Road Surface")
st.plotly_chart(fig3)

# Visualization - Boxplot for Wear by Surface Type
fig4 = px.box(filtered_df, x="Road Surface", y="Wear Level", title="Wear Level Distribution by Road Surface")
st.plotly_chart(fig4)
