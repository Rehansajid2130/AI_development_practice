# def calculate(num1,num2):
#     return num1+num2



# num1 = int(input("Enter 1st number :"))
# num2 = int(input("Enter 2st number :"))

# result = calculate(num1,num2)
# print(result)

# def greet(name):
#     print(f"Welcome {name}!")


# name = "Cyrus"

# greet(name)

def Addtask(NewTask):
    tasks.append(NewTask)
    ViewTask(tasks)
    return tasks


def ViewTask(tasks):
    for task in tasks:
        print(task)

def RemoveTask(tasks):
    tasks.pop(1)


tasks = ["Python" , "javascript"]

loop = 1
while loop > 0:

    print("1 Add task")
    print("2 View task")
    print("3 Remove task")
    print("4 Exit")
    inputt = int(input("Enter a number:"))

    if inputt == 1:
        userinput = input("Enter task")
        Addtask(userinput)
        
    elif inputt == 2:
        ViewTask(tasks)
    elif inputt == 3:
        RemoveTask(tasks)
    elif inputt == 4:
        loop = -1
    else:
        print("Invalid input")

