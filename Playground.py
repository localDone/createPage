import glob
import os

file_path = "/home/done/Documents/nginx/v/Vz/"

for raw_file_name in glob.glob(os.path.join(file_path, '*.jpeg')):
    print(raw_file_name)