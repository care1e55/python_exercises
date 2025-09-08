


def binary_search(input_sequence: list[int], search_element, start, end) -> int | None:
    if end == start:
        mid = end
    elif end < start:
        return None
    else: 
        mid = (end - start) // 2
    mid_element = input_sequence[mid]
    if mid_element == search_element:
        return mid
    if mid_element > search_element:
        start, end = start, mid-1
    elif mid_element < search_element:
        start, end = mid+1, end
    return binary_search(input_sequence, search_element, start, end)
    
    



if __name__ == '__main__':
    input_sequence = [1, 2, 3, 4, 5, 6, 7]
    search_element = 3
    expected_element_index = 2
    element_index = binary_search(input_sequence, search_element, 0, len(input_sequence)-1)
    assert element_index == expected_element_index
