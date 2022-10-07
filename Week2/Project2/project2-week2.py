from typing import List, Any

from importing import *
import csv
import json

#file_path = '/Users/giuseppe/Desktop/Corsi/Epicode-DataAnalisys/epicode-data-analyst/Week2/project2/dataset/owid-covid-data (1).json'

file_path_csv = '/Users/giuseppe/Desktop/Corsi/Epicode-DataAnalisys/epicode-data-analyst/Week2/project2/dataset/owid-covid-data.csv'


def read_json(file_path):
    """
    Legge un file JSON e inserisce i dati in un dizionario
    :param file_path: file path of json
    :return: data read from file
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def read_csv_as_list(file_path, delimiter=","):
    """
    Legge un file CSV e inserisce i dati in una lista di liste (lista di righe)
    :param file_path: file path of csv
    :param delimiter: delimiter used in the csv file
    :return: data read from file
    """
    with open(file_path) as csv_file:
        data = csv.reader(csv_file, delimiter=delimiter)
    return data

#data_csv_list = read_csv_as_list(file_path_csv)
# print(data)


with open(file_path_csv, 'r') as read_obj:
    # Return a reader object which will
    # iterate over lines in the given csvfile
    csv_reader = csv.reader(read_obj)

    # convert string to list
    list_of_csv = list(csv_reader)

    data_csv_list: List[Any] = list_of_csv


['continent', 'location', 'date', 'total_cases', 'new_cases', 'new_cases_smoothed',]

headers = data_csv_list[0]

print(data_csv_list[2][1])



#headers = data_csv_list[0]

#print(data_csv_list[2][1])
"""
for i in data_csv_list:
    if data_csv_list[0][i] == 'ITA':
        dataset_italia.append(data_csv_list[i])
"""

#print(dataset_italia)



dataset_italy = []
dataset_uk = []
for row in data_csv_list:
    if row[2] == 'Italy':
        dataset_italy.append(row[2:5])
    elif row[2] == 'United Kingdom':
        dataset_uk.append(row[2:5])
"""        
for l in labels(range(0,len(labels))):
    for row in data_csv_list:
        if
"""

labels = ['date','new_cases','new_deaths','new_vaccinations']
labels_vaccinations = ['date','new_vaccinations']

dataset_italy = []
dataset_uk = []
"""
i=0
for l in labels:
    while i < len(data_csv_list[2]):
        for col in data_csv_list:
            if col[2] == 'Italy' and data_csv_list[i] in labels:
                dataset_italy.append(row[i])
            elif col[2] == 'United Kingdom' and data_csv_list[i] in labels:
                dataset_uk.append(row[i])
        i+=1

for l in labels:
    print(l)
"""
labels = ['date','new_cases','new_deaths','new_vaccinations']

dataset_italy = [[],]
for i in range(4):
    for row in data_csv_list:
        if row[2] == 'Italy':
            dataset_italy.append(row[3])
            dataset_italy.append(row[5])
            dataset_italy.append(row[8])
            dataset_italy.append(row[38])


cols = ['location','date','new_cases','new_deaths','new_vaccinations'] # define columns
data = [[] for col in cols] # this creates a list of **different** lists, not a list of pointers to the same list like you did in [[]]*len(positions)
with open(file_path_csv, 'r') as f:
    for rec in csv.DictReader(f):
        for l, col in zip(data, cols):
            l.append((rec[col]))
#print(data)



import csv
file =  open(file_path_csv, 'r')
reader = csv.reader(file)

items = ['location','date','new_cases','new_deaths','new_vaccinations']  # put the rows in csv to a list
aisle_dept_id = []  # to have a tuple of aisle and dept ids
mydict = {} # porudtc id as keys and list of above tuple as values in a dictionary

date, new_cases, new_deths, new_vacinations = [], [], [], []

for row in reader:
    items.append(row)

for i  in range(0, len(items)):
    data.append(items[i][0])
    new_cases.append(items[i][1])
    new_deths.append(items[i][2])
    new_vacinations.append(items[i][3])

for item1, item2 in zip(new_deths, new_cases):
    aisle_dept_id.append((item1, item2))
for item1, item2 in zip(new_deths, new_vacinations):
    mydict.update({item1: [item2]})

#print(dataset_italy)
#print(len(dataset_uk))

print(mydict)
