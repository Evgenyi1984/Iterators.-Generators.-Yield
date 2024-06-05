class FlatIterator:

    def __init__(self, list_of_list):
        self._list = list_of_list               

    def flatten(self, lst):
        result=[]
        for i in lst:
            if isinstance(i,list):
                result += self.flatten(i)
            else:
                result.append(i)
        return result
         
    
    def __iter__(self):
        self._flat_list = self.flatten(self._list)           
        return self

    def __next__(self):
        if len(self._flat_list) == 0:
            raise StopIteration
        item = self._flat_list.pop(0)
        return item
    
   

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()