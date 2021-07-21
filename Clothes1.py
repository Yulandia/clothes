list_clothes = ["socks", "shirt", "skirt", "scarf"]
def insert_element(new_cloth, index=0):
    list_clothes.insert(index, new_cloth)

insert_element("sweater", 1)
print(list_clothes)
insert_element("sweater", -1)
print(list_clothes)
insert_element("sweater")
print(list_clothes)