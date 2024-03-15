import pygame

pygame.init()

# to spam the pygame.KEYDOWN event every 100ms while key being pressed

while 1:
    for event in pygame.event.get():
        print("hello", event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print ('go forward')
            if event.key == pygame.K_s:
                print ('go backward')
        if event.type == pygame.KEYUP:
            print ('stop')
