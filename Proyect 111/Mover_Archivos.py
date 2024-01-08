import os
import shutil

from_dir = "C:/Users/Acer/Downloads"
to_dir = "E:/Byjus/Documentos_Archivos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for names in list_of_files:
    name, extension = os.path.splitext(names)