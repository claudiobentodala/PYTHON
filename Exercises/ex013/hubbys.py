foods={"tea":5, "bread":[2,1,3,6]}
print("1.Input food ")
print("2.Search Food")
change=(input("Input what you wont to do: "))
change=change.lower()
if change==1:
    print("========================================")
    time = int(input("How many product you wont to add: "))
    for i in range(time):
        name = input("Input the name of food: ")
        name = name.lower()
        price = int(input("Input the price of the food: "))
        foods[name] = price
    print("========================================")
if change==2:
    print("========================================")
    search=input("What food you wont to find: ")
    if search in foods:
        print("The food are here")
    else:
        print("The food are not here")
    print("========================================")
if change==3:
    print("========================================")
    print("========================================")