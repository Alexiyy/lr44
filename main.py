import os

dictionary = {}


def input_path():
    pass  # 


def create_dict(path):
    for filename in os.listdir(path):
        try:
            path_to_file = os.path.join(path, filename)
            if os.path.isdir(path_to_file):
                create_dict(path_to_file)
            else:
                dictionary[path_to_file] = os.path.getsize(path_to_file)
        except PermissionError:  # Ошибка доступа
            pass
    return dictionary 


def analyze_dict(dictionary):
    pass  # 


def duplicate_files(doubles):
    pass #

if __name__ == '__main__':
    duplicate_files(analyze_dict(create_dict(input_path())))
