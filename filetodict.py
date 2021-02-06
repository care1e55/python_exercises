from typing import Dict

def file_to_dict(file_path: str) -> Dict[str, str]:
    users = {}
    with open(file_path) as file:
        for line in file:
            if not line.startswith("#"): 
                line = line.strip().split(":")
                users[line[0]] = line[2]
    return users

def print_dict(users: Dict[str, str]):
    for line in users.items():
        print(f'{line[0]} {line[1]}')

users = file_to_dict("/etc/passwd")
print_dict(users)
