import os

f = open("data.txt")
foo = f.readline()

if os.fork() == 0:
    foo = f.readline()
    print("child: ", foo)
else:
    foo = f.readline()
    print("parent: ", foo)

