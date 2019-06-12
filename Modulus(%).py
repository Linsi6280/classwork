#quesetion 2
total_minutes = int(input("Please enter the total minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{hours}h, {minutes}min")


#question 3
frame_count = int(input("Please enter the number of frame: "))
if frame_count % 60 == 0:
    print("It will allow a lazer to be shot.")
else:
    print("It will not allow a lazer to be shot.")   
    
    
#question 4
total_cent = int(input("Please enter the total cent: "))
dollars = total_cent // 100
cents = total_cent % 100
print(f"${dollars}, {cents}cents")


#question 5
number = int(intput("Please enter a 3-digit number: "))
first = number // 100
second = number % 100 //10
third = number % 10
print(first + second + third)



#question 6
cents = int(input("Enter the amount of cents: "))
toonies = cents // 200
cents = cents % 200  # calculate remaining cents after toonies
loonies = cents // 100
cents = cents % 100
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickles = cents // 5
cents = cents % 5
pennies = cents

print(f"Toonies: {toonies}")
print(f"Loonies: {loonies}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickles: {nickles}")
print(f"Pennies: {pennies}")



#question 7
id = int(intput("Please enter your student id: "))
g = 4
group = int((id + 1) // g)
print(f"id: {id}")
print(f"You are in group #{group}.")


