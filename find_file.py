from genericpath import isdir
from pathlib import Path
from typing import List


def find(path: Path, filename: str) -> List[Path]:
    found_filenames = []
    if path.is_dir():
        for _path in path.glob('*'):
            found_filenames += find(_path, filename)
    if filename in str(path):
        found_filenames.append(path)
    return found_filenames


if __name__ == '__main__':
    test_file_name = 'test_file.file'
    expected_file_path = [Path('test_dir') / 'test_1' / test_file_name]
    result_file_path = find(Path('test_dir'), test_file_name)
    assert result_file_path == expected_file_path

    test_file_name = 'test_file_1.file'
    expected_file_path = [Path('test_dir') / 'test_2' / test_file_name]
    result_file_path = find(Path('test_dir'), test_file_name)
    assert result_file_path == expected_file_path
