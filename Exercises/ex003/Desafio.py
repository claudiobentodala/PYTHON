name=input("Input your name: ")
print("=======Now input your note, of all year======")
n1=float(input("Input first note: "))
n2=float(input("Input second note: "))
n3=float(input("Input theard note: "))
media=(n1+n2+n3)/3
print("=======Down's your status=======")
if media>=17 and media<=20 :
    print(f"{name}, foi aprovado com média: {media}" )
    print("Status: Excelente")
elif media>=14 and media<=20 :
    print(f"{name}, foi aprovado com média: {media}")
    print("Status: Bom")
elif media>=10 and media<=20:
    print(f"{name}, foi aprovado com média: {media}" )
    print("Status: Suficiente")
elif media>=0 and media<=10:
    print(f"{name}, foi raprovado com média: {media}" )
    print("Status: Mau")
else:
    print("some is wrong, try again")