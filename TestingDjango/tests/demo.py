def add_1(x):
    return x + 1


def add_1_to_each_in_list(ll):
    return [add_1(x) for x in ll]


def test_with_empty_list():
    ll = []
    result = add_1_to_each_in_list(ll)
    if ll != result:
        raise Exception('list must be empty')
