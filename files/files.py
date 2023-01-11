name = input("Enter the name of the Document and its extension e.g. example.pdf: \n")


with open(name) as file:
    content = file.read()

print(content)