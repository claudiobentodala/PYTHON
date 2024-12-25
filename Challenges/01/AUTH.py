emails=["blog@gmail.com","clau@gmail.com"]
def credence_email(email):
email=input("Email: ")
if email in emails:
else:
    print("ERROR: email invalid")
def auth(name,year,job):
    print("===PROFILE===")
    print(f"NAME: {name}")
    print(f"YEARS OLD: {year}")
    print(f"EMAIL: {email}")
    print(f"JOB: {job}")
name=input("Name: ")
years_old=int(input("Years: "))
year=2024-years_old