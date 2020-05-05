
print("*************** First-Come-First-Serve Scheduling Algorithm ***************")
cylinders = [int(x) for x in input("Enter cylinder queue, seperated by space : ").split()]
head = int(input("Enter head : "))

cylinders.insert(0,head)

headmovement = 0

for i in range(len(cylinders)):
    if i > 0:
        headmovement += abs(cylinders[i] - cylinders[i-1])
    print(' -> ',cylinders[i],end="")

print("\ntotal head movement : ",headmovement," cylinders")