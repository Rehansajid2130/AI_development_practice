# user = {
# "name":"Cyrus",
# "age":20,
# "skill":"JavaScript"
# }

# print(f"Name {user["name"]} age {user["age"]} skill {user["skill"]}")

# print("Update the values:")

# user["name"]=input("Enter name:")
# user["age"]=int(input("Enter age:"))
# user["skill"]=input("Enter skill:")


# print(f"Name {user["name"]} age {user["age"]} skill {user["skill"]}")


# from re import A


# students = {
# "Ali":85,
# "Ahmed":91,
# "Sara":77
# }

# userinput = input("Enter student name :")

# if userinput == "Ali":
#      print(f"{students['Ali']}")
# elif userinput == "Ahmed":
#     print(f"{students['Ahmed']}")
# elif userinput == "Sara":
#     print(f"{students["Sara"]}")
# else:
#     print("Student Not found")


# user = {
#     "name": "Cyrus",
#     "age": 20,
#     "skills": ["Python", "JavaScript", "AI"]
# }
# print(f"name {user["name"]} age {user["age"]} skills: {[user['skills']]} ")

# student = {
#     "name": "Ali",
#     "marks": {
#         "math": 85,
#         "english": 78,
#         "science": 90
#     }
# }

# print(f"Student Name : {student["name"]} marks: Maths:{student["marks"]["math"]} English :{student['marks']["english"]} Science: {student["marks"]["science"]}" )

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# data = response.json()
# print(data)
# print(data["email"])
# print(data["name"])
# print(data["company"]["name"])
# print(data["address"]["city"])


# Ai system
print("You just connected to Chat")

loop = 2
while loop > 0:
    print("You:")
    userinput = input("")
    if userinput == "hello":
        print("AI:hi")
    elif userinput == "how are you":
        print("AI:I'm AI, I don't feel but I'm working!")
    elif userinput == "bye":
        print("AI:Goodbye!")
        break
    else:
        print("I don't understand")

