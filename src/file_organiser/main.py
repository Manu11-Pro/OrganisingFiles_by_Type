import shutil
import os
from .gui import *

for files_path in all_files_paths:

    folder_path = input("Enter the path of folder to organise: ").strip(' "')

    file_path = files_path

    file_name_with_ext_only = os.path.basename(file_path)
    print(file_name_with_ext_only)

    filename, ext = os.path.splitext(file_name_with_ext_only)

    ext.lower()

    #Images

    dest_dir_images = os.path.join(folder_path, "Images")

    if ext == ".png":
        if not os.path.exists(dest_dir_images):
            os.makedirs(dest_dir_images)
        shutil.copy2(file_path , dest_dir_images)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_images}")

    if ext == ".jpg":
        if not os.path.exists(dest_dir_images):
            os.makedirs(dest_dir_images)
        shutil.copy2(file_path , dest_dir_images)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_images}")

    if ext == ".jpeg":
        if not os.path.exists(dest_dir_images):
            os.makedirs(dest_dir_images)
        shutil.copy2(file_path , dest_dir_images)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_images}")

    #Documents

    dest_dir_docs = os.path.join(folder_path, "Documents")

    if ext == ".pdf":
        if not os.path.exists(dest_dir_docs):
            os.makedirs(dest_dir_docs)
        shutil.copy2(file_path , dest_dir_docs)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_docs}")

    if ext == ".txt":
        if not os.path.exists(dest_dir_docs):
            os.makedirs(dest_dir_docs)
        shutil.copy2(file_path , dest_dir_docs)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_docs}")

    if ext == ".docx":
        if not os.path.exists(dest_dir_docs):
            os.makedirs(dest_dir_docs)
        shutil.copy2(file_path , dest_dir_docs)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_docs}")

    #Videos

    dest_dir_videos = os.path.join(folder_path, "Videos")

    if ext == ".mp4":
        if not os.path.exists(dest_dir_videos):
            os.makedirs(dest_dir_videos)
        shutil.copy2(file_path , dest_dir_videos)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_videos}")

    if ext == ".mov":
        if not os.path.exists(dest_dir_videos):
            os.makedirs(dest_dir_videos)
        shutil.copy2(file_path , dest_dir_videos)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_videos}")

    #Musics

    dest_dir_musics = os.path.join(folder_path, "Musics")

    if ext == ".mp3":
        if not os.path.exists(dest_dir_musics):
            os.makedirs(dest_dir_musics)
        shutil.copy2(file_path , dest_dir_musics)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_musics}")

    if ext == ".wav":
        if not os.path.exists(dest_dir_musics):
            os.makedirs(dest_dir_musics)
        shutil.copy2(file_path , dest_dir_musics)
        print(f"Organised {file_name_with_ext_only} to {dest_dir_musics}")
