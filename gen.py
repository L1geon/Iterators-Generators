nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(nested_list):
    for l in nested_list:
        for i in l:
            yield i


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
