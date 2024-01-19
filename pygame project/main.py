import pygame
import os
import random
import sqlite3
screen_rect = (0, 0, 800, 470)
screen = pygame.display.set_mode((800, 470))
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image


class Backon:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.backon = load_image("backon.png", colorkey=-1)

    @staticmethod
    def sprite():
        return load_image("backon.png", colorkey=-1)

    def price(self):
        price = 7
        return price

    def draw(self):
        back = pygame.transform.scale(self.backon, (40, 40))
        b_coord = (self.coord[0] - 20, self.coord[1] - 20)
        self.screen.blit(back, b_coord)
        pygame.display.flip()

class Sausage:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.sausage = load_image("sausage.png", colorkey=-1)

    @staticmethod
    def sprite():
        return load_image("sausage.png", colorkey=-1)

    def price(self):
        price = 6
        return price

    def draw(self):
        mash = pygame.transform.scale(self.sausage, (40, 40))
        m_coord = (self.coord[0] - 20, self.coord[1] - 20)
        self.screen.blit(mash, m_coord)
        pygame.display.flip()

class Pinapple:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.pineapple = load_image("pineapple.png", colorkey=-1)

    @staticmethod
    def sprite():
        return load_image("pineapple.png", colorkey=-1)

    def price(self):
        price = 10
        return price

    def draw(self):
        mash = pygame.transform.scale(self.pineapple, (40, 40))
        m_coord = (self.coord[0] - 20, self.coord[1] - 20)
        self.screen.blit(mash, m_coord)
        pygame.display.flip()


class Tomato():
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.tomato = load_image("tomato.png", colorkey=-1)

    @staticmethod
    def sprite():
        return load_image("tomato.png", colorkey=-1)

    def price(self):
        price = 7
        return price

    def draw(self):
        tom = pygame.transform.scale(self.tomato, (40, 40))
        t_coord = (self.coord[0] - 20, self.coord[1] - 20)
        self.screen.blit(tom, t_coord)
        pygame.display.flip()



class Pepperoni:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.pepperony = load_image("pepperoni.png", colorkey=-1)

    @staticmethod
    def sprite():
        return load_image("pepperoni.png", colorkey=-1)

    def price(self):
        price = 11
        return price

    def draw(self):
        pep = pygame.transform.scale(self.pepperony, (40, 40))
        p_coord = (self.coord[0] - 20, self.coord[1] - 20)
        self.screen.blit(pep, p_coord)
        pygame.display.flip()


class Mashroom:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.mashroom = load_image("mashroom.png", colorkey=-1)

    @staticmethod
    def sprite():
        return load_image("mashroom.png", colorkey=-1)

    def price(self):
        price = 5
        return price

    def draw(self):
        mash = pygame.transform.scale(self.mashroom, (40, 40))
        m_coord = (self.coord[0] - 20, self.coord[1] - 20)
        self.screen.blit(mash, m_coord)
        pygame.display.flip()


class Pepper:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.pepper = load_image("pepper.png")

    @staticmethod
    def sprite():
        return load_image("pepper.png", colorkey=-1)

    def price(self):
        price = 6
        return price

    def draw(self):
        pep = pygame.transform.scale(self.pepper, (40, 40))
        p_coord = (self.coord[0] - 20, self.coord[1] - 20)
        self.screen.blit(pep, p_coord)
        pygame.display.flip()


class Sauce:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord

    @staticmethod
    def sprite():
        return load_image("sause.png", colorkey=-1)

    def price(self):
        price = 0.1
        return price

    def draw(self):
        pygame.draw.circle(self.screen, (217, 67, 67), self.coord, 10)
        pygame.display.flip()


class Cheese:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord

    @staticmethod
    def sprite():
        return load_image("cheese.png", colorkey=-1)

    def price(self):
        price = 0.1
        return price

    def draw(self):
        pygame.draw.circle(self.screen, (255, 213, 139), self.coord, 10)
        pygame.display.flip()


class Dought:
    def __init__(self, coord, screen):
        self.screen = screen
        self.coord = coord
        self.dought = load_image('dought.png')

    @staticmethod
    def sprite():
        im = load_image("dought.png", colorkey=-1)
        im1 = pygame.transform.scale(im, (30, 30))
        return im1

    def price(self):
        price = 8
        return price

    def draw(self):
        dought1 = pygame.transform.scale(self.dought, (294, 250))
        self.screen.blit(dought1, (110, 163))
        pygame.display.flip()

