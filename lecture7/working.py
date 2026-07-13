import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d\d?)(?::(\d\d))? (AM|PM) to (\d\d?)(?::(\d\d))? (AM|PM)$",s):
        if not (1 <= int(matches.group(1)) <= 12 and 1 <= int(matches.group(4)) <= 12):
            raise ValueError 
        elif matches.group(2) != None and not 0 <=  int(matches.group(2)) <= 59:
            raise ValueError
        elif matches.group(5) != None and not 0 <=  int(matches.group(5)) <= 59:
            raise ValueError
        else:
            if matches.group(3) == "AM":
                if matches.group(1) == "12":
                    hour1 = "00"
                else:
                    hour1 = matches.group(1)
            else:
                if matches.group(1) == "12":
                    hour1 = matches.group(1)
                else:
                    hour1 = int(matches.group(1)) + 12
            if matches.group(6) == "AM":
                if matches.group(4) == "12":
                    hour2 = "00"
                else:
                    hour2 = matches.group(4)
            else:
                if matches.group(4) == "12":
                    hour2 = matches.group(4)
                else:
                    hour2 = int(matches.group(4)) + 12
            if matches.group(2) != None:
                minute1 = matches.group(2)
            else:
                minute1 = "00"
            if matches.group(5) != None:
                minute2 = matches.group(5)
            else:
                minute2 = "00"

            return f"{hour1}:{minute1} to {hour2}:{minute2}"
            
    else:
        raise ValueError





if __name__ == "__main__":
    main()