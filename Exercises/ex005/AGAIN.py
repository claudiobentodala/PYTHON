food = {"bread": 50, "tea":5}
print("====add ou edit product in stock====")
check=input("Check now: ")
if check in food:
    print("===Edit the food===")
    food[check]=int(input("What is the is the new price:"))
else:
    print("===Add the new product===")
    food[check]=int(int("What is the price;"))

print("The program over!")