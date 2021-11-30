import pygame
from random import randint
from setup.setup import Setup
from game_classes.goldbox import GoldBox

class GoldBoxEngine:

    def __init__(self, texture_box):
        self.boxes = []
        self.count_boxes = Setup.start_count_boxes
        self.texture_box = texture_box

    def append_box(self):
        self.boxes.append(GoldBox(Setup.screen_width + randint(0, int(Setup.screen_width)),
                                  randint(0, int(Setup.screen_height * 0.65)),
                                  self.texture_box, randint(int(Setup.screen_width * 0.1),
                                                            int(Setup.screen_width * 0.25)) * -1,
                                  0))

    def create_boxes(self):
        self.boxes.clear()

        for i in range(self.count_boxes):
            self.append_box()

    def act(self, delta):
        for goldbox in self.boxes:
            goldbox.act(delta)

        for i in range(len(self.boxes) - 1, -1, -1):
            if self.boxes[i].x + self.boxes[i].width < 0:
                self.boxes.remove(self.boxes[i])

        if len(self.boxes) == 0:
            self.create_boxes()
