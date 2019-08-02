# Regular Expressions
import re

def checkUserInput(userInput = "", checkInput = True):
  inputText = None
  while True:
    inputText = input(userInput)
    if len(inputText) == 0:
      print("The input cannot be empty.")
      continue
    elif not inputText.isalpha() and checkInput:
      print("Error")
      continue
    break
  return inputText

def dictionaryListFile():
  try:
    file = open(checkUserInput("Enter dictionary file: ", checkInput = False))
  except:
    print("The dictionary file provided does not exist.")
    exit(0) ### Test with no 0
  
  fileLines = file.readlines()
  for fileLine in range(len(fileLines)):
    fileLines[fileLine] = fileLines[fileLine].strip()
    if fileLines[fileLine] == "":
      fileLines.pop(fileLine)
  if len(fileLines) == 0:
    print("The file is empty.")
    exit(0)
  return fileLines

# Same function
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

#Build Function
def build(pattern, words, seen, list):
  return [word for word in words 
    if re.search(pattern, word) and word not in seen.keys() and word not in list]

#Finding word function
def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

dicionaryList = dictionaryListFile()
startWord = {}

# Excluding words
while True:
  excludeWords = input("Do you want to exclude any words? Please type Y to continue and N to skip. ").lower()
  if excludeWords != "y" and excludeWords != "n":
    print("Please type 'Y' or 'N' ")
    continue
  if excludeWords == "y":
    excludeWords = dictionaryListFile()
    for word in excludeWords:
      startWord[word] = True
  break

