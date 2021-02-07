from typing import Dict, Set, Any
# Number of characters (including whitespace)
# Number of words (separated by whitespace)
# Number of lines
# Number of unique words (case sensitive, so “NO” is different from “no”)

file_path = "wcfile.txt"

def wc(file_path: str) -> Dict[str, int]:
    """
    Count:
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words (case sensitive, so “NO” is different from “no”)
    """
    unique_words = set()
    result = {
        "num_chars": 0,
        "num_words": 0,
        "num_lines": 0,
        "num_unique_words": 0
    }
    with open(file_path) as file:
        for line in file:
            result["num_chars"] += len(line)
            result["num_words"] += len(line.split())
            result["num_lines"] += 1
            unique_words.update(line.split())
    result["num_unique_words"] = len(unique_words)
    return result

def print_result(result: Dict[str, int]):
    for key, value in result.items():
        print(f'{key}: {value}')        

print_result(wc(file_path))
