nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.cursor = -1
        self.list_len = len(self.nested_list)

    def __iter__(self):
        self.cursor += 1
        self.cursor_2 = 0
        return self

    def __next__(self):
        if self.cursor_2 == len(self.nested_list[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.cursor_2 += 1
        return self.nested_list[self.cursor][self.cursor_2 - 1]



if __name__ == '__main__':
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


