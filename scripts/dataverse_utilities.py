import functools
import time
from IPython.display import Image, display
import httpx
import json
from datetime import datetime
from typing import List
from decouple import config


#################################################################################
# generic code to interact with the dataverse repository of the JDH of the C2DH #
#################################################################################


########################
# Retrieve information #
########################



# Dataverse url
DATAVERSE_URL = config('DATAVERSE_URL')
# APi token
API_TOKEN = config('API_TOKEN')

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))
        return value
    return wrapper

#In the notebook need to import implicetely the timer function 
#Example from scripts.dataverse_utilities import timer, test


# return the list of a dataset for a specific dataverse - issue
# for example jdh001 for the first issue
@timer 
def get_datasetids(dataverse_alias: str) -> List[str]: 
    url = DATAVERSE_URL+"api/dataverses/"+ dataverse_alias + "/contents"
    headers = {"X-Dataverse-key": API_TOKEN}
    r = httpx.get(url, headers=headers)
    issue = r.json()
    datasetids= []
    for article in issue['data']:
        datasetids.append(article['id'])
    return(datasetids)

def get_datafileid(dataverse_alias: str, orcid : str, filenameinput: str) -> str:
    datasetids = get_datasetids(dataverse_alias)
    for j in datasetids:
        url = DATAVERSE_URL+"api/datasets/" + str(j) 
        headers = {"X-Dataverse-key": API_TOKEN}
        r = httpx.get(url, headers=headers)
        datasets=r.json()
        data = datasets['data']
        title=data.get("latestVersion").get('metadataBlocks').get('citation').get('fields')[0].get('value')
        if title=='article_' + orcid: 
            files=data.get("latestVersion").get('files')
            for file in files:
                filename = file.get('label')
                if (filename==filenameinput):
                    result = file.get('dataFile').get('id')
                    break
            else:
                result = "File doesn't exist"
    return result   


@timer 
#def display_image():
#    display(Image(url="https://data.journalofdigitalhistory.org/api/access/datafile/6"))
