
print("*************** LOOK Scheduling Algorithm ***************")
maxnum = int(input("Enter total cylinder space on disk drive : "))
cylinders = [int(x) for x in input("Enter cylinder queue, seperated by space : ").split()]
head = int(input("Enter head / current cylinder : "))
prev = int(input("Enter previous serviced cylinder( if moving left, enter any value greater than head ) : "))

headmovement = 0
flag = False

if prev > head:
    moveleft = True
else:
    moveleft = False

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


run = True
previousValue = 0
for _ in range(len(cylinders)):
    if run:
        print(' -> ',head,end="")
        try:
            if moveleft:
                previousValue = head

                pos = cylinders.index(head)
                cylinders.remove(head)
                head = cylinders[pos-1]

                if pos == 1:
                    moveleft = False
            else:
                previousValue = head

                pos = cylinders.index(head)
                cylinders.remove(head)
                head = cylinders[pos]

                if head == maxnum - 1:
                    moveleft = True
            if run:
                headmovement += abs(head - previousValue)
                # print(abs(head - previousValue))    

        except:
            pass
    

print("\ntotal head movement : ",headmovement," cylinders")