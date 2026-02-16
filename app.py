import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Business Dashboard", layout="wide")

# Load data
df = pd.read_csv(
    r"D:\python\Internship\STAGE 2\TASK 5\Global_Superstore2.csv",
    encoding="latin1",
    low_memory=False
)

# Clean column names
df.columns = (
    df.columns
      .str.strip()
      .str.replace(" ", "_")
      .str.replace("-", "_")
)



# Sidebar filters
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

sub_category = st.sidebar.multiselect(
    "Select Sub-Category",
    options=df["Sub_Category"].unique(),
    default=df["Sub_Category"].unique()
)


# Apply filters
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Sub_Category"].isin(sub_category))
]



# KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()

top_customers = (
    filtered_df.groupby("Customer_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Dashboard Title
st.title("📊 Interactive Business Dashboard")

# KPI Display
col1, col2 = st.columns(2)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")

st.markdown("---")

# Charts
st.subheader("Sales by Category")
fig1 = px.bar(filtered_df, x="Category", y="Sales", color="Category")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Profit by Region")
fig2 = px.pie(filtered_df, names="Region", values="Profit")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🏆 Top 5 Customers by Sales")
fig3 = px.bar(
    top_customers,
    x=top_customers.values,
    y=top_customers.index,
    orientation="h",
    labels={"x": "Sales", "y": "Customer"}
)
st.plotly_chart(fig3, use_container_width=True)

st.success("✅ Dashboard Ready for Business Insights!")
