from pathlib import Path

if Path('README.md').exists():
    pass
else:
    print("README.md doesn't exist!")

if Path('.cleagitignore').exists():
    pass
else:
    print("gitignore doesn't exist!")





#import pathlib
#import os

#file_path = pathlib('README.md')

#current_directory = os.getcwd()
#print ('Currenty directory is', current_directory)

#file = ('README.md')

#if file_path.exists():
 #   pass
#else:
 #   print("File not found!")