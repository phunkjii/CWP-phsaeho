import  sys

if len(sys.argv) == 1:
    print("none")
else:
    str = sys.argv[1].split()
    for i in str:
        if i.startswith("z") or i.startswith("Z"):
            print(f"z", end="")