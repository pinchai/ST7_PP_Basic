# -----Input With validation---------
# 'id': (auto increment) 1,
# 'name': <50'sopheaktra',
# 'gender': 'male, female',
# 'age': 18->35,
# 'DOB': '12-02-2001',
# 'POB': 'SiemReap',
# 'Group': 'ST7',
# 'Major': 'MIS, BIT, GD',

# -----Output as table layout ---------
# ID    Name    Gender  Age     DOB         POB     Group   Major
# 1     Chai    Male    29      00-00-0000  BTB     SU9     MIS
# 2     Chai    Male    29      00-00-0000  BTB     SU9     MIS
# 2     Chai    Male    29      00-00-0000  BTB     SU9     MIS
# 2     Chai    Male    29      00-00-0000  BTB     SU9     MIS
# 2     Chai    Male    29      00-00-0000  BTB     SU9     MIS
# 2     Chai    Male    29      00-00-0000  BTB     SU9     MIS
# 2     Chai    Male    29      00-00-0000  BTB     SU9     MIS

name = input('Enter name: ')
gender = input('Enter gender (male, female): ')
student_list = []
current_input = {
    'name': name,
    'gender': gender,
}
student_list.append(current_input)

print("Name")
print(student_list)
