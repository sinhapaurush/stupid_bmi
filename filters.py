from storage import Storage
from tabulator import tabulate
def filterbmis():
    filter_name = input("Enter name to filter: ")
    ls = Storage()
    data = ls.readFile()
    dataToShow = []
    
    for row in data:
        if row[0] == filter_name:
            dataToShow.append(row)
    
    tabulate([ ["Name",
        "Weight",
        "Height",
        "BMI",
        "Comment"], *dataToShow])
    