# project) 오락식 Pang 게임 만들기

# [게임 조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 2. 스페이스를 누르면 무기를 쏘아 올림
# 3. 큰 공 1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공을 없애면 게임 졸료(성공)
# 6. 캐릭터는 공에 닿으면 게임 종료 (실패)
# 7. 시간 제한 99초 초과 시 게임 종료 (실패)
# 8. FPS 는 30으로 고정 (필요시 speed 값을 조정)

# [게임 이미지]
# 1. 배경 : 640 * 480 (가로 세로) - background22.png
# 2. 무대 : 640 * 50 - stage22.png
# 3. 캐릭터 : 60 * 33 - character22.png
# 4. 무기 : 20 * 430 - weapon22.png
# 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png

import random
import pygame

############################################################
# 기본 초기화 (반드시 해야 하는 것들)

pygame.init() 

# 화면 크기 조절
screen_width = 640
screen_height = 480 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("ball")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/background22.png")

stage = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/stage22.png")
stage_size = stage.get_rect().size
stage_width = stage_size[0] 
stage_height = stage_size[1] 
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

character = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/character22.png")
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = stage_y_pos - character_height
to_x = 0
character_speed = 10

weapon = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/weapon22.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] 
weapon_height = weapon_size[1] 
weapon_x_pos = (weapon_width / 2) - (weapon_width / 2) 
weapon_y_pos = screen_height + weapon_height
to_x = 0
weapon_speed = 20

balloon1 = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/balloon1.png")
balloon2 = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/balloon2.png")
balloon3 = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/balloon3.png")
balloon4 = pygame.image.load("C:/Users/Dero/Desktop/PythonWorkspace/pygame_basic/balloon4.png")


game_font = pygame.font.Font(None, 30)
total_time = 99
start_ticks = pygame.time.get_ticks()


############################################################

# 1. 사용자 게임 초기화(배경, 게임 이미지, 좌표, 이속, 폰트)

running = True
while running:
    dt = clock.tick(30)

# 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_LEFT:
            to_x -= character_speed
        elif event.key == pygame.K_RIGHT: 
            to_x += character_speed
        elif event.key == pygame.K_SPACE: 
            to_y -= weapon_speed

    if event.type == pygame.KEYUP: 
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            to_y = 0

# 3. 캐릭터 위치 정의


# 4. 충돌 처리

# 5. 화면 그리기
       

    screen.blit(background, (0, 0))
    screen.blit(stage, (stage_x_pos, stage_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() 

pygame.time.delay(2000) 

pygame.quit()