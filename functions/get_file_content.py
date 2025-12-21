import os
from config import READ_LIMIT

def get_file_content(working_directory, file_path):
    files = []
    working_dir_abs = os.path.abspath(working_directory) 
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    print(target_dir)
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    try:
        if not valid_target_dir:
            raise Exception(f'Cannot read "{file_path}" as it is outside the permitted working directory')
        elif not os.path.isfile(target_dir):
            raise Exception(f'File not found or is not a regular file: "{file_path}"')          
        else:
            with open(target_dir, "r") as file:
                content = file.read(READ_LIMIT)
                if file.read(1):
                    content += f'[... File "{file_path}" trucated at {READ_LIMIT} characters]'
                return content
    except Exception as e:
        print(f"Error: {e=}")