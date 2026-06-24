def add(x , y):
    return x + y
def subt(x ,y):
    if (x > y):
        return(x - y)
    elif ( x == y):
        return("0")
    else: 
        return(y - x)
def mul(x,y):
    return x*y
def divide(x,y):
    try:
        print("division is : ", x/y)
    except ZeroDivisionError:
        print("not divisible")
def avg(x,y):
    return (x+y)/2
def square(x,y):
    select = int(input("choose between x and y"))
    if (select == x):
        return(x**2)
    else:
        return(y**2)
print("Please select an operation:\n" \
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Square\n" \
    "6. Average\n")
while True:


    choose= int(input("Choose any operation from 1 to 6:"))
    x = int(input("Enter the first numnber"))
    y = int(input("Enter the second number"))
    if choose == 1:
        print("sum of two numbers is :", add(x,y))
    elif choose == 2:
        print("subtraction of two numbers is :", subt(x,y))
    elif choose == 3:
        print("multiplication of two numbers is :", mul(x,y))
    elif choose == 4:
        print("division of two numbers is :", divide(x,y) )
    elif choose == 5:
        print("Average of two numbers is :", avg(x,y))
    elif choose == 6:
        print("square of two numbers is :",square(x,y))
    else:
        print("command not valid")
    again = input("do you want to continue{y/n):").lower()
    if again != "y":
        print("thank you")
        break



