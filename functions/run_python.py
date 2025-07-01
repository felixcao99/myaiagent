import os
import subprocess

def run_python_file(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    file_abpath = os.path.abspath(os.path.join(working_path, file_path))

    if os.path.exists(file_abpath):
        if not file_abpath.startswith(working_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not file_abpath.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        try:
            result = subprocess.run(['python3', file_abpath], check=True, text=True, timeout=30, capture_output=True, cwd=working_path)
            if not result.stdout and not result.stderr:
                return 'No output produced.'
            print("STDOOUT: ", result.stdout)
            print("STDERR: ", result.stderr)
            return "STDOUT: " + result.stdout + "\nSTDERR: " + result.stderr
        except subprocess.CalledProcessError as e:
            return f'Process exited with error code {e.returncode}'
        except Exception as e:
            return f"Error: executing Python file: {e}"
    else:
        return f'Error: File "{file_path}" not found.'
    
