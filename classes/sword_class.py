#검 클래스
#   -이름 : name
#   -가격 : price
#   -검 이름 : sword_name

class Sword:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_sword_name(self):
        print('이 검의 이름은 %s 입니다.' % self.name)
