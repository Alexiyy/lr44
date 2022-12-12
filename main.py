import os

dictionary = {}


def input_path():
    pass  # 


def create_dict(path):
    pass  # 


def analyze_dict(dictionary):
    names = []  # Список имён
    weight = []  # Список веса файлов
    for k in dictionary.keys():
        names.append(os.path.basename(k))
    for v in dictionary.values():
        weight.append(v)
    doubles = {}
    for i in range(len(names)):
        count = 0
        for j in range(len(names)):
            if names[i] == names[j]:  # Сравниваем имена файлов
                if weight[i] == weight[j]:  # Сравниваем вес файлов, если всё совпало - дубликат
                    count += 1
                doubles[names[i]] = count
    return doubles


def duplicate_files(doubles):
    pass #

if __name__ == '__main__':
    duplicate_files(analyze_dict(create_dict(input_path())))
