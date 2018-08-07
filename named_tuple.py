from collections import namedtuple

NamedTuple = namedtuple('NamedTuple', 'field1 field2')

# https://docs.python.org/2/library/collections.html#collections.namedtuple
if __name__ == '__main__':
    print('A namedtuple is similar to an immutable dictionary.')
    instance_of_tuple = NamedTuple('val1', 'val2')
    print('Has a well formatted string representation.')
    print(instance_of_tuple)

    print('Can name arguments, unlike a dictionary')
    instance_of_tuple = NamedTuple(field1='val1', field2='val2')
    print(instance_of_tuple)

    print('Can access fields directly')
    print('val1: {}'.format(instance_of_tuple.field1))