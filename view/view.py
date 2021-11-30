import pygame

class View:

    def player_draw(self, pygame, scene, p):
        scene.blit(p.player.skin, (p.player.x,
                                   p.player.y + int(p.player.energy_y)))
