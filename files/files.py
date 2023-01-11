name = input("Enter the name of the Document and its extension e.g. example.pdf: \n")

try:
    with open(name) as file:
        content = file.read()
    print(content)

except Exception:
    print("-----!!!please check the file name and try again!!!-----")