import os
import re

os.system('clear')
print("=============\n SCRAPCHAN\n=============\n\n")

url = input("Enter the thread URL: ")
print(url)
if not os.path.exists('output'):
    os.mkdir('output')
print("Which filetype do you want to retrieve ?\n")
print("1- Video (mp4,webm)\n2- Gif\n3- Image (jpg,png)\n4- All\n\n")
choice = input("Format: ")
choiceint = int(choice)
if (choiceint == 1):
    os.system('curl ' + url + ' 2>&1 | grep -o -E \'href=\"//([^\"#]+)webm\\|mp4\"\' > links.temp');
if (choiceint == 2):
    os.system('curl ' + url + ' 2>&1 | grep -o -E \'href=\"//([^\"#]+)gif\"\' > links.temp');
if (choiceint == 3):
    os.system('curl ' + url + ' 2>&1 | grep -o -E \'href=\"//([^\"#]+)jpg\\|png\"\' > links.temp');
if (choiceint == 4):
    os.system('curl ' + url + ' 2>&1 | grep -o -E \'href=\"//([^\"#]+)jpg\"\' > links.temp');

for line in open("links.temp"):
    line = re.sub('"|^\w+="', "https:", line)
    line = re.sub('https:$', "",line)
    print(line)
    os.system('cd output/ && wget -N ' + line)
os.remove("links.temp")





