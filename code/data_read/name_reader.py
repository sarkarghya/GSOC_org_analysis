import pickle as pk
import os
from datetime import date
from datetime import timedelta

directory = f'./code/orgs-{date.today() - timedelta(days = 1)}/' # edit date differance or type in full path

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    with open(file_path, 'rb') as datfile:
        dic = pk.load(datfile)
        print(dic['name'])