import pygame

class View:

    def player_draw(self, scene, p):
        scene.blit(p.player.skin, (p.player.x,
                                   p.player.y + int(p.player.energy_y)))

    def ball_draw(self, scene, b):
        scene.blit(b.ball.skin, (b.ball.x, b.ball.y))
