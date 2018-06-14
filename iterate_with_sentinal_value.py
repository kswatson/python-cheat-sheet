from functools import partial

def old_way(to_be_read, sentinal_value):
    blocks = []
    while True:
        block = to_be_read.read(2)
        if block == sentinal_value:
            break
        blocks.append(block)
    return blocks

def pythonic_way(to_be_read, sentinal_value):
    blocks = []
    read_block = partial(to_be_read.read, 2)
    for block in iter(read_block, sentinal_value):
        blocks.append(block)
    return blocks

def pythonic_simpler_way(to_be_read, sentinal_value):
    blocks = ''.join(iter(partial(to_be_read.read, 2), sentinal_value))
    return blocks

if __name__ == '__main__':
    def read_with_strategy(filename, sentinal_value, strategy):
        with open(filename) as file:
            print(strategy(file, sentinal_value))

    read_with_strategy('test_file', '', old_way)
    read_with_strategy('test_file', '', pythonic_way)
    read_with_strategy('test_file', '', pythonic_simpler_way)