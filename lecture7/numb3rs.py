import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches :=  re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip):
        number = True
        for i in range(1,5):
            if not 0 <= int(matches.group(i)) <= 255:
                number = False
        return number
    else:
        return False

if __name__ == "__main__":
    main()