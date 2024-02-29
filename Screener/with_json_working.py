import json


def dump_valid_pairs(exchange, pairs):
    try:
        with open(f'crypto_pairs_data/{exchange}.json', 'w') as json_file:
            json.dump(pairs, json_file, indent=4)
    except Exception as exception:
        print(exception)


def load_valid_pairs(exchange):
    try:
        with open(f'crypto_pairs_data/{exchange}.json') as json_file:
            data = json.load(json_file)
        return data

    except Exception as exception:
        print(exception)
