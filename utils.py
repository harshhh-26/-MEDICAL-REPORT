"""
utils.py - Formatting Helpers & Safe Input Validators
"""
import config

def print_header():
    border = "+" + "-" * 60 + "+"
    print(border)
    print(f"| {config.PROJECT_TITLE.center(58)} |")
    print(border)
    print(f"| Author       : {config.AUTHOR:<43} |")
    print(f"| Register No. : {config.REGISTER_NO:<43} |")
    print(f"| Course Code  : {config.COURSE_CODE:<43} |")
    print(f"| Course Title : {config.COURSE_TITLE:<43} |")
    print(border)
    print()

def get_valid_input(prompt: str, target_type=str, min_val=None, max_val=None):
    while True:
        try:
            val = target_type(input(prompt).strip())
            if min_val is not None and val < min_val:
                print(f"  [!] Value must be at least {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"  [!] Value must not exceed {max_val}.")
                continue
            return val
        except ValueError:
            print(f"  [!] Invalid input type. Please enter a valid {target_type.__name__}.")