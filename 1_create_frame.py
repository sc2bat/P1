import pygame # 설치 확인 완료

# 뼈대부터
pygame.init() # 초기화 (필수)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("dodo") # 게임 이름
# 여기까지 프로그램이 실행은 되지만 후에 아무것도 없어서 프로그램이 자동 종료됨

# 이벤트 루프를 활용해 창 꺼짐 방지
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get(): # 입력 확인
        if event.type == pygame.QUIT: # 여러 이벤트 중 QUIT 라면 창닫기
            running = False

# pygame 종료
pygame.quit()