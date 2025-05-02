N1 = int(input())
s1 = set(map(int, input().split()))
s2 = set(map(int,input().split()))
N2 = int(input())

difference = s1.difference(s2)
print(len(difference))

# INPUTS
# 9 
# 1 2 3 4 5 6 7 8 9
# 9
# 10 11 2 1 3 4 5 6 2


