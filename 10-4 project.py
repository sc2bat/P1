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
current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, "images") 

background = pygame.image.load(os.path.join(image_path, "background22.png"))

stage = pygame.image.load(os.path.join(image_path, "stage22.png"))
stage_size = stage.get_rect().size 
stage_height = stage_size[1] 

character = pygame.image.load(os.path.join(image_path, "character22.png"))
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - stage_height - character_height

character_to_x = 0
character_speed = 5

weapon = pygame.image.load(os.path.join(image_path, "weapon22.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] 

weapons = []
weapon_speed = 10

# 공 만들기 ( 4개 크기에 대해 따로 처리)
ball_images = [ 
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따라 다른 속도
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값
# 나뉘어지는 공들
balls =[]
balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y의 좌표
    "img_idx" : 0, # 공의 이미지 인덱스
    "to_x" : 3, # x축 이동방향 , -3 왼쪽 , 3 오른쪽
    "to_y" : -6, # y축 이동방향,
    "init_spd_y" : ball_speed_y[0]}) # y 최초 속도

# 사라질 무기와 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1


running = True
while running:
    dt = clock.tick(60) 

# 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width /2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] 
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
    # 가로 벽에 닿으면 공이동 위치변경
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
    # 세로 스테이지에 튕겨 올라감
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


# 4. 충돌 처리
# 캐릭 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
        
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
#  공 rect 정보 업뎃
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        # 공 캐릭 충돌 체크
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기들의 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

        # 무기 rect 정보 업뎃
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
        # 충돌 체크  공과 무기가 닿으면 공 무기 둘다 사라짐  
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기 제거
                ball_to_remove = ball_idx # 해당 공 제거
                # 가장 작은 크기의 공이 아니면 다음 단계의 공으로 나눠줌
                if ball_img_idx < 3:
                    # 현재 공 크기 정보를 가지고오ㅗㅁ
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    balls.append({#왼쪽으로 튕기는 작은공
                        "pos_x" : ball_pos_x + (ball_width /2) - (small_ball_width /2),
                        "pos_y" : ball_pos_y + (ball_height /2) - (small_ball_height /2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : -3,
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})

                    balls.append({#오른쪽으로 튕기는 작은공
                        "pos_x" : ball_pos_x + (ball_width /2) - (small_ball_width /2),
                        "pos_y" : ball_pos_y + (ball_height /2) - (small_ball_height /2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : 3,
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})

                    

                break

# 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[ball_to_remove]
        weapon_to_remove = -1

# 5. 화면 그리기
    screen.blit(background, (0, 0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    # 공 그리기
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() 

pygame.time.delay(1000) 

pygame.quit()