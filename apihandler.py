"""
Handles the interactions with the rick and morty API
Functions:
  
  getAllPages(str) -> dict
  getDictionaries(str) -> dict
  storeDictionaries(dict, dict, dict) -> .JSON, .JSON, .JSON
  readDictionaries(.JSON, .JSON, .JSON) -> dict, dict, dict
  requestJSON(str) -> expected dict
  
Misc variables:

  None

Classes:
  
  None
"""

#Imports for handling files and web requests
import requests
import json

#Functions:

def requestJson(url: str):
  output = requests.get(url)
  output.raise_for_status()
  output = output.json()
  return output

def getAllPages(api_endpoint: str):
  """
  Function to get all the pages from a given API endpoint. Called by the getDictionaries function.
  Args:
    site (str): The API endpoint URL.
  Returns:
    api_dict (dict): A dictionary containing all pages of results.
  """
  #initialise the dictionary returned from the api
  api_dict = requestJson(api_endpoint)
  
  #loop over the number of pages returned by the api
  maxpages = int(api_dict['info']['pages'])
  for page_num in range(2,maxpages,1):
    nextpageurl = api_endpoint+"/?page="+str(page_num)
    nextpage = requestJson(nextpageurl)
    #the extend method adds all the items from the list individually rather than as one item
    api_dict['results'].extend(nextpage['results'])
  
  return api_dict

def getDictionaries(url: str):
  """
  Function that returns the json files from the entire rick and morty api as dictionaries
  Args:
    url (str): The API base URL.
  Returns:
    characters_dict (dict): A dictionary containing all characters.
    locations_dict (dict): A dictionary containing all locations.
    episodes_dict (dict): A dictionary containing all episodes.
  """
  #base dictionary contains links to characters, locations and episodes  
  base_dict = requestJson(url)

  #getting characters
  characters_url = str(base_dict['characters'])
  characters_dict = getAllPages(characters_url)

  #getting locations
  locations_url = str(base_dict['locations'])
  locations_dict = getAllPages(locations_url)
  
  #getting episodes
  episodes_url = str(base_dict['episodes'])
  episodes_dict = getAllPages(episodes_url)
  return characters_dict, locations_dict, episodes_dict

def storeDictionaries(characters_dict: dict, locations_dict: dict, episodes_dict: dict):
  """
  Test function that converts the dictionaries created by getDictionaries() to json files.
  (Do not use when testing API retrieval)
  Args:
    characters_dict (dict): A dictionary containing all characters.
    locations_dict (dict): A dictionary containing all locations.
    episodes_dict (dict): A dictionary containing all episodes.
  """
  with open("JSON files/characters.JSON","w") as characters_file:
    characters_file.write(json.dumps(characters_dict, sort_keys=True, indent = 4))
  
  with open("JSON files/locations.JSON","w") as locations_file:
    locations_file.write(json.dumps(locations_dict, sort_keys=True, indent = 4))
  
  with open("JSON files/episodes.JSON","w") as episodes_file:
    episodes_file.write(json.dumps(episodes_dict, sort_keys=True, indent = 4))

def readDictionaries():
  """
  Test function that reads JSON files created by storeDictionaries() back to dictionaries.
  (Do not use when testing API retrieval)
  Returns:
    characters_dict (dict): A dictionary containing all characters.
    locations_dict (dict): A dictionary containing all locations.
    episodes_dict (dict): A dictionary containing all episodes.
  """
  with open("JSON files/characters.JSON") as myFile:
    characters_dict = json.loads(myFile.read())
  with open("JSON files/locations.JSON") as myFile:
    locations_dict = json.loads(myFile.read())  
  with open("JSON files/episodes.JSON") as myFile:
    episodes_dict = json.loads(myFile.read())
  return characters_dict, locations_dict, episodes_dict