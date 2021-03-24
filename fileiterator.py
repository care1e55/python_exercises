import os 

files_dir = 'books'

def files_lines_iterator(files_dir):
    for file in os.listdir(files_dir):
        for line in open(os.path.join(files_dir, file)):
            yield line


if __name__ == '__main__':
    for line in files_lines_iterator(files_dir):
        print(line)
