food={"bread": 50,"tea": 25,"coffee": 150,"milk": 800 }
print("==========SEARCH THE FOOD=============")
search=input("Search what food you wont: ")
print(f"The {search} price is " ,food[search])
print("==========REMOVE THE FOOD============")
food.pop(input("What food you wont to remove: "))
print("Rith now the foods is {food}")
print("=============ADD OR EDIT THE FOOD==========")
times=int(input("How many time you wont to add or edit food: "))
for i in range(times):
    food[input("What food you wont to add or edit: ")]=float(input("What's the price: "))
print(f"Rith now the foods is {food}")
