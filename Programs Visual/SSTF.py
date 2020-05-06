import pygame, os
from pygame.locals import *
pygame.init()
os.system('cls')

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

pygame.display.set_caption("SSTF")
win = pygame.display.set_mode((1000, 500),0,32)
win.fill((250,250,250))
font = pygame.font.SysFont('comicsans', 20)
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

    

for _ in range(len(cylinders)):
    pygame.time.delay(700)
    try:
        if abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head)-1 ]) < abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head)+1 ]) :
            headmovement += abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head) - 1 ])
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
        else:
            headmovement += abs(cylinders[cylinders.index(head)] - cylinders[cylinders.index(head) + 1 ])
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
    except:
        pass


font = pygame.font.SysFont('comicsans', 30)
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