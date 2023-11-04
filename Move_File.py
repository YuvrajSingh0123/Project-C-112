import os
import shutil
from_dir ="C:/Users/Dell/Downloads"
to_dir = "C:/Users/Dell/OneDrive/Desktop/Document_Files"
List_of_Files = os.listdir(from_dir)
print(List_of_Files)
for file_name in list_of_files:
     name, extension = os.path.splitext(file_name)
     print(name)
     print(extension)
     