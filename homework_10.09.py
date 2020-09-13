import os
import re


class Organizer:

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def run(self):
        content = os.listdir(self.dir_path)
        for i in content:
            if re.compile(r'\.(\w+)$').search(i):
                new_dir = re.compile(r'\.(\w+)$').search(i).group(1) + '_files'
                new_dir_path = os.path.join(self.dir_path, new_dir)
                if new_dir not in content:
                    os.mkdir(new_dir_path)
                os.rename(os.path.join(self.dir_path, i), os.path.join(new_dir_path, i))
            content = os.listdir(self.dir_path)


# p = '/home/yurii/Downloads'
# org = Organizer(p)
# org.run()
