"""
Handles searching of the dict database. 
Functions:
  
  searchCharacter(str, dict) -> list
  fuzzySearchCharacter(str, dict) -> list
  printMatches(list, list)

Misc variables:

  None

Classes:
  
  None
"""

#Imports for fuzzy search
from thefuzz import fuzz

#Functions:
def searchCharacter(character_name: str, characters_dict: dict):
  """
  Searches for a character in the character dictionary and returns their individual character dictionary.
  Args:
    character_name (str): Name of the character to search.
    character_dict (dict): The dictionary of characters.
  Returns:
    matches (list): A list containing dictionaries of the matched characters and their attributes.
  """

  characters_list = characters_dict['results']
  matches = []
  for person in characters_list:
    if character_name.lower() in person['name'].lower():
      matches.append(person)
  if len(matches) == 0:
    raise Exception("No matches found!")
  else:
    return matches

def fuzzySearchCharacter(character_name:str, characters_dict: dict, exact_match_strictness: int = 100, fuzzy_match_strictness: int = 80):
  """
  Completes fuzzy search for a character and their attributes in a dictionary.
  Args:
    character_name (str): Name of the character to search.
    character_dict (dict): The dictionary of characters.
  **Optional Args:**
    exact_match_strictness (int): tolerance of the exact match function
    fuzzy_match_strictness (int): tolerance of the fuzzy match function
  Returns:
    exact_matches (list): List containing the exact matches.
    partial_matches (list): List containing the partial matches.
  """
  character_name = character_name.lower()
  characters_list = characters_dict['results']
  
  exact_matches = []
  partial_matches = []
  
  #Loops through dictionary to search individual characters
  for character_dictionary in characters_list:
    name_to_check = character_dictionary['name'].lower()
    #Computing fuzzy search of term in character dictionary
    if fuzz.ratio(character_name, name_to_check) >= exact_match_strictness:
      exact_matches.append(character_dictionary)
    elif fuzz.token_set_ratio(character_name, name_to_check) >= fuzzy_match_strictness:
      partial_matches.append(character_dictionary)
  
  if len(partial_matches) == 0 and len(exact_matches) == 0:
    return exact_matches, partial_matches
    #raise Exception("No matches found!")
  else:
    return exact_matches, partial_matches 

def printMatches(exact_matches: list, partial_matches: list):
  """
  Prints matches found during a fuzzy search.
  Args:
    exact_matches (list): List containing the dictionaries of exact search character matches.
    partial_matches (list): List containing the dictionaries of partial search character matches.
  """
  
  if len(exact_matches) == 0 and len(partial_matches) == 0:
    print("No matches found!")
    return

  #Checking the exact matches
  if len(exact_matches) == 0:
    print("No exact matches found!")
  else:
    print("Exact Matches: ", end = "")
    for items in exact_matches:
      print(f"{items['name']}: {items['id']}", end =", ")
    print("")
  
  #Checking the partial matches
  if len(partial_matches) == 0:
    print("No partial matches found!")
  else:
    print("Partial Matches: ", end = "")
    for items in partial_matches:
      print(f"{items['name']}: {items['id']}", end =", ")
    print("")
