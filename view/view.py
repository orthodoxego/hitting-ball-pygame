import pygame

class View:

    def player_draw(self, scene, player):
        scene.blit(player.player.texture, (player.x,
                                           player.y + int(player.energy_y)))

    def ball_draw(self, scene, ball):
        if ball.y >= 0:
            scene.blit(ball.ball.texture, (ball.x, ball.y))
        else:
            scene.blit(ball.ball.ghost_texture, (ball.x, 0))

    def nlo_draw(self, scene, nlo):
        scene.blit(nlo.texture, (nlo.x, nlo.y))

    def text_draw(self, scene, surface, x, y):
        scene.blit(surface, (x, y))

    def stars_draw(self, scene, stars):
        for star in stars:
            pygame.draw.circle(scene,
                               star[4],
                               (star[0], star[1]),
                               1,
                               1)

