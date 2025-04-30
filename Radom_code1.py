# s = set('HackerRank')
# print((s))
# s.add('H')
# print((s))
# print(s.add('HackerRank')) 
# print(s)
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5