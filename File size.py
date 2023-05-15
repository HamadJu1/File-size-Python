import os

def get_large_files(path, size_limit):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > size_limit:
                print(f"File: {file_path}  Size: {file_size / (1024 * 1024):.2f} MB\n")


folder_path = r'C:\Users\Hamad\Downloads'


size_limit = 100 * 1024 * 1024

get_large_files(folder_path, size_limit)
