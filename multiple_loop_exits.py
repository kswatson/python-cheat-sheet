def find_old(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return 1


def find_pythonic(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        # Executes when loop ends normally
        return -1
    # Executes when loop breaks
    return 1


if __name__ == '__main__':
    def find_with_strategy(seq, target, strategy):
        found = strategy(seq, target)
        if found == -1:
            print(str(target) + ' Not Found')
        else:
            print(str(target) + ' Found')


    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    find_with_strategy(lst, -1, find_old)
    find_with_strategy(lst, 1, find_old)
    find_with_strategy(lst, -1, find_pythonic)
    find_with_strategy(lst, 1, find_pythonic)
