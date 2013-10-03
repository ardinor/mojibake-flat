import os
from mojibake.settings import FLATPAGES_ROOT

def build_gen_files():

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

    file_dir = os.path.dirname(os.path.abspath(__file__))
    gen_dir = os.path.join(file_dir, 'mojibake/gen')

    if not os.path.exists(gen_dir):
        os.mkdir(gen_dir)

    with open(os.path.join(gen_dir, 'categories.md'), 'w+') as f:
        f.write(str(categories))

if __name__ == '__main__':
    build_gen_files()
