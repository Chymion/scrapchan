# -*- coding: utf-8 -*-
import os
import re
import sys
MIN_PYTHON = (3, 0)
if (sys.version_info < MIN_PYTHON):
    sys.exit("Sorry, Python %s.%s or later is required..." % MIN_PYTHON)

os.system('clear')
print("=============\n🍀SCRAPCHAN🍀\n=============\n")

url = input("Enter the thread URL: ")
if not os.path.exists('output'):
    os.mkdir('output')
print("Which filetype do you want to retrieve ?\n")
print("1- Video (mp4,webm)\n2- Gif\n3- Image (jpg,png)\n4- All\n\n")
choice = input("Format: ")
choiceint = int(choice)
if (choiceint == 1):
    os.system('curl ' + url + ' 2>&1 | grep -Eo \'href="[^\"]+"\' | grep \'webm\|mp4\' > links.temp');
if (choiceint == 2):
    os.system('curl ' + url + ' 2>&1 | grep -Eo \'href="[^\"]+"\' | grep \'gif\' > links.temp');
if (choiceint == 3):
    os.system('curl ' + url + ' 2>&1 | grep -Eo \'href="[^\"]+"\' | grep \'jpg\|png\' > links.temp');
if (choiceint == 4):
    os.system('curl ' + url + ' 2>&1 | grep -Eo \'href="[^\"]+"\' | grep \'jpg\|png\|webm\|mp4\|gif\' > links.temp');
count = 0
for line in open("links.temp"):
    line = re.sub('"|^\w+="', "https:", line)
    line = re.sub('https:$', "",line)
    matches=[".jpg", ".png", ".mp4", ".webm", ".gif"]
    if any(x in line for x in matches):
        count+=1
if ((count % 2) == 0):
    count /= 2
else:
    count += 1
print("There are " + str(int(count)) + " elements to be downloaded")
choiceCount = input("Continue ? [y/n] : ")
if (str(choiceCount) == 'y' or str(choiceCount) == 'Y'):
    for line in open("links.temp"):
        line = re.sub('"|^\w+="', "https:", line)
        line = re.sub('https:$', "",line)
        matches=[".jpg", ".png", ".mp4", ".webm", ".gif"]
        if any(x in line for x in matches):
            os.system('cd output/ && wget -N ' + line)
else:
    os.remove("links.temp")
    quit()
#else:
#    tempChoice = int(choiceCount)
#    tempChoice+=1
#    tempCount=0
#    os.system('touch output/saved.temp')
#    for line in open("links.temp"):
#        if (int(tempCount) > int(tempChoice)):
#            if not (tempCount % 2 == 0):
#                os.remove("links.temp")
               # os.remove("output/saved.temp")
#                quit()
#        line = re.sub('"|^\w+="', "https:", line)
#        line = re.sub('https:$', "",line)
#        matches=[".jpg", ".png", ".mp4", ".webm", ".gif"]
#        if any(x in line for x in matches):
#            os.system('cd output/ && wget -N ' + line + ' >> saved.temp')
#            for lined in open("output/saved.temp"):
#                tempCount+=1
#            print("TESSSSSSSSSSST: "+ str(tempCount))
os.remove("links.temp")

