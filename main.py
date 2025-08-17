#for handling api data
from apihandler import getAllPages, getDictionaries, storeDictionaries, readDictionaries
from searchhandler import fuzzySearchCharacter, searchCharacter, printMatches 


#Base url contains links to all APIs
url = "https://rickandmortyapi.com/api"

def fetchDictionaries():
  """
  Gets all data from rick and morty api and returns as dictionaries.
  Returns:
    characters_dict (dict): A dictionary containing all characters.
    locations_dict (dict): A dictionary containing all locations.
    episodes_dict (dict): A dictionary containing all episodes.
  """
  characters_dict, locations_dict, episodes_dict = getDictionaries(url)
  storeDictionaries(characters_dict,locations_dict,episodes_dict)
  return characters_dict, locations_dict, episodes_dict

def naiveSearch(searchTerm: str, characters_dict: dict):
  """
  Old search algorithm - prints searchList containing strings that searchTerm is substring
  Returns:
    None
  """
  searchList = searchCharacter(searchTerm,characters_dict)
  for items in range(0,len(searchList)):
    print(searchList[items]['name']+": "+str(searchList[items]['id']))

def main():
  pass

def test():
  
  characters_dict, locations_dict, episodes_dict = fetchDictionaries()

  #Collecting the dictionaries
  #characters_dict, locations_dict, episodes_dict = readDictionaries()
  
  #Conducting search on character name:
  searchTerm = input("Please enter the character you would like to find: ")
  exact_matches, partial_matches = fuzzySearchCharacter(searchTerm, characters_dict)
  
  #Sorting the matches by id:
  exact_matches = sorted(exact_matches, key = lambda x: x['id'])
  partial_matches = sorted(partial_matches, key = lambda x: x['id'])

  #print out search matches
  printMatches(exact_matches,partial_matches)

test()
main()