# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:57:39 2021

@author: Admin
"""
from gsoc_scraped import data_dicto 
c_dict = {}
for data in data_dicto:
    for langs in data['tech']:
        c_dict[langs] = c_dict.setdefault(langs, 0) + 1