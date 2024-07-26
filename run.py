import re
import yaml

with open(r'animated_emoji_items.yml') as file:
    documents = yaml.full_load(file)
    data = {}
    data["info"] = documents["info"]
    data["categories"] = {}
    namespace  = data["info"]["namespace"]
    data["categories"][namespace] = {}
    items = []
    # for item, doc in sorted(documents["items"],key=lambda x: int(x.split("_")[-1])):
    for item, doc in documents["items"].items():
        items.append(namespace+":"+item)
    # items = sorted(items,key=lambda x: int(x.split("_")[-1]))
    data["categories"][namespace]["name"] = namespace.replace("_"," ").title()
    data["categories"][namespace]["enabled"] = True
    data["categories"][namespace]["icon"] = namespace+":"+item
    data["categories"][namespace]["permission"] = "ia.menu."+namespace
    data["categories"][namespace]["items"] = items

with open('./'+namespace+"_category.yml", 'w') as file:
    documents = yaml.dump(data, file, sort_keys=False)   
print("ok")