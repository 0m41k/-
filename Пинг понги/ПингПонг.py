from pygame import *
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_H, player_W):
       super().__init__()
       self.H = player_H
       self.W = player_W
       self.image = transform.scale(image.load(player_image), (self.W, self.H))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed   
class Boll(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
 

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-Понг")
background = transform.scale(image.load("original.jpg"), (win_width, win_height))
player = Player('Ракетка.png', 625, win_height - 300, 4, 125, 65)
player2 = Player2('Ракетка.png', 10, win_height - 300, 4, 125, 65)
boll = Boll('мячик.png', win_width - 80, 280, 2, 45, 45)

game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        player2.update()
        boll.update()
        player.reset()
        player2.reset()
        boll.reset()

    display.update()
    clock.tick(FPS)
