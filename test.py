import os
working_director = 'calulator'
file = 'tt.txt'
working_path = os.path.abspath(working_director)
file_abpath = os.path.abspath(os.path.join(working_path, file))
print(working_path)
print(os.path.join(working_path,directory))
print(os.path.abspath(os.path.join(working_path, directory)))