class Table:
    def __init__(self):
        self.boxes = []
        self.boxes.append(Box((8, 44, 135, 110), Sauce))
        self.boxes.append(Box((155, 45, 100, 110), Cheese))
        self.boxes.append(Box((9, 172, 100, 227), Dought))
        self.boxes.append(Box((263, 45, 100, 110), Pepperoni))
        self.boxes.append(Box((373, 44, 100, 110), Pepper))
        self.boxes.append(Box((480, 46, 100, 110), Mashroom))
        self.boxes.append(Box((592, 47, 100, 110), Tomato))
        self.boxes.append(Box((596, 302, 100, 110), Sausage))
        self.boxes.append(Box((701, 298, 100, 110), Pinapple))
        self.boxes.append(Box((703, 48, 100, 110), Backon))
        self.fl = True

    def draw(self, screen):
        if table.levell() == 2:
            image = load_image("table_level2.png")
            backon = load_image("backon.png", colorkey=-1)
            backon1 = pygame.transform.scale(backon, (40, 40))
            sausage = load_image("sausage.png", colorkey=-1)
            sausage1 = pygame.transform.scale(sausage, (40, 40))
            pineapple = load_image("pineapple.png", colorkey=-1)
            pineapple1 = pygame.transform.scale(pineapple, (40, 40))
        else:
            image = load_image("table_level2.png")
        image1 = pygame.transform.scale(image, (800, 470))
        screen.blit(image1, (0, 0))
        pygame.draw.rect(screen, (64, 63, 69), (0, 0, 800, 40))
        tomato = load_image("tomato.png", colorkey=-1)
        tomato1 = pygame.transform.scale(tomato, (40, 40))
        pepperony = load_image("pepperoni.png", colorkey=-1)
        pepperony1 = pygame.transform.scale(pepperony, (40, 40))
        mashroom = load_image("mashroom.png", colorkey=-1)
        mashroom1 = pygame.transform.scale(mashroom, (40, 40))
        pepper = load_image("pepper.png")
        pepper1 = pygame.transform.scale(pepper, (40, 40))
        pygame.draw.rect(screen, (166, 56, 56), pygame.Rect(670, 200, 150, 40), border_radius=40)
        font = pygame.font.SysFont('couriernew', 20, bold=True)
        text = font.render(str('Готово'), True, (255, 232, 221))
        screen.blit(text, (710, 210))
        pygame.draw.rect(screen, (166, 56, 56), pygame.Rect(620, 6, 176, 30), border_radius=40)
        text = font.render(str('Счет:'), True, (255, 232, 221))
        screen.blit(text, (625, 10))
        pygame.draw.rect(screen, (166, 56, 56), pygame.Rect(-20, 233, 159, 45), border_radius=40)
        font = pygame.font.SysFont('couriernew', 20, bold=True)
        text1 = font.render(str('В урну'), True, (255, 232, 221))
        screen.blit(text1, (3, 240))
        for i in range(100):
            if table.levell() == 2:
                screen.blit(backon1, (random.randint(705, 751), random.randint(50, 100)))
                screen.blit(sausage1, (random.randint(599, 650), random.randint(300, 355)))
                screen.blit(pineapple1, (random.randint(705, 753), random.randint(300, 355)))
            screen.blit(tomato1, (random.randint(598, 642), random.randint(50, 100)))
            screen.blit(pepperony1, (random.randint(269, 320), random.randint(50, 100)))
            screen.blit(mashroom1, (random.randint(485, 535), random.randint(60, 100)))
            screen.blit(pepper1, (random.randint(375, 430), random.randint(50, 100)))
        pygame.display.flip()

    def change_the_cursor(self, click_coord):
            if ing is not None:
                im1 = ing.sprite()
            else:
                im1 = load_image('arrow.png')
            screen.blit(im1, click_coord)
            del im1
            pygame.mouse.set_visible(False)
            pygame.display.flip()
    def where_is_a_click(self, click_coord, screen):
        image = load_image("arrow.png")
        result = None
        for box in self.boxes:
            if box.mycoord(click_coord):
                result = box.ingclass
                break
        return result

    def mycoord(self, click_coord):
        result = False
        for box in self.boxes:
            if box.mycoord(click_coord):
                result = True
                break
        return result

    def levell(self):
        levell = 1
        if pizza.score() >= 3000:
            levell = 2
        font = pygame.font.SysFont('couriernew', 20, bold=True)
        pygame.draw.rect(screen, (166, 56, 56), pygame.Rect(420, 6, 176, 30), border_radius=40)
        text = font.render(str('Уровень: ' + str(levell)), True, (255, 232, 221))
        screen.blit(text, (427, 10))
        return levell

    def for_stars(self):
        if table.levell() == 2:
            if self.fl:
                self.fl = False
                return True
            else:
                return False


