import os
import re

if not os.path.exists('output'):
    os.mkdir('output')
os.system('curl https://boards.4chan.org/s/thread/21053159 2>&1 | grep -o -E \'href=\"//([^\"#]+)jpg\"\' > links.temp');

for line in open("links.temp"):
    line = re.sub('"|^\w+="', "https:", line)
    line = re.sub('https:$', "",line)
    print(line)
    os.system('cd output/ && wget -N ' + line)






