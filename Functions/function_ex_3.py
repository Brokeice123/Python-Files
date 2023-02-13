try:
    def age_months():
        age = int(input("Enter your age"))
        months = age*12
        print(f"You have lived for {months} months")
    age_months()
except:
    print("Not a number")