import pprint
import sys
import os
from collections import defaultdict


def get_files(path):
    defdict = defaultdict(dict)
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
    duplicates = {}
    for file_name, file_data in files_dict.items():
        for file_size, file_path in file_data.items():
            if len(file_path) >= 2:
                duplicates[file_name] = file_data
    return duplicates


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input('Укажите путь к каталогу: ')
    if os.path.exists(file_path):
        file_path = os.path.abspath(file_path)
        all_files = get_files(file_path)
        all_duplicates = get_duplicates(all_files)
        if all_duplicates:
            for duplicates_name, duplicates_data in all_duplicates.items():
                for file_size, file_path in duplicates_data.items():
                    print("""
Имя найденных дубликатов: {name}
Размер: {size} байт
Количество найденных дубликатов: {quantity}
Пути к файлам: {file_path}""".format(name=duplicates_name, size=file_size,
                                                     quantity=len(duplicates_data[file_size]),
                                                     file_path=file_path))
        else:
            print('Ура! Дублитов не обнаруженно')
    else:
        print(
            'Внимание: - Указанной папки не существует, проверьте правильность введенных данных, и попробуйте еще раз.')
