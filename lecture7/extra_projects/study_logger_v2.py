import re
import csv

def main():
    extract = lst_extract(input())
    store_file(extract)

def lst_extract(s):
    new_str = re.sub(r"^(?:Today +)?I +studied[:\s]?","",s,flags = re.IGNORECASE)
    pattern = r"([a-z0-9& ]+?)\s+for\s+(?:(\d+)\s*h(?:our(?:s)?)?)?\s*(?:(\d+)\s*m(?:inute(?:s)?)?)?(?:, |$|and )"

    return_list = []

    for loop in re.finditer(pattern,new_str,re.IGNORECASE):
        subject = loop.group(1)
        duration = 0
        if loop.group(2):
            duration += int(loop.group(2))*60
        if loop.group(3):
            duration += int(loop.group(3))
        
        return_list.append({"subject":subject.title().strip(),"duration":duration})
    return return_list
                        
            
            
def store_file(lst):
    with open("study_logger_v2.csv","w",newline = "") as file:
        writer = csv.DictWriter(file,fieldnames = ["subject","duration"])
        writer.writeheader()
        for item in lst:
            writer.writerow({"subject":item["subject"],"duration":item["duration"]})


if __name__ == "__main__":
    main()

