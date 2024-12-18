grade = input("What is your grade percentage (Use % symbol)?: ")

if grade >= "70%" and grade < "80": 
    print("Your grade is C.")
    print("You have passed! Congrats!")
elif grade >= "80%" and grade < "90":
    print("Your grade is B.") 
    print("You have passed! Congrats!")
elif grade >= "90":
    print("Your grade is A!") 
    print("You have passed! Congrats!")
elif grade >= "60%" and grade < "70%":
    print("Your grade is D. :( )") 
    print("Sorry but you didn't pass! You can do these keep trying!")
else:
    if grade < "60%":
        print("Your grade is F. XD ") 
        print("Sorry but you didn't pass! You can do these keep trying!")
        




    
    