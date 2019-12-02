
import sys

# game_functions
import pygame
from time import sleep
from pygame.sprite import Group, Sprite
import pygame.font


class Settings():
    """存储游戏设置的类"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        self.fleet_drop_speed = 10
        self.speed_scale = 1.1

        self.initialize_dynamic_settings()

    def  initialize_dynamic_settings(self):
        self.bullet_speed_factor = 3
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale

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

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('./python_base/data/chapter3/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.width:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed_factor * \
                                    self.settings.fleet_direction)
        self.rect.x = self.x 

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


class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit


class Button():
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event, ship):    
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
def check_play_button(settings, screen, stats, play_button, ship, aliens, bullets,
                     mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

def check_events(settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, play_button, ship, aliens,
            bullets, mouse_x, mouse_y)

def update_bullets(settings, screen, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_bullets_aliens_collisions(settings, screen, ship, aliens, bullets)

def check_bullets_aliens_collisions(settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.pygame.sprite.groupcollide(bullets, aliens, 
                        True, True, collided = None)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, ship, aliens)

def update_aliens(settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    if pygame.sprite.pygame.sprite.spritecollideany(ship, aliens):
        # print('Ship hit!!!')
        ship_hit(settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)

def update_screen(settings, screen, stats, ship, aliens, bullets, play_button):
    screen.fill(settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def ship_hit(settings, stats, screen, ship, aliens, bullets):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
        
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)



def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break
    
def get_alien_number_x(settings, alien_width):
    available_space = settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space / (2 * alien_width))
    return number_alien_x

def get_alien_number_rows(settings, ship_height,alien_height):
    availabels_space = settings.screen_height - 3 * alien_height - ship_height
    number_alien_rows = int(availabels_space / (2 * alien_height))
    return number_alien_rows

def creat_alien(settings, screen, aliens, alien_number, row_number):
        alien = Alien(settings, screen)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(settings, screen)
    number_alien_x = get_alien_number_x(settings, alien.rect.width)
    number_aline_rows = get_alien_number_rows(settings, ship.rect.height, 
                                                alien.rect.height)
    for row_number in range(number_aline_rows):
        for alien_number in range(number_alien_x):
            creat_alien(settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(settings, aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens:
        alien.rect.y += alien.settings.fleet_drop_speed
    settings.fleet_direction *= -1

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, 
                                        settings.screen_height))
    pygame.display.set_caption('雷电')
    play_button = Button(settings, screen, "Play")
    stats = GameStats(settings)
    ship = Ship(settings,screen)
    bullets = Group()
    # alien = Alien(settings, screen)
    aliens = Group()
    create_fleet(settings, screen, ship, aliens)
    running = True
    while running:
        check_events(settings, screen, stats, play_button, ship, 
                        aliens,bullets)
        if stats.game_active:
            ship.update()
            update_bullets(settings, screen, ship, aliens, bullets)
            update_aliens(settings, stats, screen, ship, aliens, bullets)
        update_screen(settings, screen, stats, ship, aliens, 
                        bullets, play_button)

run_game()
