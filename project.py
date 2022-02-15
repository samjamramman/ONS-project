#samjamramman
#Project for andrew
import json

import src.logic as logic

usefulDatasets = logic.get_useful_datasets()

#puts the relevent datasets in a json file
with open("usefulDatasets.json", "w") as file:
    json.dump(usefulDatasets, file, indent=4)

print("All finished")