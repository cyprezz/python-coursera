import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def write_data(key, val, new_data):
    if key not in new_data:
        new_data[key] = list()
    new_data[key].append(val)
    json_data = json.dumps(new_data)

    with open(storage_path, 'w') as f:
        f.write(json_data)


def read_file():
    curr_data = dict()
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            curr_data = f.read()
            if curr_data:
                curr_data = json.loads(curr_data)

    return curr_data


if args.key and not args.val:
    data = read_file()
    if args.key not in data:
        print(None)
    else:
        found = data[args.key]
        print(', '.join(found))
elif args.key and args.val:
    data = read_file()
    write_data(args.key, args.val, data)
else:
    print('No input data')
