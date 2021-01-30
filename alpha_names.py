from operator import itemgetter
from typing import Tuple, Dict

PEOPLE = [
    {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
    {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
    {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
]

def get_first_last(row: Dict) -> Tuple[str]:
    return row['first'], row['last']

result1 = sorted(PEOPLE, key=get_first_last)
result2 = sorted(PEOPLE, key=lambda row: (row['first'], row['last']))
result3 = sorted(PEOPLE, key=itemgetter('first','last'))
print(result1, end='\n\n')
print(result2, end='\n\n')
print(result3, end='\n\n')
