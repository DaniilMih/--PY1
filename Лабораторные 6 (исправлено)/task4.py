import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter, new_line):
    with open(filename) as f:
        js_dict = []
        for value, line in enumerate(f):
            fields = line.strip(new_line).split(delimiter)
            if value == 0:
                heads = fields
                continue

            js_dict.append({})

            for i, _ in enumerate(heads):

                js_dict[-1][heads[i]] = fields[i]
    return js_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE, ',', '\n'), indent=4))
