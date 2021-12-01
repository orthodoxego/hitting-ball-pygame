import pygame

class FontSurface:

    def __init__(self):
        self.__font_help = pygame.font.Font("font\kelly.ttf", 20)
        self.__font_score = pygame.font.Font("font\kelly.ttf", 38)

        self.help_surface_text = self.__font_help.render("Для ускорения шара отбейте его площадкой (зажмите ЛКМ). P - Пауза", True, (150, 150, 175))

    def getSurfaceText(self, text, color):
        """Вернёт строку с текстом для отображения, шрифт 38."""
        return self.__font_score.render(text, True, color)

    def getHelpSurfaceText(self, text, color):
        """Вернёт строку с текстом для отображения, шрифт 20."""
        return self.__font_help.render(text, True, color)




