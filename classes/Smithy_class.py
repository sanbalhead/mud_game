#강화소 클래스
#   -이름 : name

#검 강화하러 가기
#상점 가기
#아이템창 가기
#저장하기
#나가기


class Smithy:
    def __init__(self, name):
        self.name = name

    def print_menu(self):
        print("""
        1. Upgrading sword
        2. Shop
        3. Item
        4. Save the report
        5. Quit
        """)