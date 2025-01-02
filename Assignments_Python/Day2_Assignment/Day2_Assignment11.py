# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. 

amount = int(input("Please Enter the amount : "))

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50

print(f"The number of notes of 500 is {notes_500}")
print(f"The number of notes of 200 is {notes_200}")
print(f"The number of notes of 100 is {notes_100}")
print(f"The number of notes of 50 is {notes_50}")

