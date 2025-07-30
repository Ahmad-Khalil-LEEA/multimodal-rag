import os

def list_files_recursive(folder, ext=None):
    files = []
    for root, dirs, filenames in os.walk(folder):
        for filename in filenames:
            if ext is None or filename.endswith(ext):
                files.append(os.path.join(root, filename))
    return files
