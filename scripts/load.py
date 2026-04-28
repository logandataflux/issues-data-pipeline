import pandas as pd
import psycopg2

#Load cleaned data
df = pd.read_csv("data/clean_issues.csv")

# CLEAN DATAFRAME

#Remove accidental index column
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

#Ensure correct column order
required_cols = [
    "id",
    "title",
    "state",
    "created_at",
    "updated_at",
    "resolution_time_hours",
    "sla_status"
]

df = df[required_cols]

#CONNECT TO POSTGRESQL
conn = psycopg2.connect(
    dbname="issues_db",
    user="postgres",
    password="LetsGo210$",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

#INSERT DATA
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO github_issues (
            id,
            title,
            state,
            created_at,
            updated_at,
            resolution_time_hours,
            sla_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """, (
        row["id"],
        row["title"],
        row["state"],
        row["created_at"],
        row["updated_at"],
        row["resolution_time_hours"],
        row["sla_status"]
    ))

#COMMIT + CLOSE
conn.commit()
cur.close()
conn.close()

print("Data loaded into PostgreSQL successfully")