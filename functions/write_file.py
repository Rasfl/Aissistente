import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write content to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
            },
        },
    },
}


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolutePath = os.path.abspath(working_directory)
        targetFile = os.path.normpath(os.path.join(absolutePath, file_path))
        validTargetDir = os.path.commonpath([absolutePath, targetFile]) == absolutePath
        isDir = os.path.isdir(targetFile)

        if not validTargetDir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if isDir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parentDir = os.path.dirname(targetFile)
        if parentDir:
            os.makedirs(parentDir, exist_ok=True)
        with open(targetFile, "w", encoding="utf-8") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f"Error: '{e}'")
