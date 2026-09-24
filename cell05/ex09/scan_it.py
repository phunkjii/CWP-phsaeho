import sys

if len(sys.argv) == 0:
    print("none")
else:
    cnt = sys.argv[2].count(sys.argv[1])
    if cnt == 0:
        print("none")
    else:
        print(cnt)