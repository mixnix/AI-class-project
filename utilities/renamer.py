import os

if __name__ == "__main__":
    absolute_path = os.path.abspath("../res/readyTemplates")
    listed_filenames = os.listdir("../res/readyTemplates")
    count = 1
    for filename in listed_filenames:
        before_name = os.path.join(absolute_path,filename)
        after_name = os.path.join(absolute_path,str(count)+".jpg")
        os.rename(before_name, after_name)
        count += 1
