import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a file, creating or overwriting it",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Relative path of the file to write to",
                },
                "content": {
                    "type": "string",
                    "description": "The string content to write into the file",
                },
            },
            "required": ["file_path", "content"],
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
