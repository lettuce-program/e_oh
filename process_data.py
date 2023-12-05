import re
import requests
import json
from tinydb import TinyDB, Query

db = TinyDB("eo.json")
data = {"nodes": [], "links":  []}
count = 0
for f in db:
    count += 1
    print(f"{count}/{len(db)}")
    doc = requests.get(f["body_html_url"]).text
    res = re.findall(r'Executive Order (\d+)', doc)
    lst = list(set(res))
    remove_self = [x for x in lst if f["executive_order_number"] not in x]
    
    #db.update({"related_executive_orders": remove_self}, Query().executive_order_number == f["executive_order_number"])

    data["nodes"].append({"id": f["title"], "eo": f["executive_order_number"], "link": f["body_html_url"], "data": f["signing_date"]})
    for idx in remove_self: 
        res = db.search(Query().executive_order_number == idx)
        if res:
            data["links"].append({"source": f["title"], "target": res[0]["title"]})
        else:
            data["links"].append({"source": f["title"], "target": idx})
            data["nodes"].append({"id": idx})

with open("data.json", "w") as fil:
    json.dump(data, fil)
