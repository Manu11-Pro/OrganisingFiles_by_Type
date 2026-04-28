import shutil
import os
import sys
from .utils import all_files_paths, all_folders_paths
from .file_info_dictionary import file_info

if sys.version_info < (3, 14):
    sys.exit("OrganisingFiles_by_Type requires Python3.14.x+ to work as intended")
    
def main():
    extension_map = {ext : category for category,
                    exts in file_info.items() for ext in exts}

    for files_path , folder_path in zip (all_files_paths, all_folders_paths):

        filename, ext = os.path.splitext(files_path)
        ext = ext.lower()

        category = extension_map.get(ext, "Others")

        dest_dir = os.path.join(folder_path, category)
        os.makedirs(dest_dir, exist_ok=True)

        shutil.copy2(files_path, dest_dir)
        print(f"Organised {os.path.basename(files_path)} to {dest_dir}")

if __name__ == "__main__":
    main()