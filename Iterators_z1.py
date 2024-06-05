class FlatIterator:

    def __init__(self, list_of_list):
        self._list = list_of_list               

    def __iter__(self):
        flat_list = []
        for i in self._list:
            for m in i:
                flat_list.append(m)
        self._flat_list = flat_list            
        return self

    def __next__(self):
        if len(self._flat_list) == 0:
            raise StopIteration
        item = self._flat_list.pop(0)
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()