"""
 Inspect code below. You won't be able to run it as it is.
 original task here: https://www.online-ide.com/NHdk4IPVcy

 Find all bugs, errors, refactor (fix formatting etc.).
 Feel free to change, remove, rewrite or add parts of code, rename variables etc. to follow best code practices.
 Make sure the code snippet runs and works correctly in all cases.
 When you are done copy fixed code and past it in the answer field in tests. Good luck!

 Expected output of update_configs("me"):
 Saving new config :{'key1': 'value_1', 'key2': 'value_2', 'key3': 'value_3', 'modified_date': <date and time now>, 'modified_by': 'me', 'max_product_count': 10}

"""

import json
from datetime import datetime

data_types = ["text", "json"]


class FileReader:
    """Context manager to convert input file into .cfg"""

    def __init__(self, data_type: str, file_path: str):
        if data_type in data_types:
            self._data_type = data_type
        else:
            raise Exception

        self.file_path = file_path

    def __enter__(self):
        file = open(self.file_path)

        if self._data_type == "json":
            self.payload = json.load(file)
        elif self._data_type == "text":
            self.payload = {}

            for line in file:
                (k, v) = line.split()
                self.payload[k] = v
        else:
            raise Exception

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        output_file = open('result.cfg', 'w+')
        print(f"Saving new config :{self.payload}")
        json.dump(self.payload, output_file)
        output_file.close()


def update_configs(user, file="test_data.txt", d_type="text"):
    """ Function to update configs.

    Parameters:
            user (string): User
            file (string): File path
            d_type (string): Data type
    """
    additional_config = {
        "modified_date": str(datetime.now()),
        "modified_by": user,
        "max_product_count": 10
    }

    with FileReader(d_type, file) as file:
        file.payload = {**file.payload, **additional_config}


update_configs("me")
# update_configs("me", "test_data.json", "json")
