print("Guten Morgen Ja")
print("Guten Morgen Ja")
print("Guten Morgen Ja")

def greeting(name, course):
    print(f"Guten Morgen {name}, you are enrolled in {course} course")

greeting("Jay", "Engineering")
greeting("Kaja", "Law")
greeting("Nuru","Data Analytics")

import math
def areaCircle(radius):
    area=math.pi*radius**2
    return area

print(areaCircle(12))
print(areaCircle(5))
print(areaCircle(7))

# Create a function that calculates an individual BMI and return output as a statement
def totalBMI(height, weight):
    BMI=weight/(height**2)
    return f"Your BMI is {BMI}"

height = float(input("What is your height in metres: "))
weight = float(input("What is you weight in kgs: "))
print (totalBMI(height,weight))


def calc_average(score1,score2,score3):
    average=(score1+score2+score3)/3
    return average
def calc_grade(average):
    if average<0 or average>100:
        return "Invalid Number"
    elif average >=80:
        return "A"
    elif average >=70:
        return  "B"
    elif average >=60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"


from datetime import datetime
current_time= datetime.now()
print(current_time)