from dictlist_csv import dict_csv
from org_dict import org_dict

if __name__ == "__main__":
    url = "https://summerofcode.withgoogle.com/organizations/?sp-page=6"
    dict_csv(org_dict(url), 'GSOC_orgs') # name of csv file in which I want my data stored