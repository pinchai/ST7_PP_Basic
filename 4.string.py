name = input("Please enter name(max=10): ")
while len(name) > 10:
    name = input("Please enter name(max=10): ")

value = input("Enter Value Age: ")
while value.isdigit() == False:
    value = input("Enter Value Age again 16-45: ")

gender = input("Please enter gender (male, female): ")
txt = "male female"
while (gender in txt) == False:
    gender = input("Please enter gender again (male, female): ")

score = int(input("Please enter student score 0-100: "))

print(f'==================')
print(f'Name: {name}')
print(f'Age: {name}')
print(f'Gender: {gender}')
print(f"Score: {score:.2f}")

