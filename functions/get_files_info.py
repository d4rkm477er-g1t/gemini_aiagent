import os


def get_files_info(working_directory, directory = "."):
    files = []
    working_dir_abs = os.path.abspath(working_directory) 
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    try:
        if not directory:
            raise Exception(f'"{directory}" is not a directory')
        elif not valid_target_dir:
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        else:
            listed_directory = os.listdir(target_dir)
            print(listed_directory)
            for file in listed_directory:
                path = target_dir + f"/{file}"
                files.append(f"{file}: file_size={os.path.getsize(path)} bytes, is_dir={os.path.isdir(path)}")
            return "- " + "\n- ".join(files)
    except Exception as e:
            print(f"Error: {e=}")