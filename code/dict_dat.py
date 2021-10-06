import pickle as pk
from datetime import date
import os.path
from data_dict import id_data

def dict_dat(iid):
    directory = f'./orgs-{date.today()}/'
    file_path = os.path.join(directory, f"{str(iid)}.dat")
    if not os.path.isdir(directory):
        os.mkdir(directory)
    try:
        with open(file_path, 'wb') as datfile:
            pk.dump(id_data(iid), datfile)
    except IOError:
        print("I/O error")