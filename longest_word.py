from typing import Dict
import os

def find_longest_word(file_path: str) -> str:
    longest = ""
    with open(file_path) as file:
        for line in file:
            if not line.strip():
                continue
            cur_longest = max(
                line.strip().split(), key = lambda word: len(word) 
            )
            if len(cur_longest) > len(longest):
                longest = cur_longest
    return longest

def find_all_longest_words(dir_path: str) -> Dict[str, str]:
    return {
        file: find_longest_word(os.path.join(dir_path,file)) 
        for file in os.listdir(dir_path)
    }

if __name__ == "__main__":
    test_file_path = "books/84-0.txt"
    test_dir_path = "books"
    result = find_longest_word(test_file_path)
    print(result)
    result = find_all_longest_words(test_dir_path)
    print(result)
