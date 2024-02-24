from pathlib import Path

def get_cats_info(path):
    try:
        with open(path) as file:
            file_text = file.read()
            cats_info = []
            for line in file_text.split("\n"):
                line = line.split(",")
                cats_info.append({"id":line[0], "name":line[1], "age":line[2]})
            return(cats_info)
    except:
        print(" The file does not exist")





cats_info = get_cats_info("c:/Users/admin/Desktop/PYTHON/M_4/hw_4/data_cats.txt")
print(cats_info)