print("WELCOME! \nRegister for COVID-19 vaccination and schedule your vaccination slots at the nearest vaccination centers.")
name=input("Please enter your Name:")
age= int(input("your age?:"))
if age >=45:
    print(f"your age is {age}") 
    health=input("If you are Diabetic type yes or no:")  
    if health=="yes":
        print("your vaccination appointment is confirmed please visit  the nearest vaccination center")
    elif health=="no":
         print("Sorry you are not elegible, please wait for the next vacinnation drive")

else:
    print("Sorry!!! You are under age for vaccination, please waite for the next vacinnation drive")