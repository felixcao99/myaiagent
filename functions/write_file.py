import os

def write_file(working_directory, file_path, content):
    working_path = os.path.abspath(working_directory)
    file_abpath = os.path.abspath(os.path.join(working_path, file_path))

    if not file_abpath.startswith(working_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(file_abpath, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Could not write to file "{file_path}": {str(e)}'
