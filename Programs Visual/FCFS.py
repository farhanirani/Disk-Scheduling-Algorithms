import pygame, os
from pygame.locals import *
pygame.init()
os.system('cls')

print("*************** First-Come-First-Serve Scheduling Algorithm ***************")
cylinders = [int(x) for x in input("Enter cylinder queue, seperated by space : ").split()]
head = int(input("Enter head : "))

cylinders.insert(0,head)

headmovement = 0

pygame.display.set_caption("FCFS")
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


for i in range(len(cylinders)):
    pygame.time.delay(700)
    try:
        if i > 0:
            headmovement += abs(cylinders[i] - cylinders[i-1])

        pygame.draw.line(win, (0,0,0), (cylindersOffset[i],currentY), (cylindersOffset[i+1],currentY+25), 2)
        pygame.draw.circle(win, (255,0,0), (cylindersOffset[i],currentY), 2)
        pygame.draw.circle(win, (255,0,0), (cylindersOffset[i+1],currentY+25), 2)
        pygame.display.update()
        currentY += 25

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