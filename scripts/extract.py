import requests
import pandas as pd

url = "https://api.github.com/repos/kubernetes/kubernetes/issues"

rows = []

# 🔥 LOOP through multiple pages
for page in range(1, 6):  # pulls 5 pages
    params = {
        "state": "all",
        "per_page": 100,
        "page": page
    }

    response = requests.get(url, params=params)
    data = response.json()

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