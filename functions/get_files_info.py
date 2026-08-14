import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    absolutePath = os.path.abspath(working_directory)
    target_dir = os.path.normapath(os.path.normpath(absolutePath, directory))