import tkinter as tk
from tkinter import filedialog

all_files_paths = tk.filedialog.askopenfilenames(title="Select files to be organised", filetypes=[("All files", "*.*")])

print(all_files_paths)

all_folders_paths = []

for files_path in all_files_paths:
    print(files_path)
    folder = filedialog.askdirectory(title="Select folders as the destination for organised files")

    all_folders_paths.append(folder)
