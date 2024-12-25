#exemplo of conditional
name=input("Input your name: ")
vendas=int(input("Input what you sale: "))
bonus=2000
if vendas>bonus:
    bonus=bonus*0.2
    print(f"{name}, win bonus of {bonus}, congratulation")
else:
    print(f"{name}, don't win bonus, that's too bad")
