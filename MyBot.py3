#!/usr/bin/env python
from ants import *
from random import shuffle

# define a class with a do_turn method
# the Ants.run method will parse and update bot input
# it will also run the do_turn method for us
class MyBot: 
    def __init__(self):
        # define class level variables, will be remembered between turns
        pass
    
    # do_setup is run once at the start of the game
    # after the bot has received the game settings
    # the ants class is created and setup by the Ants.run method
    def do_setup(self, ants):
        # initialize data structures after learning the game settings
        pass
    
    # do turn is run once per turn
    # the ants class has the game state and is updated by the Ants.run method
    # it also has several helper methods to use
    def do_turn(self, ants):
        def do_turn(self, ants):
        destinations = []
        for a_row, a_col in ants.my_ants():
            targets = ants.food() + [(row, col) for (row, col), owner in ants.enemy_ants()]
            # find closest food or enemy ant
            closest_target = None
            closest_distance = 999999
            for t_row, t_col in targets:
                dist = ants.distance(a_row, a_col, t_row, t_col)
                if dist < closest_distance:
                    closest_distance = dist
                    closest_target = (t_row, t_col)
            if closest_target == None:
                # no target found, mark ant as not moving so we don't run into it
                destinations.append((a_row, a_col))
                continue
            directions = ants.direction(a_row, a_col, closest_target[0], closest_target[1])
            shuffle(directions)
            for direction in directions:
                n_row, n_col = ants.destination(a_row, a_col, direction)
                if ants.unoccupied(n_row, n_col) and not (n_row, n_col) in destinations:
                    destinations.append((n_row, n_col))
                    ants.issue_order((a_row, a_col, direction))
                    break
            else:
                # mark ant as not moving so we don't run into it
                destinations.append((a_row, a_col))
            
if __name__ == '__main__':
    # psyco will speed up python a little, but is not needed
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    try:
        # if run is passed a class with a do_turn method, it will do the work
        # this is not needed, in which case you will need to write your own
        # parsing function and your own game state class
        Ants.run(MyBot())
    except KeyboardInterrupt:
        print('ctrl-c, leaving ...')
