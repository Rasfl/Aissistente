import os
from config import maxCharacters

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads and returns the contents of a specific file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Relative path of the file to read",
                },
            },
            "required": ["file_path"],
        },
    },
}
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolutePath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absolutePath, file_path))
        validTargetDir = os.path.commonpath([absolutePath, targetDir]) == absolutePath
        isFile = os.path.isfile(targetDir)
            
        if not validTargetDir:
                return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
        if not isFile:
                return f'Error: "{file_path}" is not a directory'
        else:
            # "with open" build-in with the "r" parameter to indicate "open for reading (default)" and read the text file. With the Max Characters defined in Aissistente/config.py
            with open(targetDir, "r") as f:
                fileContentString = f.read(maxCharacters)
                if f.read(1):
                        fileContentString += f'[...File "{targetDir}" truncated at {maxCharacters} characters]'

                return fileContentString
    except Exception as e:
        print(f"Error: '{e}'")
