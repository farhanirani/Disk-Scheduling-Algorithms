import pygame, os
from pygame.locals import *
pygame.init()
os.system('cls')

print("*************** SCAN / elevator Scheduling Algorithm ***************")
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
cylinders.insert(0,0)
cylinders.append(maxnum-1)


pygame.display.set_caption("SCAN")
win = pygame.display.set_mode((1000, 500),0,32)
win.fill((250,250,250))
font = pygame.font.SysFont('Ariel', 20)
pygame.display.update()
currentY = 100

factor = 950 / max(cylinders)
cylindersOffset = []
for x in cylinders:
    cylindersOffset.append(int(x*factor + 20))

pygame.draw.line(win, (0,0,0), (20,50), (980,50), 2)
for i in range(len(cylinders)):
    text = font.render(str(cylinders[i]), 1, (0,0,0))
    win.blit(text, (cylindersOffset[i],35))
pygame.display.update()



run = True
previousValue = 0
for _ in range(len(cylinders)):
    if run:
        pygame.time.delay(700)
        print(' -> ',head,end="")
        try:
            if moveleft:
                previousValue = head
                pos = cylinders.index(head)
                i = pos * 1

                pygame.draw.line(win, (0,0,0), (cylindersOffset[i],currentY), (cylindersOffset[i-1],currentY+25), 2)
                pygame.draw.circle(win, (255,0,0), (cylindersOffset[i],currentY), 2)
                pygame.draw.circle(win, (255,0,0), (cylindersOffset[i-1],currentY+25), 2)
                pygame.display.update()
                currentY += 25

                cylindersOffset.remove(cylindersOffset[i])
                cylinders.remove(head)
                head = cylinders[pos-1]

                if pos == 1:
                    moveleft = False
                if head == maxnum - 1 and pos == 0:
                    run = False
                if head == 0 and len(cylinders) == 1:
                    run = False
            else:
                previousValue = head

                pos = cylinders.index(head)
                i = pos * 1

                pygame.draw.line(win, (0,0,0), (cylindersOffset[i],currentY), (cylindersOffset[i+1],currentY+25), 2)
                pygame.draw.circle(win, (255,0,0), (cylindersOffset[i],currentY), 2)
                pygame.draw.circle(win, (255,0,0), (cylindersOffset[i+1],currentY+25), 2)
                pygame.display.update()
                currentY += 25
            
                cylindersOffset.remove(cylindersOffset[i])
                cylinders.remove(head)
                head = cylinders[pos]

                if head == maxnum - 1:
                    moveleft = True
                if head == maxnum - 1 and pos == 0:
                    run = False
            if run:
                headmovement += abs(head - previousValue)
                # print(abs(head - previousValue))    

        except:
            pass
    

font = pygame.font.SysFont('Ariel', 30)
text = font.render("Total head movement : "+str(headmovement)+" cylinders", 1, (0,0,0))
win.blit(text, (450,450))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key ==K_ESCAPE:
                pygame.quit()
                exit()