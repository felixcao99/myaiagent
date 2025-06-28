import os

def get_files_info(working_directory, directory=None):
    working_path = os.path.abspath(working_directory)
    directory_path = os.path.abspath(os.path.join(working_path, directory))
    if os.path.isdir(directory_path):
        if not directory_path.startswith(working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            files = os.listdir(directory_path)
            results = ""
            for file in files:
                line = f"- {file}: file_size={os.path.getsize(os.path.join(directory_path, file))} bytes, is_dir={os.path.isdir(os.path.join(directory_path, file))}\n"
                results += line
            return results
    else:
        return f'Error: "{directory}" is not a directory'
