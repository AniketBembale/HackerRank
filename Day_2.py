n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

# print(n1)
# print(s1)

print(len(s1.union(s2)))
