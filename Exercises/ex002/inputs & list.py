stock=[ "bread", "tea", "milk", "cake" ]
search=input("Find in stock now: ")
search=search.lower()
print(f"Status in stock:", search, "equal to ", search in stock )
stock.append(input("Imput new product:"))
print(stock)
stock.remove(input("Input now:"))
print(stock)
print(stock.count(input("Count repeat:")))


