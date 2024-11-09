from tabulator import tabulate
from storage import Storage

def formulaBMI(height, weight):
    """
        Takes height and weight and calculates BMI out of it. 
        height in meters and weight in kg
    """
    return round((weight/(height**2)), 2)

def BMIinterpretation(bmi):
    if (bmi <= 18.4):
        return "Underweight"
    elif (bmi >= 18.5 and bmi <= 24.9):
        return "Normal"
    elif (bmi >= 25 and bmi <= 39.9):
        return "Overweight"
    else:
        return "Obese"


def bmi():
    print("BMI WIZARD")
    username = input("Person Name: ")
    w = float(input("Weight (in Kg): "))
    h = float(input("Height (in Kg): "))
    bmi = formulaBMI(h, w)
    comment = BMIinterpretation(bmi)
    dataToPrint = [
        username,
        f"{w}Kg",
        f"{h}m",
        bmi,
        comment
    ]
    tabulate([
     [
        "Name",
        "Weight",
        "Height",
        "BMI",
        "Comment"    
     ],
     dataToPrint   
    ])
    
    ls = Storage()
    ls.appendRecord(dataToPrint)
    