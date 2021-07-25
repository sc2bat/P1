import pygame

pygame.init() 

screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("dodo")

background = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/background.png")

# 캐릭(스프라이트) 불러오기
character =  pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/character.png")
# 캐릭은 움직임이 존재 
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height# 세로 가장 아래에 해당

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
    screen = pygame.display.set_mode((480, 640)) 
    screen.blit(background, (0, 0)) 

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기


    pygame.display.update() 

pygame.quit()