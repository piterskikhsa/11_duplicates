import pprint
import sys
import os
from collections import defaultdict

defdict = defaultdict(dict)

def get_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size in defdict[file]:
                defdict[file][file_size].append(file_path)
            else:
                defdict[file][file_size] = [file_path]
    return defdict

def get_duplicates(files_dict):
    duplicates_files = []
    for file_name, file_data in files_dict.items():
        for file_size, file_path in file_data.items():
            if len(file_path)> 1:
                print(file_name, file_path, file_size)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input('Укажите путь к коталогу: ')
    all_files = get_files(file_path)
    get_duplicates(all_files)