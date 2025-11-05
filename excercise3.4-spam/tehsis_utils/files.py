import os

def get_file_content(file_path, encoding="utf-8"):
    try:
        with open(file_path, 'r', encoding=encoding, errors="ignore") as file:
            if not os.path.isdir():
              content = file.read()
              return content
    except FileNotFoundError:
        print(f"Error: The file: {file_path} was not foud")
    except Exception as e:
        print(f"Error in file after ex ${file}: {e}")

def read_from_dirs(dirs, encoding="cp1252"):
    results = []
    for dir in dirs:
        files_paths = os.listdir(dir)
        for fp in files_paths:
            results.append(get_file_content(os.path.join(dir, fp), encoding))
    return results
