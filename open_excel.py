from prettytable import from_csv
with open("su15.csv") as fp:
    mytable = from_csv(fp)
    mytable.align = "l"
    print(mytable)
