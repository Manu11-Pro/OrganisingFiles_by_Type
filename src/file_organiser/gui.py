import tkinter as tk
from tkinter import filedialog

all_files_paths = tk.filedialog.askopenfilenames(title="Open a file", filetypes=[("All files", "*.*")])

print(all_files_paths)

for files_path in all_files_paths:
    print(files_path)
