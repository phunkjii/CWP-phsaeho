import sys

args = []

if len(sys.argv) <= 2:
    print("none")
else:
    for i in sys.argv:
        args.append(i)
    for i in range(len(sys.argv)-1, 0, -1):
        print(sys.argv[i])