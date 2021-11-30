import pygame

class View:

    def player_draw(self, scene, player):
        scene.blit(player.player.skin, (player.x,
                                   player.y + int(player.energy_y)))

    def ball_draw(self, scene, ball):
        scene.blit(ball.ball.skin, (ball.x, ball.y))
