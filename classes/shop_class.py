#상점 클래스
#   -이름 : name

from cgi import print_form
from classes.item_class import *
from classes.sword_class import *
from module.print_module import *

class shop:
    def __init__(self, name):
        self.name = name
