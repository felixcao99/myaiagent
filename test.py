import os
working_director = 'calulator'
directory = '../'
working_path = os.path.abspath(working_director)
print(working_path)
print(os.path.join(working_path,directory))
print(os.path.abspath(os.path.join(working_path, directory)))
