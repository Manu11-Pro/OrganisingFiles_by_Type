from utils import ext

file_info = {"Images": [".png", ".jpg", ".jpeg"],
             "Documents": [".txt", ".pdf", ".docx"],
             "Videos": [".mp4", ".mov", ".ogv"]}

extension_map = {ext : category for category, exts in file_info.items() for exts in ext}