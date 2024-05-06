import os

"""
    This module handles the opening of files and reading them

    Args:
        open_file(filename : file ): Opens the given file and keeps it on read mode
"""

def open_file(filename):
    path = os.getcwd() + '/' + filename
    with open(path, 'r') as f:
        l = f.readlines()
        f.close()
    return l

# if __name__ == '__main__':
#     print(open_file('images.txt'))
