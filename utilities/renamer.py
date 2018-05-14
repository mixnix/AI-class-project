import os, re

def convertToPng(relativePath):
    absolute_path = os.path.abspath(relativePath)
    listed_filenames = os.listdir(relativePath)
    pattern = re.compile(r"^(.*?)\..*") # matches string until first dot
    for filename in listed_filenames:
        before_name_path = os.path.join(absolute_path,filename)
        name_without_extension = re.match(pattern, filename)
        after_name_path = os.path.join(absolute_path,name_without_extension.group(1)+".png")
        os.rename(before_name_path,after_name_path)


def renamingScript():
    absolute_path = os.path.abspath("../res/readyTemplates")
    listed_filenames = os.listdir("../res/readyTemplates")
    count = 1
    for filename in listed_filenames:
        before_name = os.path.join(absolute_path,filename)
        after_name = os.path.join(absolute_path,str(count)+".jpg")
        os.rename(before_name, after_name)
        count += 1

if __name__ == "__main__":
    convertToPng("../res/readyTemplates/Monsters/Goblin")
