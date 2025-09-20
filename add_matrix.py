class Tensor:
    def __init__(self, data: list[list[list]]):
        self.data = data

    @property
    def shape(self):
        return (len(self.data), len(self.data[0]), len(self.data[0][0]))


    def __iter__(self):
      return self

    def __next__(self):
        for list_1 in self.data:
            for list_2 in list_1:
                for num in list_2:
                    yield num
        raise StopIteration

    def __eq__(self, other: "Tensor") -> bool:
        return self.data == other.data

    def __add__(self, other: "Tensor"):
        result_list = [] 
        for self_1, other_1 in zip(self.data, other.data):
            result_1_list = []
            for self_2, other_2 in zip(self_1, other_1):
                result_2_list = [] 
                for self_3, other_3 in zip(self_2, other_2):
                    result_2_list.append(self_3 + other_3)
                result_1_list.append(result_2_list)
            result_list.append(result_1_list)
        return Tensor(result_list)
    
    def __str__(self) -> str:
        return str(self.data)
    
    __repr__ = __str__
    

if __name__ == '__main__':
    test_tensor_1 = Tensor([[[1,1], [1,1]], [[1,1], [1,1]]])
    test_tensor_2 = Tensor([[[1,1], [1,1]], [[1,1], [1,1]]])
    expected_result_tensor = Tensor([[[2,2], [2,2]], [[2,2], [2,2]]])
    print(test_tensor_1 + test_tensor_2)
    print((test_tensor_1 + test_tensor_2) == expected_result_tensor)
    print((test_tensor_1 + test_tensor_2).shape)
    print(expected_result_tensor.shape)
