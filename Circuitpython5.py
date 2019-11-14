#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# Circuit python 5


import ugame
import stage

import constants


def game_scene():
    # this function is a scene

    # an image bank of CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_X, \n
                            constants.SCREEN_Y)

    # the list of the sprites that will be on the device
    sprites = []

    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / \n
                        2 - constants.SPRITE_SIZE/),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE + \n
                            constants.SPRITE_SIZE / 2))
    sprites.append(ship)  # insert at the top of sprite list

    # create a stage for the background to show up
    # setting the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # setting the layers to show them in order
    game.layers = sprites + [background]
    # rendering the background and the locations of the sprites
    game.render_block()

    # repeat forever game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)

        # update game logic
        # move ship right
        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        # move ship right
        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
