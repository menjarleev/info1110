print("Hello")
print("I will add two numbers for you")
print("Enter two whole numbers on one line")
line = input()
n1, n2, n3 =  line.split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
print("The sum of your numbers is: ")
print(n1+n2+n3)