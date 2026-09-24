import sys

if len(sys.argv) != 3:
    print("none")
else:
    num = []
    i = int(sys.argv[1])
    while (i <= int(sys.argv[2])):
        num.append(i)
        i += 1
    print(num)