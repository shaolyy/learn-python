
# game_functions
import pygame
import sys
from pygame.sprite import Sprite,Group

class Settings():
    """存储游戏设置的类"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

class Ship():
    """飞船类"""
    def __init__(self, settings, screen):
        self.screen = screen

        self.image = pygame.image.load('./python_base/data/chapter3/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.settings = settings
        self.center = float(self.rect.centerx)
        
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center
            

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    """对子弹进行管理的类"""
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
def check_keyup_events(event, ship):    
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))

def update_screen(settings, screen, ship, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, 
                                        settings.screen_height))
    pygame.display.set_caption('雷电')
    ship = Ship(settings,screen)
    bullets = Group()
    running = True
    while running:
        check_events(settings, screen, ship, bullets)
        ship.update()
        update_bullets(bullets)
        update_screen(settings, screen, ship, bullets)

run_game()
