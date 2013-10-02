import os
from mojibake.settings import FLATPAGES_ROOT

posts = os.path.join(FLATPAGES_ROOT, 'posts')
categories = {}
dates = {}
for i in os.listdir(posts):
    if os.path.splitext(i)[1].lower() == '.md':
        with open(os.path.join(posts, i), 'r') as j:
            for line in j:
                if 'category: ' in line:
                    # Remove the category: and the \n
                    found_line = line[10:][:-1]
                    for k in found_line.split(', '):
                        #cat = k.replace('\n', '')
                        if k in categories.keys():
                            categories[k].append('posts/{}'.format(i[:-3]))
                        else:
                            categories[k] = ['posts/{}'.format(i[:-3])]
                    break

print categories
