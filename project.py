#samjamrammanl
#Project for andrew
import requests
import json

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

#puts the relevent datasets in a json file
with open("usefulDatasets.json", "w") as file:
    json.dump(usefulDatasets, file, indent=4)

print("All finished")
