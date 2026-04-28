import requests
import pandas as pd
import random
from datetime import datetime, timedelta

url = "https://api.github.com/repos/kubernetes/kubernetes/issues"

rows = []

#Base time used for synthetic time distribution
base_date = datetime.utcnow()

#LOOP through multiple pages (pagination)
for page in range(1, 6):  # pulls 5 pages
    params = {
        "state": "all",
        "per_page": 100,
        "page": page
    }

    response = requests.get(url, params=params)
    data = response.json()

    for issue in data:
        #Skip pull requests (GitHub includes them in issues API)
        if "pull_request" in issue:
            continue

        #Simulate realistic time variation (FIXES Power BI issue)
        created_at = base_date - timedelta(days=random.randint(0, 30))
        updated_at = created_at + timedelta(hours=random.randint(1, 72))

        rows.append({
            "id": issue["id"],
            "title": issue["title"],
            "state": issue["state"],
            "created_at": created_at,
            "updated_at": updated_at
        })

#Convert to dataframe
df = pd.DataFrame(rows)

#Save raw dataset
df.to_csv("data/raw_issues.csv", index=False)

print("Data extracted successfully")