import pandas as pd

#Load raw data
df = pd.read_csv("data/raw_issues.csv")

#Convert timestamps
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

#Resolution time (hours)
df["resolution_time_hours"] = (
    df["updated_at"] - df["created_at"]
).dt.total_seconds() / 3600

#Fill missing values safely
df = df.fillna({"resolution_time_hours": 0})

#SLA CLASSIFICATION 
def sla_status(hours):
    if hours <= 24:
        return "On Time"
    elif hours <= 48:
        return "At Risk"
    else:
        return "Breached"

df["sla_status"] = df["resolution_time_hours"].apply(sla_status)

#SLA BOOLEAN
df["sla_breach"] = df["resolution_time_hours"] > 48

#Save cleaned dataset
df.to_csv("data/clean_issues.csv", index=False)

print("Transformation complete")