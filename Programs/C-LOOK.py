
print("*************** C-LOOK Scheduling Algorithm *************** ")
maxnum = int(input("Enter total cylinder space on disk drive : "))
cylinders = [int(x) for x in input("Enter cylinder queue, seperated by space : ").split()]
head = int(input("Enter head / current cylinder : "))
prev = int(input("Enter previous serviced cylinder( if moving right, enter any value less than head ) : "))

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

maxnum = 1 + cylinders[-1]
previousValue = 0

if prev > head:
    moveleft = True
else:
    moveleft = False

for _ in range(len(cylinders)):
    if not moveleft:
        print(' -> ',head,end="")
        try:
            previousValue = head
            pos = cylinders.index(head)
            cylinders.remove(head)
            if previousValue == maxnum - 1:
                pos = 0
            head = cylinders[pos]

            headmovement += abs(head - previousValue)
        except:
            pass
    else:
        print(' -> ',head,end="")
        try:
            previousValue = head
            pos = cylinders.index(head)
            cylinders.remove(head)
            if previousValue == maxnum - 1:
                pos = len(cylinders)
            head = cylinders[pos-1]

            headmovement += abs(head - previousValue)
        except:
            pass



print("\ntotal head movement : ",headmovement," cylinders")