import pygame


class Text:

    def __init__(self):
        self.__font_help = pygame.font.Font("font\kelly.ttf", 20)
        self.__font_score = pygame.font.Font("font\kelly.ttf", 38)
        self.help_surface_text = self.__font_help.render("Для ускорения шара отбейте его площадкой (зажмите ЛКМ). P - Пауза", True, (150, 150, 175))

    def getStringIntText(self, s, value, color):
        """Вернёт строку с текстом и очками для отображения."""
        return self.__font_score.render(s + str(value), True, color)




