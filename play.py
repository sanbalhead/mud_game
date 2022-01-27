#play 파일

#캐릭터 : player
#강화소 : smithy
#깨짐 방지권 : break_proof_ticket
#나의 돈 : my_money


from cgitb import text
import random
from re import S
from tkinter import W
from classes.person_class import *
from classes.Smithy_class import *
from classes.sword_class import *
from module.print_module import *

player = Person('', '')
smithy = Smithy('')
break_proof_ticket = 0
my_money = 1000000


def start_game():
    repeat()

#게임 메뉴
#   -검 강화하러 가기
#   -상점 가기
#   -아이템창 가기
#   -저장하기
#   -나가기

def repeat():
    where = 0
    while True:
        if where == 0:
            print('''
        == Welcome %s == ''' % player.name)

            where = 1

        elif where == 1:
            smithy.print_menu()
            smithy_op = int(input("Choose a menu: "))

            if smithy_op == 1:
                print_form_msg("Upgrading sword")
                start_upgrading_sword()
                
            
            if smithy_op == 2:
                print_form_msg("Shop")
                start_shop()

            if smithy_op == 3:
                print_form_msg("Item")
                start_item()

            
            if smithy_op == 4:
                f = open('./save_data.txt', 'w')
                f.write("save")
                f.close()
                break

            if smithy_op == 5:
                print_form_msg("Quit")
                break

            else:
                print_warning_msg("Check the menu again.")

#검 강화하기
#   -강화를 할때마다 확률이 0.95%가 된다.
#   -팔기
#   -만약 깨짐 방지권이 있다면 실패 할 때 사용됨

#검 이름 : Sword
#검 레벨 : sword_lvl
#강화 금액 : basic_price
#검 판매 금액 : sword_price
#확률 : ras

def start_upgrading_sword():
    global my_money
    sword_lvl = 0
    sword_price = 100
    Sword = sword_name.get(sword_lvl)
    basic_price = 300
    ras = 1.0
    


    print_line()
    print('''
    Stop when you type sell
    choose "upgrade" or "sell"
    Sword is %d level.
    Sword name is %s
    ''' % (sword_lvl, Sword))
    print_line()

    ch = input()
    while True:


        if ch == 'sell':
            my_money = my_money + sword_price
            print("Sword was lvel %d." % sword_lvl)
            print("It sold for %d." % sword_price)
            print("You have %d." % my_money)
            print("Sword name is '%s'" % Sword)
            start_game()

        rate = random.random()
        
        if ch == 'upgrade':
            if my_money < basic_price:
                print_line()
                print_warning_msg("You don't have enough money")
                print_line()
                break


            if rate < ras:
                sword_lvl = sword_lvl + 1
                basic_price = basic_price * 1.5
                my_money = my_money - basic_price
                sword_price = sword_price * 1.7
                Sword = sword_name.get(sword_lvl)

                print_line()
                print('success')
                ras = ras * 0.95
                print("Sword is %d levels." % sword_lvl)
                print("Sword name is '%s'" % Sword)
                print("Success chance is %fpercent." % ras)
                print("Upgrading amount is %d." % basic_price)
                print("Sale price is %d." % sword_price)
                print("Current holding amount is %d." % my_money)
                print_line()
            
        
        elif rate > ras:
            if break_proof_ticket > 1:
                break_proof_ticket = break_proof_ticket - 1
                print_line()
                print_form_msg("You used break proof ticket")
                print_line()
                pass
            else:
                print_line()
                print('fail')
                print_line()
                start_game()
        
        elif rate == 0:
            start_game()

        
        ch = input()

#상점
#   -깨짐 방지권 : 10000원

def start_shop():
    while True:
        print_line()
        print('''
1. break-proof ticket --- price : 10000
''')
        print_line()

        print_line()
        stu = input('''
Would you like to buy something
if you type "out" go to the Start_game
''')    
        print_line()
        
        
        if stu == 1:
            if my_money > 1000000:
                break_proof_ticket = break_proof_ticket + 1
                print("Your break proof ticket is %d" % break_proof_ticket)

            elif my_money < 10000000:
                print_line()
                print_warning_msg("You don't have enough money.")
                print_line()
        

        elif stu == 'out':
            break

#아이템
#   -돈과 깨짐 방지권이 얼마나 있는지 확인

def start_item():
    while True:
        print_line()
        print('''
        Your money : %d
        Your break proof ticket : %d 
        ''' % (my_money, break_proof_ticket))
        print_line()
        break
    
#메인 메뉴
#   -게임시작
#   -불러오기
#   -게임종료

#이름 : name
#성 : sex
#강화소 이름 : smithy_name


if __name__ == "__main__":
    print_line()
    print('''
⁅ Welcome to Upgrading Sword ⁆
''')
    print_line()

    End = False
    while True:
        print_line()
        print("""
      1. starting game
      2. load
      3. game over
        """)
        print_line()

        op = int(input('Enter the menu: '))
        if op == 1:
            name = ""
            while True:
                name = input('Enter the name: ')
                if len(name) > 0:
                    break
            
            sex = ""
            while True:
                print("""
        1. man         2. woman
                """)
                sex = int(input('Enter your gender: '))
                if sex == 1:
                    sex = 'man'
                    break
                if sex == 2:
                    sex = 'woman'
                    break

            smithy_name = ''
            while True:
                smithy_name = input('Enter the smithy name: ')
                if len(smithy_name) > 0:
                    break

            player = Person(name, sex)
            smithy = Smithy(smithy_name)

            from load import *

            print_form_msg("Go to %s."% smithy.name)
            start_game()            

        elif op == 2:
            try:
                f = open("./save_data.txt", "r")
            except FileNotFoundError as e:
                print_warning_msg("No data saved.")

        elif op == 3:
            print_form_msg('Game over')
            End = True
            break
        
        else:
            print_warning_msg('Wrong number')