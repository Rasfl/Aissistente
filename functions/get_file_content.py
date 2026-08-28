import os
import sys

# import config:
pasta_atual = os.path.dirname(os.path.abspath(__file__))
pasta_pai = os.path.dirname(pasta_atual)
sys.path.append(pasta_pai)

from config import maxCharacters


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolutePath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absolutePath, file_path))
        validTargetDir = os.path.commonpath([absolutePath, targetDir]) == absolutePath
        isDir = os.path.isdir(targetDir)
            
        if not validTargetDir:
                return (f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
        if not isDir:
                return (f'Error: "{file_path}" is not a directory')
        else:
            # "with open" build-in with the "r" parameter to indicate "open for reading (default)" and read the text file. With the Max Characters defined in Aissistente/config.py
            with open(file_path, "r") as f:
                fileContentString = f.read(maxCharacters)
                if f.read(1):
                        content += f'[...File "{file_path}" truncated at {maxCharacters} characters]'
    except Exception as e:
          print(f"Error: '{e}'")