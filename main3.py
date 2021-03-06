import pygame
import random
import math

# Initialises pygame
pygame.init()


# Boss
class enemy:
    def __init__(self):
        self.enemylooks = pygame.image.load('ufo.png')
        self.enemyX = random.randint(0, 736)
        self.enemyY = random.randint(50, 108)
        self.enemy_changeX = 0.3
        self.enemy_changeY = 0.3

    def enemy(self, x, y):
        screen.blit(self.enemylooks, (x, y))

    # Small enemies


class small_enemies:
    def __init__(self):
        self.enemylooks = pygame.image.load('battleship.png')
        self.enemyX = random.randint(0, 736)
        self.enemyY = random.randint(50, 108)
        self.enemy_changeX = 0.3
        self.enemy_changeY = 0.3

    def enemy(self, x, y):
        screen.blit(self.enemylooks, (x, y))

    # Screen


screen = pygame.display.set_mode((800, 600))
run = True

# Player
playerImage = pygame.image.load("spaceship.png")
playerX = 336
playerY = 450

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1.5
bullet_state = "start"


def fire_bullet_enemy(x, y):
    global bullet_enemy_state
    bullet_enemy_state = "fire"
    screen.blit(bulletImg_enemy, (x, y - 4))


# Player location
def playerLoc(X, Y):
    screen.blit(playerImage, (X, Y))


# Firing a bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y + 13))


# Enemy collision
def isCollision(enemyX, enemyY, bulletX, bulletY, radius):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < radius:
        return True
    else:
        return False


# showing score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)

textX = 10
textY = 10

# showing enemy health
enemy_health_value = 100
health_font = pygame.font.Font('freesansbold.ttf', 20)

text1 = 600
text2 = 570

# showing player health
player_health_value = 100
health_player_font = pygame.font.Font('freesansbold.ttf', 20)

text3 = 10
text4 = 570

# you win text
Win_font = pygame.font.Font('freesansbold.ttf', 64)

# you lose text
lose_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_enemy_health(x, y):
    Enemy_health = health_font.render("Enemy health :" + str(enemy_health_value), True, (255, 255, 255))
    screen.blit(Enemy_health, (x, y))


def show_player_health(x, y):
    player_health = health_player_font.render("My health :" + str(player_health_value), True, (255, 255, 255))
    screen.blit(player_health, (x, y))


def You_Win_text():
    You_Win_text = Win_font.render("YOU WIN", True, (255, 255, 255))
    screen.blit(You_Win_text, (275, 250))


def You_lose_text():
    You_lose_text = lose_font.render("YOU LOSE", True, (255, 255, 255))
    screen.blit(You_lose_text, (250, 250))


# Initialize playerX_update
playerX_update = 0

# Creating enemies
boss = enemy()
chindi = small_enemies()
chindi2 = small_enemies()
chindi3 = small_enemies()
randchindi = small_enemies()
list_of_object = [boss, chindi, chindi2, chindi3]

bulletImg_enemy = pygame.image.load('bullet.png')
bulletY_enemy_change = 0.75
bulletX_enemy_change = 0
bullet_enemy_state = "start"

# Game running
while run:
    # Screen fill
    screen.fill((0, 0, 0))

    # Processes next event in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_update = 0.5
            elif event.key == pygame.K_LEFT:
                playerX_update = -0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "start":
                    bulletX = playerX + 56
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_update = 0

    # Player movement, makes sure player does not leave the screen
    playerX += playerX_update
    if playerX <= 0:
        playerX = 0
    if playerX >= 672:
        playerX = 672

    # Enemy movements
    for object in list_of_object:

        # You Win
        if enemy_health_value == 0:
            for j in list_of_object:
                object.enemyx = 2000
            You_Win_text()
            break
        # You lose
        if player_health_value == 0:
            for p in list_of_object:
                object.enemyx = 2000
            You_lose_text()
            break

        object.enemyX += object.enemy_changeX
        object.enemyY += object.enemy_changeY

        # boundary detection
        if object.enemyX <= 0:
            object.enemy_changeX = 0.3
        elif object.enemyX >= 736:
            object.enemy_changeX = -0.3

        if object.enemyY <= 0:
            object.enemy_changeY = 0.3
        elif object.enemyY >= 108:
            object.enemy_changeY = -0.3

        # Collision
        collision = isCollision(object.enemyX + 32, object.enemyY, bulletX, bulletY, 32)
        if collision:
            bulletY = 480
            bullet_state = "start"
            if object != boss:
                list_of_object.pop(list_of_object.index(object))
            if object == boss:
                enemy_health_value -= 25

        # Changes enemy location
        object.enemy(object.enemyX, object.enemyY)

    # Reset bullet when it leaves the screen
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "start"
        # bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bullet_enemy_state == "start":
        randchindi = list_of_object[random.randint(0, len(list_of_object) - 1)]
        bulletY_enemy = randchindi.enemyY
        bulletX_enemy = randchindi.enemyX
        bulletX_enemy = randchindi.enemyX + 24

    fire_bullet_enemy(bulletX_enemy, bulletY_enemy)

    if bulletY_enemy > 550:
        bulletY_enemy = randchindi.enemyY
        bulletY_enemy = randchindi.enemyY
        bullet_enemy_state = "start"
    if bullet_enemy_state == "fire":
        fire_bullet_enemy(bulletX_enemy, bulletY_enemy)
        bulletY_enemy += bulletY_enemy_change
        if isCollision(playerX + 56, playerY, bulletX_enemy, bulletY_enemy, 60):
            bullet_enemy_state = "start"
            player_health_value -= 25

            if player_health_value == 0:
                for object in list_of_object:
                    object.enemyX = 2000
                You_lose_text()

    playerLoc(playerX, playerY)

    show_enemy_health(text1, text2)
    show_player_health(text3, text4)
    # Update the screen
    pygame.display.update()
