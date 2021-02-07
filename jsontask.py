import os
import glob
import json
from typing import Dict
from collections import defaultdict

def summary_score(file_path: str) -> Dict[str, Dict[str, float]]:
    subject_grades = defaultdict(list)
    with open(file_path) as file:
        for line in json.load(file):
            for subject, grade in line.items():
                subject_grades[subject].append(grade)
    return {
        subject : {
            'min': min(grades), 
            'max': max(grades), 
            'average': sum(grades)/len(grades)
        }
        for subject, grades in subject_grades.items() 
    }
    
def all_scores(dir_path: str) -> Dict[str, Dict[str, Dict[str, float]]]:
    return {
        file_path.split('/')[-1]: summary_score(file_path) 
        for file_path in glob.glob(
            os.path.join(dir_path, "*.json")
        ) 
    }

def print_pretty_stats(stats: Dict[str, Dict[str, Dict[str, float]]]):
    for file_name, file_stats in stats.items():
        print(file_name)
        for subject, subject_stat in file_stats.items():
            print("\t" + subject + ": ", end='')
            for stat, value in subject_stat.items():
                print(f'{stat} {value}', end=' ')
            print("")

if __name__ == "__main__":
    test_dir_path = "scores"
    stats = all_scores(test_dir_path)
    print_pretty_stats(stats)
