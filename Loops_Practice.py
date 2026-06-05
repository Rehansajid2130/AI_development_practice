
# num = int(input("Starting number:"))

# while num > 0:
#     print(num)
#     num -=1

# print("Blast off!")

# for i in range(num):
#     print(num)
#     num-=1

# print("Blast off!")


# guessing game

# secret_num = 7
# userinput = 0

# while secret_num > 0:

#     userinput = int(input("Enter a number :"))

#     if userinput == secret_num:
#         print("Correct")
#         break
#     elif userinput > secret_num:
#         print("Too high")
#     elif userinput < secret_num:
#         print("Too low")
#     else:
#         print("Invalid input")


# items = ["Milk","Bread","Eggs"]
# print("Current Cart")
# for item in items:
#     print(item)

# New_item = input("Enter new item to add :")

# items.append(New_item)
# print("Updated Cart")

# for item in items:
#     print(item)
    

numbers = [4,10,2,99,23,50,100,200,239]
max = 0
ran = numbers.__len__()

for i in range(ran-1):
        if numbers[i+1] > numbers[i]:
            max = numbers[i+1]



print(max)
