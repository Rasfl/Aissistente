import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolutePath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absolutePath, directory))
        validTargetDir = os.path.commonpath([absolutePath, targetDir]) == absolutePath
        isDir = os.path.isdir(targetDir)
        
        if not validTargetDir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not isDir:
            return (f'Error: "{directory}" is not a directory')
        else:
            listDir = os.listdir(targetDir)

            listResult: list[str] = []
            for filesDir in listDir:
                itemPath = os.path.join(targetDir, filesDir)
                listResult.append(f"- {filesDir}: file_size={os.path.getsize(itemPath)} bytes, is_dir={isDir}")
            result = ""
            result = "\n".join(listResult)
            return result
        
    except Exception as e:
        print(f"Error: '{e}'")
