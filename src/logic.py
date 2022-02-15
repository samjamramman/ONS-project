import json
import requests

def get_useful_datasets():
    
    #gets the list of datasets
    datasets = requests.get("https://api.beta.ons.gov.uk/v1/datasets?limit=45")
    data = json.loads(datasets.text)
    
    usefulDatasets=[]
    
    for dataset in data["items"]: #cycles through each dataset
      try:  #if a keyword section is present
        keywords = dataset["keywords"]
        if "ASHE" in keywords:  #if the keyword "ASHE" is present
          usefulDatasets.append(dataset)
    
      except: #if there is no keyword section
        description = dataset["description"].lower().split(" ") #splits the discription string into a list of strings
        if ("incomes" or "income") in description:  #if the words "incomes" or "income" are in description
          usefulDatasets.append(dataset)
    return usefulDatasets
