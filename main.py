from pygame import *
# базовый класс для спрайтов
class GameSprite(sprite.Sprite):
    """
    image_file - имя файла с картинкой для спрайта
    x - координата x спрайта
    y - координата y спрайта
    speed - скорость спрайта
    size_x - размер спрайта по горизонтали
    size_y - размер спрайта по в ертикали
    """

    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()  # конструктор суперкласса
        self.image = transform.scale(
            image.load(image_file), (size_x, size_y)
        )  # создание внешнего вида спрайта - картинки
        self.speed = speed  # скорость
        self.rect = (
            self.image.get_rect()
        )  # прозрачная подложка спрайта - физическая модель
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        # отобразить картинку спрайта в тех же координатах, что и его физическая модель
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс для игрока
class Player(GameSprite):
    # метод для управления игрока стрелками клавиатуры
    def update_r(self):
        # получаем словарь состояний клавиш
        keys = key.get_pressed()

        # если нажата клавиша влево и физическая модель не ушла за левую границу игры
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        # если нажата клавиша вправо и физическая модель не ушла за правую границу игры
        if keys[K_DOWN] and self.rect.y < height - 150:
            self.rect.y += self.speed

    def update_l(self):
        # получаем словарь состояний клавиш
        keys = key.get_pressed()

        # если нажата клавиша влево и физическая модель не ушла за левую границу игры
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        # если нажата клавиша вправо и физическая модель не ушла за правую границу игры
        if keys[K_s] and self.rect.y < height - 150:
            self.rect.y += self.speed

# переменная окончания игры
finish = False  # когда True, то спрайты перестают работать
# переменная завершения программы
game = True  # завершается при нажатии кнопки закрыть окно

# размеры окна
width = 600
height = 500

# создание окна
window = display.set_mode((width, height))
display.set_caption("Ping Pong")
back = (200, 255, 255)
window.fill(back)
clock = time.Clock()
FPS = 60


# шрифт
font.init()
font1 = font.SysFont("Arial", 36)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

racket1 = Player("derevo.png", 30, 200, 4, 50, 150)
racket2 = Player("derevo.png", 520, 200, 4, 50, 150)
ball = GameSprite('stive.jpg', 200, 200, 4, 50, 50)
ball_x = 3
ball_y = 3


# игровой цикл
while game:
    # обработка нажатия кнопки Закрыть окно
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(racket1,ball):
            ball_x *= -1

        if sprite.collide_rect(racket2,ball):
            ball_x *= -1

        if ball.rect.y < 0 or ball.rect.y > height - 50:
            ball_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))

        if ball.rect.x > width - 50:
            finish = True
            window.blit(lose2,(200,200))

        racket1.reset()
        racket2.reset()
        ball.reset()
        
    display.update()
    clock.tick(FPS)
