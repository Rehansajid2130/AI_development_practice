
from math import e


age = int(input("Enter your age :"))

if age < 13 and age >= 0:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
else:
    print("Adult")