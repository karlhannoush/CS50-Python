from datetime import date
import sys
from num2words import num2words

def main():
    birth = get_birth()
    delta_days = (date.today()-birth).days*24*60
    print(string_number(delta_days))

def get_birth():
    birth_date = input("Your date of birth: ")
    try:
        date_list = birth_date.split("-")
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])
        return date(year,month,day)
    except ValueError,IndexError:
        sys.exit("Invalid format")
        
    
def string_number(number):
    string = num2words(number)
    if "and " in string:
        return string.replace("and ","")
    else:
        return string
    
if __name__ == "__main__":
    main()