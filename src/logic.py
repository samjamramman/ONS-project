import json
import requests


def get_datasets():
  datasets = requests.get("https://api.beta.ons.gov.uk/v1/datasets?limit=45")
  data = json.loads(datasets.text)
  return data

def get_pay_datasets():
    
    #gets the list of datasets
    datasets = get_datasets()
    
    payDatasets=[]
    
    for dataset in datasets["items"]: #cycles through each dataset
      try:  #if a keyword section is present
        keywords = dataset["keywords"]
        if "ASHE" in keywords:  #if the keyword "ASHE" is present
          payDatasets.append(dataset)
    
      except: #if there is no keyword section
        description = dataset["description"].lower().split(" ") #splits the discription string into a list of strings
        if ("incomes" or "income") in description:  #if the words "incomes" or "income" are in description
          payDatasets.append(dataset)
    return payDatasets

def get_latest_url_by_id(id):
  # This method must 1. call get_useful_datasets()
  datasets = get_datasets()
  #  2. search for the data set where 'id' is 'tax-benefits-statistics' 
  for dataset in datasets["items"]:
    if dataset["id"] == id:
      correctDataset = dataset
  # 3. return the value in .links.lastest.href
  return correctDataset["links"]["latest_version"]["href"]

def get_dataset_by_id(id):
  datasets = get_datasets()
  for dataset in datasets["items"]:
    if dataset["id"] == id:
      correctDataset = dataset
  return correctDataset