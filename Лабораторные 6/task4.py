import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    dict_json = []
    with open(filename, "r") as f:   # TODO реализовать конвертер из csv в json
        print(f.readlines())
        for row in f:
            dict_json.append(row)

    with open(filename, "w") as f_1:
        

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
