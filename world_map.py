#!/usr/bin/env python3

"""
2 classes :
Carte : store game map and hide it from the character
Kirk : a character that cna move on Carte.carte
Ouais c'est pas clair, tant pis
"""

class Carte:

    def __init__(self, carte, kirk):
        self.carte = [list(ligne) for ligne in carte]
        self.size = len(self.carte[0]), len(self.carte)
        #print('len : ',len(carte))
        self.revealed = [['?' for c in ligne] for ligne in carte]
        self.kirk = kirk

    def discover(self, kc, kr):
        x0 = kc-2 if (kc-2) > 0 else 0
        x1 = kc+3 if (kc+2) < self.size[0] else self.size[0]
        y0 = kr-2 if (kr-2) > 0 else 0
        y1 = kr+3 if (kr+2) < self.size[1] else self.size[1]
        #print(x0,x1,y0,y1)
        for x in range(x0, x1):
            for y in range(y0, y1):
                self.revealed[y][x] = self.carte[y][x]

    def get_carte(self):
        self.discover(*self.kirk.pos)
        for row in self.revealed:
            yield ''.join(row)

    def diplay_whole_world(self):
        for row in self.carte:
            yield ''.join(row)

    def move_kirk(self, direction):
        old_pos = self.kirk.pos
        self.kirk.move(direction)
        new_pos = self.kirk.pos
        #print(f'Kirk move toward {new_pos} cell')

        self.carte[old_pos[1]][old_pos[0]] = '.'
        self.carte[new_pos[1]][new_pos[0]] = 'T'


class Kirk:

    def __init__(self, carte):
        for j, ligne in enumerate(carte):
            for i, c in enumerate(ligne):
                if c == 'T':
                    self._pos = i, j

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, *pos):
        self._pos = pos

    def move(self, d):
        if d == "UP":
            self._pos = self._pos[0], self._pos[1]-1
        if d == "DOWN":
            self._pos = self._pos[0], self._pos[1]+1
        if d == "LEFT":
            self._pos = self._pos[0]-1, self._pos[1]
        if d == "RIGHT":
            self._pos = self._pos[0]+1, self._pos[1]




