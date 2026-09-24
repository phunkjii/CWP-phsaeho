import sys

if len(sys.argv) == 1:
    print("none")
else:
    arg = sys.argv[1]
    usr = input("What was the parameter? ")
    if usr == arg:
        print("Good job!")
    else:
        print("Nope, sorry...")