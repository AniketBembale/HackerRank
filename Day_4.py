class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = age
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age<13 :
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

# Inputs

# 4
# -1
# 10
# 16
# 18