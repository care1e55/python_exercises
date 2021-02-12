from typing import Any, Dict, Callable

def transform_values(func: Callable, d: Dict[str, Any]) -> Dict[str, Any]:
    return {
        key: func(value) for key, value in d.items()
    }

if __name__ == "__main__":
    d = {'a':1, 'b':2, 'c':3}
    print(transform_values(lambda x: x*x, d))
