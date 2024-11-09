from storage import Storage
from tabulator import tabulate

def history():
    ls = Storage()
    data = ls.readFile()
    tabulate([[
         "Name",
        "Weight",
        "Height",
        "BMI",
        "Comment"    
        ], *data])
    
    