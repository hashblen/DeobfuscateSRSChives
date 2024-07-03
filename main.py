import json
import urllib.request
import re

with urllib.request.urlopen("https://starrailstation.com/api/v1/data/01fc766f1e55cae692368f51c05b073e/4y851o") as url:
    achievements_data = json.load(url)

req_stardb = urllib.request.Request("https://stardb.gg/api/achievements", headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req_stardb) as url:
    stardb_data = json.load(url)

# Create a dictionary to map names to IDs
id_map = {item['name']: item['id'] for item in stardb_data}

srs_ids_to_real = {}

# Iterate over the achievements and replace the IDs
for achievement_id, achievements in achievements_data['achievements'].items():
    for achievement in achievements:
        name = re.sub(r'<.*?>', '', achievement['title'])
        if name in id_map:
            srs_ids_to_real[achievement['id']] = id_map[name]
        else:
            print(f"Warning: No matching ID found for achievement '{name}'")

# Save the updated achievements data to a new file
with open('srs_ids_to_real.json', 'w') as f:
    json.dump(srs_ids_to_real, f, indent=2)
