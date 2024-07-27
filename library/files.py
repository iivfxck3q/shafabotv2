import json
import os


def read_txt(filepath) -> str:
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def read_json(filepath) -> str:
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_txt(filepath, data):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filepath, 'a', encoding='utf-8') as file:
        if os.path.getsize(filepath) > 0:
            file.write('\n')
        file.write(data)


def write_json(filepath, data):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    except json.JSONDecodeError:
        existing_data = []

    if not isinstance(existing_data, list):
        existing_data = [existing_data]

    if isinstance(data, list):
        existing_data.extend(data)
    else:
        existing_data.append(data)

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)
