stock={"tea": 25, "bread": 50}
food=(input("Search the food: "))
if food in stock:
    price=input("Search the prices foods: ")
    if price in stock.values():
       print(f"The {food} is in stock with the price of {price}kz")
    else:
        print(f"The {food} is in stock but this isn't the {price}kz ")
else:
    print(f"{food} have not in stock")

print("And program")
