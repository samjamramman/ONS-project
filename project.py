#samjamramman
#Project for andrew
import json
import requests
import src.logic as logic

usefulDatasets = logic.get_pay_datasets()

#puts the relevent datasets in a json file
with open("usefulDatasets.json", "w") as file:
    json.dump(usefulDatasets, file, indent=4)

link = logic.get_latest_url_by_id("tax-benefits-statistics")
dataset = requests.get(link)
data = json.loads(dataset.text)
with open("currentDatasets.json", "w") as file:
    json.dump(data, file, indent=4)