class Box():
    def __init__(self, coord, ingclass):
        self.coord = coord
        self.ingclass = ingclass

    def mycoord(self, click_coord):
        return (click_coord[0] > self.coord[0] and click_coord[0] < (self.coord[0] + self.coord[2])) and (
                    click_coord[1] > self.coord[1] and click_coord[1] < (self.coord[1] + self.coord[3]))


class Pizza():
    def __init__(self):
        self.coord = (159, 176, 210, 224)
        self.ings = []
        con = sqlite3.connect("remember_game")
        cur = con.cursor()
        self.nums = cur.execute('''SELECT score FROM memory''').fetchone()[0]

    def add(self, ing):
        self.ings.append(ing)
        ing.draw()

    def score(self, pizza_cost=None):
        summa = 0
        if pizza_cost is not None:
            self.nums += pizza_cost
        font = pygame.font.SysFont('couriernew', 20, bold=True)
        text = font.render(str(self.nums), True, (255, 232, 221))
        screen.blit(text, (688, 10))
        for ing in self.ings:
            summa += ing.price()
            pygame.draw.rect(screen, (166, 56, 56), pygame.Rect(620, 6, 176, 30), border_radius=40)
            text = font.render(str('Счет:'), True, (255, 232, 221))
            screen.blit(text, (625, 10))
            text = font.render(str(round(self.nums-summa)), True, (255, 232, 221))
            screen.blit(text, (688, 10))
        con = sqlite3.connect("remember_game")
        cur = con.cursor()
        reqest = "UPDATE memory SET score = " + str(round(self.nums-summa))
        con.commit()
        cur.execute(reqest)
        return round(self.nums - summa)


    def mycoord(self, click_coord):
        return (click_coord[0] > self.coord[0] and click_coord[0] < (self.coord[0] + self.coord[2])) and (
                    click_coord[1] > self.coord[1] and click_coord[1] < (self.coord[1] + self.coord[3]))

