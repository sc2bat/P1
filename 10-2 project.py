# 무기와 키보드 이벤

import os
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
############################################################

# 1. 사용자 게임 초기화(배경, 게임 이미지, 좌표, 이속, 폰트)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

background = pygame.image.load(os.path.join(image_path, "background22.png"))

stage = pygame.image.load(os.path.join(image_path, "stage22.png"))
stage_size = stage.get_rect().size # stage 높이 위에 캐릭터 두기
stage_height = stage_size[1] 

character = pygame.image.load(os.path.join(image_path, "character22.png"))
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - stage_height - character_height

# 캐릭 이동
character_to_x = 0
character_speed = 5

# 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon22.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] 

# 무기 발사 횟수 여러번 가능이라 가정 리스트로
weapons = []
# 무기 이속 위로
weapon_speed = 10

running = True
while running:
    dt = clock.tick(60) 

# 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        # 캐릭 키보드
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                # pass
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width /2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

# 3. 캐릭터 위치 정의
    character_x_pos += character_to_x

    # 경계값
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 무기 위치 조정
    # 100, 200 -> 180, 160, 140 ...
    # 500, 200 -> 180, 160, 140 ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치 위로
    # 끝에 닿으면 사라지는 무기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]


# 4. 충돌 처리

# 5. 화면 그리기
    screen.blit(background, (0, 0))
    
    # 무기를 다른거보다 먼저 그리는 방향을 위해 이동
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    # 무기 그리기 리스트를 다 그려야하니 for
    # for weapon_x_pos, weapon_y_pos in weapons:
        # screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
       
    pygame.display.update() 

pygame.time.delay(1000) 

pygame.quit()