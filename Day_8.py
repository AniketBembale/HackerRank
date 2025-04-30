n = int(input())

phonebook = {}
for _ in range(n):
    name, number = input().split()
    phonebook[name] = number

while True:
    try:
        name = input()
        if name in phonebook:
            print(f"{name}={phonebook[name]}")
        else:
            print("Not found")
    except EOFError:
        break


# Input
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry