import pygame

pygame.init() 

screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("dodo")

# 배경 불러오기 그림파일 탭 우클릭 copy path shift Alt c
background = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/background.png")
# \ -> / or \\

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
    screen = pygame.display.set_mode((480, 640)) 
    screen.blit(background, (0, 0)) # 배경 좌표 설정\
    # screen.fill((0, 0, 255)) # 단순 색채우기 순서대로 RGB

    pygame.display.update() # 게임 화면 다시 그리기! 계속 호출해야함

pygame.quit()