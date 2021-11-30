from setup.setup import Setup

class Controller:

    def __init__(self, player):
        self.player = player
        self.lkm_pressed = False

    def act(self, pygame, delta):

        # Реакция площадки игрока на зажатую
        # ЛКМ мыши и отпущенную.
        if self.lkm_pressed:
            self.player.mouse_button1_pressed(delta)
        else:
            self.player.mouse_button1_unpressed(delta)

        # Расчёт движения за курсором
        # if pygame.mouse.get_focused():
        self.__check_mouse_cursor(pygame, delta)

        # Проверяет события мыши и клавиатуры
        return self.__check_events(pygame, delta)

    def __check_events(self, pygame, delta):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.lkm_pressed = True
                return True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.lkm_pressed = False
                return True

            # Закрыли окно
            elif event.type == pygame.QUIT:
                return False

            # Клавиши
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_LEFT:
                    self.player.move_left(delta, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right(delta, Setup.screen_width)
                elif event.key == pygame.K_UP:
                    print("ВВЕРХ")
                elif event.key == pygame.K_DOWN:
                    print("ВНИЗ")

        return True

    def __check_mouse_cursor(self, pygame, delta):
        """Проверяет и вызывает интерфейс для изменения координат площадки
        игрока в зависимости от положения курсора мыши."""
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        if x < self.player.x:
            self.player.move_left(delta, x)
        if x > self.player.x + self.player.width:
            self.player.move_right(delta, x)
