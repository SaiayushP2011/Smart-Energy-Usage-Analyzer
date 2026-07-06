import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Messy dataset with missing values, outliers, and inconsistent data types
data = {
    "UserID": [1,2,3,4,5,6,7,8,9,10,11,12],
    "Age": [22, np.nan, 35, 28, 19, 40, np.nan, 33, 27, 31, 45, np.nan],
    "MonthlyBill": [120, 200, -999, 150, 80, np.nan, 9999, 180, 160, -999, 220, 140],
    "Usage_kWh": [300, 500, 450, 400, 250, 700, 600, np.nan, 420, 520, 800, 390],
    "Plan": ["Basic","Premium","Basic",np.nan,"Basic","Premium","Basic","Premium","Basic","Premium","Basic","Premium"],
    "Region": ["North","South","North","East","South","West","North","East","South","West","North","East"]
}

df = pd.DataFrame(data)

# Cleaning the dataset
df = df.replace([-999, 9999], np.nan)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["MonthlyBill"] = df["MonthlyBill"].fillna(df["MonthlyBill"].median())
df["Usage_kWh"] = df["Usage_kWh"].fillna(df["Usage_kWh"].mean())
df["Plan"] = df["Plan"].fillna(df["Plan"].mode()[0])

def sort_age(age):
    if age>= 18 and age < 25:
        return "Young"
    elif 25 <= age <= 39:
        return "Adult"
    elif age >= 40:
        return "Senior"
    else:
        return "Invalid Age"
    
def Usage_category(bill):
    if bill < 100:
        return "Low"
    elif 100 <= bill <= 200:
        return "Medium"
    else:
        return "High"

df["High_Usage"] = df["Usage_kWh"] > 450
df["High_Bill"] = df["MonthlyBill"] > df["MonthlyBill"].median()
df["BillPerUsage"] = df["MonthlyBill"] / df["Usage_kWh"]
df["Age_Group"] = df["Age"].apply(sort_age)
df["Usage_Category"] = df["MonthlyBill"].apply(Usage_category)
avg_bill_region = df.groupby("Region")["MonthlyBill"].mean()
avg_bill_plan = df.groupby("Plan")["MonthlyBill"].mean()

#avg_bill_region.plot(kind = "bar", title = "Average Monthly Bill by Region")
#plt.xlabel("Region")
#plt.ylabel("Average Monthly Bill in $")

#avg_bill_plan.plot(kind = "bar", title = "Average Monthly Bill by Plan")
#plt.xlabel("Plan")
#plt.ylabel("Average Monthly Bill in $")


#How many young, adult, and senior users are there in the dataset?
#age_group_counts = df["Age_Group"].value_counts()
#age_group_counts.plot(kind = "bar", title = "Number of Users by Age Group")
#plt.xlabel("Age Group")
#plt.ylabel("Number of Users")


#Do premium users use more energy than basic users on average?
#avg_usage_plan = df.groupby("Plan")["Usage_kWh"].mean()
#avg_usage_plan.plot(kind = "bar", title = "Average Energy Usage by Plan")
#plt.xlabel("Plan")
#plt.ylabel("Average Energy Usage in kWh")

#Which regions has the highest percentage of high usage users?
#high_usage_region = df.groupby("Region")["High_Usage"].mean() * 100
#high_usage_region.plot(kind = "bar", title = "Percentage of High Usage Users by Region")
#plt.xlabel("Region")
#plt.ylabel("Percentage of High Usage Users")

#Histogram of Monthly Bills
#df["MonthlyBill"].plot(kind = "hist", bins = 10, title = "Distribution of Monthly Bills")
#plt.xlabel("Monthly Bill in $")

#Scatter plot of Monthly Bill vs Usage_kWh
df.plot(kind = "scatter", x = "Usage_kWh", y = "MonthlyBill", title = "Monthly Bill vs Energy Usage")
plt.xlabel("Energy Usage in kWh")
plt.ylabel("Monthly Bill in $")

plt.show()

df.info()
df.head()
df.isnull().sum()
