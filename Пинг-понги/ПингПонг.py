from pygame import *
from random import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_H, player_W):
        super().__init__()
        self.W = player_W
        self.H = player_H
        self.image = transform.scale(image.load(player_image), (self.W, self.H))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed   
            

play1 = 0
play2 = 0

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-Понг")
background = transform.scale(image.load("поле.jpg"), (win_width, win_height))

player = Player('Ракетка 2ю0.jpg', 680, win_height - 300, 4, 125, 10)
player2 = Player('Ракетка 2ю0.jpg', 10, win_height - 300, 4, 125, 10)
ball = Player('мячик.png',350, 250, 4, 45, 45)
Reset = Player('рестарт.png', 300, 200, 0, 100, 100)

game = True
finish = False

clock = time.Clock()
FPS = 90

font.init()
font = font.SysFont('Comic Sans', 55)
lose1 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
play1l = font.render(str(play1), True, (0, 0, 0))
play2l = font.render(str(play2), True, (0, 0, 0))

speed_x = 3 
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        keys = key.get_pressed()
        if keys[K_r]:
                if finish != False:
                    player.rect.x = 680 
                    player.rect.y = win_height - 300
                    player2.rect.x = 10
                    player2.rect.y = win_height - 300
                    ball.rect.x = 350
                    ball.rect.y = 250
                    finish = False
       
    if finish != True:
        window.blit(background,(0, 0))
        player.update_r()
        player2.update_l()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        play1l = font.render(str(play1), True, (0, 0, 0))
        play2l = font.render(str(play2), True, (0, 0, 0))
        
        
        if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1
            time.delay(20)
        if ball.rect.y > 455 or ball.rect.y < 0:
            speed_y *= -1
            time.delay(20)
        if ball.rect.x < 0:
            finish = True
            play2 += 1
            window.blit(lose1, (200, 100))
            Reset.reset()
            if speed_x > 0:
                speed_x *= -1
        if ball.rect.x > 655:
            finish = True
            play1 += 1
            window.blit(lose2, (200, 100))    
            Reset.reset()
            if speed_x < 0:
                speed_x *= -1
        window.blit(play1l, (310,5))
        window.blit(play2l, (370,5))
        player.reset()
        player2.reset()
        ball.reset()
        
    display.update()
    clock.tick(FPS)
