import pandas as pd
import psycopg2

# Load cleaned data
df = pd.read_csv("data/clean_issues.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="issues_db",
    user="postgres",
    password="LetsGo210$",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO github_issues
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("Data loaded into PostgreSQL")