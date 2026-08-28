import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolutePath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absolutePath, directory))
        validTargetDir = os.path.commonpath([absolutePath, targetDir]) == absolutePath
        isDir = os.path.isdir(directory)
        if not validTargetDir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not isDir:
            return (f'Error: "{directory}" is not a directory')
        else:
            return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        print(f"Error: '{e}'")
