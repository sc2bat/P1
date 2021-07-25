# 프레임 배경 스테이지 캐릭터

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

# 1 배경
background = pygame.image.load(os.path.join(image_path, "background22.png"))
# 2 stage
stage = pygame.image.load(os.path.join(image_path, "stage22.png"))
stage_size = stage.get_rect().size # stage 높이 위에 캐릭터 두기
stage_height = stage_size[1] 
# 3 character
character = pygame.image.load(os.path.join(image_path, "character22.png"))
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - stage_height - character_height

running = True
while running:
    dt = clock.tick(60) 

# 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

# 3. 캐릭터 위치 정의

# 4. 충돌 처리

# 5. 화면 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
       
    pygame.display.update() 

pygame.time.delay(1000) 

pygame.quit()