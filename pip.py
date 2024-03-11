from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["ID", "Name", "Gender", "Address"]
table.add_row(["001", 'Vireak', 'Male', "PhnomPenh"])
print(table)
