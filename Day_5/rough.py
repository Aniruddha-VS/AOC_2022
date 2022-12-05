items = [1,2,3,4,5]
new_items = [8,9]

new_items = new_items + items[-2:]
items = items[:-2]

print(items, new_items)