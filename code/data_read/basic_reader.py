import pickle as pk
import os
from datetime import date
from datetime import timedelta


def dict_print(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path, "rb") as datfile:
            print(pk.load(datfile))


if __name__ == "__main__":
    direct = f"./code/orgs-{date.today() - timedelta(days = 2)}/"  # edit date differance or type in full path
    dict_print(direct)
