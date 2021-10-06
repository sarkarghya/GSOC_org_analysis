from dictlist_csv import dict_csv
from org_id import org_ids

# from data_dict import id_data
from dict_dat import dict_dat

if __name__ == "__main__":
    url = "https://summerofcode.withgoogle.com/organizations/?sp-page=6"
    #    u_list = []
    for iid in org_ids(url):
        #        u_list.append(id_data(iid))
        dict_dat(iid)
#    dict_csv(u_list, 'GSOC_orgs') # name of csv file in which I want my data stored
