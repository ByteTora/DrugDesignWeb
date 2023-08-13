import os

def read_path(dir):
    folder_path = dir
    file_names = os.listdir(folder_path)
    return file_names