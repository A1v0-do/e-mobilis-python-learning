age= 27
if age>=35:
    print("You are a millenial")
else:
    print("You are a Gen z")

marks=int(input("What is your marks: "))
if marks <0 or marks >100:
    print("Invalid marks")
elif marks>=80:
    print("GRADE A")
elif marks>=70:
    print("GRADE B")
elif marks>=60:
    print("GRADE C")
elif marks>=50:
    print("GRADE D")
else:
    print("GRADE E")

# Loops

# for loop
for x in [12, 65,7,4,65, 7]:
    print(x)
# while loop
count = 1
while count <=5:
    print(count)
    count= count + 1