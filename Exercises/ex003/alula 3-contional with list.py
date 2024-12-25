#conditional with list
product=["bread", "milk", "coffee"]
search=input("Search a product in shop: ")
search.lower()
if search in product:
    print(f"{search}, is in list, you wont?")
    print("Status:true ")
else:
    print(f"{search}, isn't in list")
    print("Status: false")