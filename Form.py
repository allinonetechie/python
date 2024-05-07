FirstName = "Waqas"
LastName = "Ahmed"
Age = 17
DOB = "6/17/2023"
 
 ### Age Condition
if Age > 18:
    print("Welcome to our website! \n")
else:
    print("Visitors under age 18 are not allowed to visit out website. Please try again later when you are older than 18. \n")    


# Type Conditions

##Condition for FirstName
if not isinstance(FirstName, str): 
    print("InValid Type of FirstName, Please fix it! \n")
elif isinstance(FirstName, str):
    print("Valid Type of FirstName \n")
else:
    print("Something went wrong. Please check again! \n")     

## Condition for Age
if type(Age) != int:
    print("Invalid Type of Age. Please fix it! \n")  
elif type(Age) == int:
    print("Valid Type of Age \n")
else:
    print("Something went wrong. Please check again! \n")     
    


print(f"Hello {FirstName}  {LastName}, I see that your date of birth is {DOB}")