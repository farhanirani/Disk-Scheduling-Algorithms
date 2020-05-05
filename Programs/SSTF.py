
print("*************** Shortest-Seek-Time-First Scheduling Algorithm ***************")
cylinders = [int(x) for x in input("Enter cylinder queue, seperated by space : ").split()]
head = int(input("Enter head : "))

headmovement = 0
flag = False

#sort queue ascending
cylinders.sort()
for i in reversed(range(len(cylinders))):
    if head > cylinders[i]:
        cylinders.insert(i+1, head)
        flag = True
        break
if not flag:
    cylinders.insert(0,head)



for _ in range(len(cylinders)):
    print(' -> ',head,end="")
    try:
        if abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head)-1 ]) < abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head)+1 ]) :
            headmovement += abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head) - 1 ])
            pos = cylinders.index(head)
            cylinders.remove(head)
            head = cylinders[pos-1]
        else:
            headmovement += abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head) + 1 ])
            pos = cylinders.index(head)
            cylinders.remove(head)
            head = cylinders[pos]
    except:
        pass

print("\ntotal head movement : ",headmovement," cylinders")