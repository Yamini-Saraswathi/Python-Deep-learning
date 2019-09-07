lbs = []
s = int(input( "Number of students = "))
for i in range(s):
    temp = int(input("Enter weight in lb"))
    lbs.append(temp)
kgs = [i*0.4535 for i in lbs]
print(kgs)

