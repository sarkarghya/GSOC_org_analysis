import csv

def dict_csv(dict_data, name):
    try:
        with open(f"{str(name)}.csv", 'w', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(dict_data[0].keys()) )
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
            print(f'Data has been saved in {str(name)}.csv')
    except IOError:
        print("I/O error")