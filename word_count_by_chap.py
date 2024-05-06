import os
import jieba
import csv

character_dict = 'D:\\JupyterSpace\\AI&python\\text_cut\\射雕英雄传人物.txt'
jieba.load_userdict(character_dict)
jieba.load_userdict("D:\\JupyterSpace\\AI&python\\text_cut\\小作业3-4-射雕英雄传词典.txt")

dir_path = "D:\\JupyterSpace\\AI&python\\text_cut\\射雕英雄传"

all_row = []  # list to hold all the rows


with open(character_dict, encoding='utf-8') as cd:
    name_dict = cd.read()

name_dict = name_dict.split('\n')

# iterate over each file in the dir
for filename in os.listdir(dir_path):
     # open and read the file
    with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as file:
         contents = file.read()
        
    cut_contents = jieba.lcut(contents)

    count = {}

    for word in cut_contents:
        count[word] = count.get(word,0) + 1
    
    # substract all the dict of names and counts
    # insert into the list with their filenames
    items = dict(list(count.items()))
    line = [filename]
  
    for name in name_dict:
        if name in contents and name in cut_contents:
            line.append(items[name])
        else:
            line.append(0)
    all_row.append(line)

headers = [""] + name_dict
# use "newline" to delete the blank row
with open('D:\\JupyterSpace\\AI&python\\text_cut\\word_count.csv', 'w', newline="") as ntable:
    ntable = csv.writer(ntable)
    ntable.writerow(headers)
    ntable.writerows(all_row)


       
       

        
