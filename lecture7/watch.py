import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if extract := re.search(r'"(https?://)(?:www\.)?youtube\.com/embed/(.+)"',s,re.IGNORECASE):
        return f"{extract.group(1)}youtu.be/{extract.group(2)}"


if __name__ == "__main__":
    main()