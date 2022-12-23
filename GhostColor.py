"""
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
OBJECT-ORIENTED PROGRAMMINGFUNDAMENTALS
"""


import random
class Ghost(object):
    def __init__(self):
        colorlist = ("white", "yellow", "purple", "red")
        self.color = random.choice(colorlist)
