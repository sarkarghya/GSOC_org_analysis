import pickle as pk
import os
from datetime import date
from datetime import timedelta


def stu_num(directory):
    o_dic = {"0-2": 0, "3-5": 0, "6-10": 0, "11-15": 0, "15+": 0}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path, "rb") as datfile:
            dic = pk.load(datfile)
            if len(dic["students"]) < 3:
                o_dic["0-2"] += 1
            elif len(dic["students"]) < 6:
                o_dic["3-5"] += 1
            elif len(dic["students"]) < 11:
                o_dic["6-10"] += 1
            elif len(dic["students"]) < 16:
                o_dic["11-15"] += 1
            else:
                o_dic["15+"] += 1
    return o_dic


if __name__ == "__main__":
    direct = f"./code/orgs-{date.today() - timedelta(days = 2)}/"  # edit date differance or type in full path
    print(stu_num(direct))
