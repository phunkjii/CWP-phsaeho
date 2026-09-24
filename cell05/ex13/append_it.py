import sys

if len(sys.argv) == 1:
    print("none")
else:
    for i in sys.argv[1:]:
        if i.endswith("ism"):
            continue
        else:
            print(i+"ism")