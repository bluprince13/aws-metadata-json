from get_metadata import get_metadata


# https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-python-dictionaries-and-lists
def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(key):
    metadata = get_metadata()
    return list(gen_dict_extract(key, metadata))


if __name__ == '__main__':
    key = input("What key would you like to find?\n")
    print(find_key(key))
