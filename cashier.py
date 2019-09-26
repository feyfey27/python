
items = []

name = input("Item (enter \"done\" when finished: ")

while name != "done":

	price = float(input("Price: "))
	quantity = int(input("Quantity: "))


	item = {}
	item["name"] = name
	item["price"] = price
	item["quantity"] = quantity

	items.append(item)
	name = input("Item (enter \"done\" when finished: ")

# print(items)
total = 0
for item in items:
	print(item["quantity"], item["name"], item["price"] * item["quantity"], "KD")
	total += item["price"] * item["quantity"]
print("Total Price: ", total, "KD")

