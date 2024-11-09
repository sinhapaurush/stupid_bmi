def rowPrinter(row, head=False):
    if (head):
        print("="*40)
    for i in row:
        print(i, end="\t")
    if (head):
        print()
        print("="*40, end="")
    print()
    
def tabulate(data):
    rowNum = 0
    for row in data:
        if (rowNum == 0):
            rowPrinter(row, True)
        else:
            rowPrinter(row)
        rowNum = rowNum + 1