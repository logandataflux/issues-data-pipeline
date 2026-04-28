import pandas as pd

#Load raw data
df = pd.read_csv("data/raw_issues.csv")

#Convert timestamps
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

#Feature engineering: resolution time(hours)
df["resolution_time_hours"] = (
    df["updated_at"] - df["created_at"]
).dt.total_seconds() / 3600

#Add simple SLA flag (anything less than 48 hours = late)
df["sla branch"] = df["resolution_time_hours"] >48

#Basic cleanup
df = df.fillna({"resolution_time_hours": 0})

#Save cleaned dataset
df.to_csv("data/clean_issues.csv", index=False)

print("Transformation complete")