class Particle(pygame.sprite.Sprite):
    pygame.init()
    fire1 = []
    fire = load_image("star.png")
    for scale in (5, 10, 20):
        fire1.append(pygame.transform.scale(fire, (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.screen = screen
        self.image = random.choice(self.fire1)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos

        self.gravity = 0.2

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()

def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


def open_page(screen):
    pygame.init()
    image = load_image("open page.png")
    image1 = pygame.transform.scale(image, (800, 470))
    screen.blit(image1, (0, 0))
    pygame.draw.rect(screen, (255, 239, 213), pygame.Rect(500, 50, 400, 100), border_radius=40)
    font = pygame.font.SysFont('couriernew', 40, bold=True)
    text = font.render(str('Играть'), True, (170, 30, 0))
    screen.blit(text, (575, 80))

def new_game(screen):
    image = load_image("background.jpg", colorkey=-1)
    image1 = pygame.transform.scale(image, (800, 470))
    screen.blit(image1, (0, 0))
    pygame.draw.rect(screen, (255, 239, 213), pygame.Rect(-20, 170, 150, 40), border_radius=40)
    font = pygame.font.SysFont('couriernew', 20, bold=True)
    text = font.render(str('Следующий'), True, (170, 30, 0))
    screen.blit(text, (3, 180))
    pygame.draw.rect(screen, (255, 239, 213), pygame.Rect(-20, 230, 150, 40), border_radius=40)
    text1 = font.render(str('Готовить'), True, (170, 30, 0))
    screen.blit(text1, (3, 240))
    pygame.draw.rect(screen, (166, 56, 56), pygame.Rect(620, 6, 176, 30), border_radius=40)
    text = font.render(str('Счет:'), True, (255, 232, 221))
    screen.blit(text, (625, 10))

def character_changer(screen):
    new_game(screen)
    con = sqlite3.connect("customer_phrases")
    cur = con.cursor()
    character = cur.execute('''SELECT name FROM characters ORDER BY random() LIMIT 1''').fetchone()
    del_color = "SELECT color_to_del FROM characters WHERE name = '" + character[0] + "'"
    res_color = cur.execute(del_color).fetchone()
    res_color = res_color[0].split(',')
    res1_color = (int(res_color[0][1:]), int(res_color[1]), int(res_color[2][:2]))
    pers = load_image(character[0])
    pers1 = pygame.transform.scale(pers, (200, 250))
    screen.blit(pers1, (140, 125))
    if table.levell() == 2:
        phrase = cur.execute('''SELECT phrase FROM phrases ORDER BY random() LIMIT 1''').fetchone()
    else:
        phrase = cur.execute('''SELECT phrase FROM phrases WHERE level = 1 ORDER BY random() LIMIT 1''').fetchone()
    pr = "SELECT price FROM phrases WHERE phrase = '" + phrase[0] + "'"
    price = cur.execute(pr).fetchone()
    if len(phrase[0]) * 10 > 430:
        font_surf = pygame.font.SysFont('couriernew', 15, bold=True)
    else:
        font_surf = pygame.font.SysFont('couriernew', 20, bold=True)
    font_surf = font_surf.render(str(phrase[0]), True, (170, 30, 0))
    dest_surf = screen
    dest_rect = pygame.draw.rect(screen, (255, 239, 213), pygame.Rect(310, 105, 480, 75), border_radius=40)
    dest_surf.blit(font_surf, font_surf.get_rect(center=dest_rect.center))
    pizza.score()
    table.levell()
    return price


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 470))
    running = True
    open_page(screen)
    pygame.display.flip()
    table = Table()
    pizza = Pizza()
    ing = None
    flag = False
    play_flag = False
    table.levell()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    for i in range(20):
        create_particles((random.randint(0, 800), random.randint(0, 470)))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x = event.pos[0]
                pos_y = event.pos[1]
                if flag:
                    if table.mycoord((pos_x, pos_y)):
                        ing = table.where_is_a_click((pos_x, pos_y), screen)
                        table.levell()
                    elif ing is not None:
                        if pizza.mycoord((pos_x, pos_y)):
                            pizza.add(ing((pos_x, pos_y), screen))
                            pizza.score()
                            table.levell()
                            pygame.display.flip()
                if play_flag is False:
                    if (pos_x >= 550 and pos_x <= 700) and (pos_y >= 59 and pos_y <= 153 ):
                        new_game(screen)
                        pizza.score()
                        table.levell()
                        pygame.display.flip()
                    if (pos_x >= 0 and pos_x <= 170) and (pos_y >= 170 and pos_y <= 210 ):
                        character_changer(screen)
                        pygame.display.flip()
                if (pos_x >= 676 and pos_x <= 790) and (pos_y >= 200 and pos_y <= 236 ):
                    new_game(screen)
                    play_flag = False
                    flag = False
                    pizza_coast = character_changer(screen)[0]
                    pizza.score(pizza_coast)
                    table.levell()
                    pizza.score()
                    pygame.display.flip()
                if (pos_x >= 0 and pos_x <= 170) and (pos_y >= 220 and pos_y <= 270 ):
                    table.draw(screen)
                    pizza.score()
                    table.levell()
                    play_flag = True
                    flag = True
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                pos_x = event.pos[0]
                pos_y = event.pos[1]
                if ing is not None:
                    if pizza.mycoord((pos_x, pos_y)):
                        pizza.add(ing((pos_x, pos_y), screen))
        if table.for_stars():
            while len(all_sprites) > 0:
                all_sprites.update()
                new_game(screen)
                all_sprites.draw(screen)
                pygame.display.flip()
                clock.tick(50)
