#출력 모듈
#   -기본 메시지 : print_form_msg
#   -경고 메시지 : print_warning_msg
#   -선 메시지 : print_line

def print_form_msg(msg):
    print("     ===     %s     ===     " % msg)

def print_warning_msg(msg):
    print("      ⁕      %s      ⁕      " % msg)

def print_line():
    print("="*100)