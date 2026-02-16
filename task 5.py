import pandas as pd

# Load dataset
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




# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

# Handle missing values
df = df.dropna()

# Ensure numeric columns are correct type
numeric_cols = ["Sales", "Profit", "Discount", "Shipping_Cost", "Quantity"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("Cleaned_Superstore.csv", index=False)

print("✅ Data cleaned and saved as Cleaned_Superstore.csv")
