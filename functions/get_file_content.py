import os

def get_file_content(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    file_abpath = os.path.abspath(os.path.join(working_path, file_path))

    if os.path.isfile(file_abpath):
        if not file_abpath.startswith(working_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            results = ""
            maxchars = 10000
            with open(file_abpath, 'r') as file:
                content = file.read(maxchars)
                results += content
                if len(content) == maxchars:
                    results += f'[...File "{file_path}" truncated at 10000 characters]'
            return results
    else:
        return f'Error: File not found or is not a regular file: "{file_path}"'