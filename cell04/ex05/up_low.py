text = input("")
result = ""

for i in text:
    if i.islower():
        text += i
        print(i.upper(), end="")
    elif i.isupper():
        text += i
        print(i.lower(), end="")