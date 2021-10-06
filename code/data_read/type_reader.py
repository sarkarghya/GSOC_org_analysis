import pickle as pk
import os
from datetime import date
from datetime import timedelta


def type_org(directory):
    o_dic = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path, "rb") as datfile:
            dic = pk.load(datfile)
            o_dic.setdefault(dic["org_type"], 0)
            o_dic[dic["org_type"]] += 1
    return {k: v for k, v in sorted(o_dic.items(), key=lambda item: item[0])}


if __name__ == "__main__":
    direct = f"./code/orgs-{date.today() - timedelta(days = 1)}/"  # edit date differance or type in full path
    print(type_org(direct))
