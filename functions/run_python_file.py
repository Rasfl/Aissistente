import os
import subprocess
import sys

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file in the specified working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Arguments to pass to the Python file",
                },
            },
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        absolutePath = os.path.abspath(working_directory)
        targetFile = os.path.normpath(os.path.join(absolutePath, file_path))
        validTargetDir = os.path.commonpath([absolutePath, targetFile]) == absolutePath
        isFile = os.path.isfile(targetFile)

        if not validTargetDir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        elif not isFile:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        else:
            outputPart = []
            command = [sys.executable, targetFile]
            if args:
                command.extend(args)

            result = subprocess.run(
                command,                            # List of commands.
                cwd=working_directory,               # Directory of work.
                capture_output=True,                 # To capture stdout and stderr.
                text=True,                           # To decode the output to string, rather than bytes.
                timeout=30                          # To prevent infinite execution, set a timeout of 30 seconds to prevent.
            )
            if result.returncode != 0:
                outputPart.append(f"Process exited with code {result.returncode}") 
            if not result.stdout and not result.stderr:
                outputPart.append("No output produced")
            else:
                if result.stdout:
                    outputPart.append(f"STDOUT:\n{result.stdout.strip()}")
                if result.stderr:
                    outputPart.append(f"STDERR:\n{result.stderr.strip()}")
        return "\n".join(outputPart)

    except subprocess.TimeoutExpired:
        return f"Error: Process timed out after after {result.timeout} seconds"
    except Exception as e:
        print(f"Error: executing Python file: {e}")
