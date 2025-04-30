# Read input
N, M = map(int, input().split())
print(N,"\n",M)

# Top half
for i in range(1, N, 2):
    pattern = (".|." * i).center(M, "-")
    print(pattern)
    

# Middle line
print("WELCOME".center(M, "-"))

# Bottom half (mirror of the top)
for i in range(N-2, 0, -2):
    pattern = (".|." * i).center(M, "-")
    print(pattern)
