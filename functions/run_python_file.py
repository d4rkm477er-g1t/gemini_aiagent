import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory) 
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    try:
        if not valid_target_dir:
            raise Exception(f'Cannot execute "{file_path}" as it is outside the permitted working directory')
        elif not os.path.isfile(target_dir):
            raise Exception(f'"{file_path}" does not exist or is not a regular file')
        elif ".py" not in file_path:
            raise Exception(f'"{file_path}" is not a Python file')
        else:
            command = ["python", target_dir]
            if args:
                command.extend(args)
            result = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)
            output = ""
            if result.returncode != 0:
                output += f"Process exited with code {check_returncode(result)}"
            elif result.stdout != None and result.stderr == None:
                output += "No output produced"
            else:
                output += f'STDOUT: {result.stdout}, STDERR: {result.stderr}'
            return output
    except Exception as e:
        return f"Error: {e=}"
            