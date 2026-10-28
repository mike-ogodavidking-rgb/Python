with open("notes.txt", "a") as file:
    file.write("This is a new note.\n")
    file.write("This is the second line.\n")

with open("notes.txt", "r") as file:
    content = file.read()
    
print(content)