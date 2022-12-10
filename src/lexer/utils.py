from pathlib import Path

def file_dir(file):
    return Path(file).parent

def read_lines(py_file, target_file):
    with open(file_dir(py_file) / target_file) as f:
        return [line.strip() for line in f.readlines()]