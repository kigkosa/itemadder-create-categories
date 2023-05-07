import yaml

with open(r'king_arthur_set.yml') as file:
    documents = yaml.full_load(file)
    data = {}
    data["info"] = documents["info"]
    data["categories"] = {}
    namespace  = data["info"]["namespace"]
    data["categories"][namespace] = {}
    items = []

    for item, doc in documents["items"].items():
        items.append(namespace+":"+item)
    data["categories"][namespace]["enabled"] = True
    data["categories"][namespace]["icon"] = item
    data["categories"][namespace]["permission"] = "ia.menu."+namespace
    data["categories"][namespace]["items"] = items

with open('./'+namespace+"_category.yml", 'w') as file:
    documents = yaml.dump(data, file, sort_keys=False)   
print("ok")
# print(data)
# print(items)