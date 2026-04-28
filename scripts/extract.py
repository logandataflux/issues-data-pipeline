import requests
import pandas as pd

url = "https://api.github.com/repos/kubernetes/kubernetes/issues"

response = requests.get(url)
data = response.json()

rows = []
for issue in data:
    if "pull_request" in issue:
        continue
    
    rows.append({
        "id": issue["id"],
        "title": issue["title"],
        "state": issue["state"],
        "created_at": issue["created_at"],
        "updated_at": issue["updated_at"]
    })

df = pd.DataFrame(rows)

df.to_csv("data/raw_issues.csv", index=False)

print("Data extracted successfully")