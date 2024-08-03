# Age Assignments Based on the Riddle

# Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.



name:str = "Anton"
age:int = 21
city:str = "New York"

name1:str = "Beth"
age1:int = (age + 6)
city1:str = "Lahore"

name2:str = "Chen"
age2:int = (age1 + 20)
city2:str = "Karachi"

name3:str = "Drew"
age3:int = (age2 + age)
city3:str = "Paris"

name4:str = "Ethan"
age4:int = (age2)
city4:str = "Los agles"

print(f"{name} is {age} years old and lives in {city}")
print(f"{name1} is {age1} years old and lives in {city1}")
print(f"{name2} is {age2} years old and lives in {city2}")
print(f"{name3} is {age3} years old and lives in {city3}")
print(f"{name4} is {age4} years old and lives in {city4}")

#output
# Anton is 21 years old and lives in New York
# Beth is 27 years old and lives in Lahore
# Chen is 47 years old and lives in Karachi
# Drew is 68 years old and lives in Paris
# Ethan is 47 years old and lives in Los agles
