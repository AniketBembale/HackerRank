class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

        # Add your code here
    def computeDifference(self):
        max_val = max(self.__elements)
        min_val = min(self.__elements)
        self.maximumDifference = abs(max_val-min_val)

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


# Sample Input
# STDIN   Function
# -----   --------
# 3       __elements[] size N = 3
# 1 2 5   __elements = [1, 2, 5]

# Sample Output
# 4
