import pygame

flag = False  
pygame.init() 

screen = pygame.display.set_mode((720, 480))  

back = pygame.Surface((720, 480))
back.fill((162, 250, 248))              
back = back.convert()      

a = [(270, 300), (370, 60), (470, 300), (245, 150), (495, 150), (270, 300)]
for i in range(1, len(a)):
    pygame.draw.line(back, (131, 52, 235), a[i-1], a[i], 2)

# pygame.draw.polygon(back, (0,180,0), ((100, 300), (200, 60), (300, 300), (75, 150), (325, 150)))  # by using polygon

screen.blit(back, (0, 0))
pygame.display.flip()  


while not flag: 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:    
            flag = True                