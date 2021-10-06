import pickle as pk
import os
from datetime import date
from datetime import timedelta


def clean(stir):
    return "".join(
        [st for st in stir if not (st.isnumeric() or st.isspace() or st == ".")]
    )


def defra(lisa):
    n_lisa = []
    for item in lisa:
        n_lisa.extend(item.split("/"))
    return n_lisa


def lang_org(directory):
    langs_raw = ["c++", "c", "javascript", "java", "python"]  # add other languages
    langs = sorted(langs_raw, key=len)
    la_c = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path, "rb") as datfile:
            dic = pk.load(datfile)
        for item in defra(dic["tech"]):
            for lang in langs:
                ci = clean(item.lower())
                if lang in ci and (len(lang) == len(ci)):
                    la_c.setdefault(lang, []).append(dic["name"])
    x = dict(map(lambda x: (x[0].capitalize(), len(set(x[1]))), la_c.items()))
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    # return set(la_c) #to see orgs


if __name__ == "__main__":
    direct = f"./code/orgs-{date.today() - timedelta(days = 2)}/"  # edit date differance or type in full path
    print(lang_org(direct))
