# user input
name="Xavier"
print(name)

first_name= input("Enter your First Name: ")
last_name= input("Enter your Last Name: ")
age= input("Enter your age: ")
# print(first_name)
# print(last_name)
print(f"{first_name} {last_name} you are {age} years old")
num1= int (input("Enter first number: "))
num2= int( input("Enter second number: "))
sum=num1+num2
print(sum)

price = float(input("Enter unit price: "))
quantity = float(input("Enter number of units: "))
total_amount= price*quantity
print(total_amount)

# Calculate an individual's BMI. Using height and weight
weight= float(input("Enter your weight: "))
height1= float(input("Enter your height: "))
bmi=weight/height1
print(bmi)