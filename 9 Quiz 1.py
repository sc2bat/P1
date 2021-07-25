# 하늘에서 떨어지는 공 피하기 게임을 만드시오.

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 자우로만 이동가능
# 2. 공은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 공을 피하면 다음 공이 다시 떨어짐
# 4. 캐릭터가 공과 충돌하면 게임 종료
# 5. FPS 는 30 으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭 : 70 * 70 - character.png
# 3. rhd : 70 * 70 - enemy.png


import random
import pygame    

############################################################
# 기본 초기화 (반드시 해야 하는 것들)

pygame.init() 

# 화면 크기 조절
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("dodo")

clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화(배경, 게임 이미지, 좌표, 이속, 폰트)
background = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/background.png")

character =  pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/character.png")

character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 10

# 적
ball =  pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/enemy.png")

ball_size = ball.get_rect().size
ball_width = ball_size[0] 
ball_height = ball_size[1] 
ball_x_pos = random.randint(0, screen_width - ball_width)
ball_y_pos = 0
ball_speed = 10


running = True
while running:
    dt = clock.tick(30) 

# 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_LEFT:
            to_x -= 5 
        elif event.key == pygame.K_RIGHT: 
            to_x += 5 

    if event.type == pygame.KEYUP: 
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0

# 3. 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    ball_y_pos += ball_speed
    if ball_y_pos > screen_height:
        ball_y_pos = 0
        ball_x_pos = random.randint(0, screen_width - ball_width)

    screen = pygame.display.set_mode((480, 640)) 
    screen.blit(background, (0, 0)) 
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ball, (ball_x_pos, ball_y_pos))  
            
# 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    if character_rect.colliderect(ball_rect):
        print("충돌함")
        running = False

# 5. 화면 그리기
       
    pygame.display.update() 

pygame.time.delay(2000) 

pygame.quit()