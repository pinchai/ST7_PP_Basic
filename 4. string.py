name = input("Please enter name(max=10): ")
while len(name) > 10:
    name = input("Please enter name(max=10): ")

gender = input("Please enter gender (male, female): ")
txt = "male female"
while (gender in txt) == False:
    gender = input("Please enter gender again (male, female): ")

print('name: '+name)
print('gender: '+gender)

