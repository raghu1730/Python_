print("For statement")
a=30
b=20
c=20
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("None of it")
print("For statement using logical operators")
if b > a and b > c:
    print("both the conditons are true")
else:
    print("False")
print("--------------------------------")
if b > a or b > c:
    print("both the conditons are true")
else:
    print("False")