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
    exit()
  
  fileLines = file.readlines()
  for fileLine in range(len(fileLines)):
    fileLines[fileLine] = fileLines[fileLine].strip()
    if fileLines[fileLine] == "":
      fileLines.pop(fileLine)
  if len(fileLines) == 0:
    print("The file is empty.")
    exit()
  return fileLines

# Same function
def same(item, target):
  return len([itemLetter for (itemLetter, targetLetter) in zip(item, target) if itemLetter == targetLetter])

#Build Function
def build(pattern, words, seen, potentialNextWords):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in potentialNextWords]

#Finding word function
def find(word, words, seen, target, path):
  potentialNextWords = []
  fixedIndexes=[i for i in range(len(word)) if word[i] == target[i]]
  for i in [index for index in range(len(word)) if index not in fixedIndexes]:
    potentialNextWords += build(word[:i] + "." + word[i + 1:], words, seen, potentialNextWords)
  if len(potentialNextWords) == 0:
    return False
  potentialNextWords = sorted([(same(word, target), word) for word in potentialNextWords], reverse=True)
  for (match, item) in potentialNextWords:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in potentialNextWords:
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
    print("Please type 'y' or 'n' ")
    continue
  if excludeWords == "y":
    excludeWords = dictionaryListFile()
    for word in excludeWords:
      startWord[word] = True
  break

#Start word
while True:
  start = checkUserInput("Enter start word: ").lower()
  if start not in dicionaryList:
    print("The dictionary word inputed can't be found")
    continue
  break
startWord[start] = True

#Target Word
while True:
  target = checkUserInput("Enter target word: ").lower()
  if start == target:
    print("The target word can not be the same as the start word!")
    continue
  elif len(target) != len(start):
    print("The target and start word must be the same length")
    continue
  elif target not in dicionaryList:
    print("The dictionary word inputed can't be found")
    continue
  break

# Check if this works
words = [word for word in dicionaryList if len(word) == len(start)]

shortestPath = True

if shortestPath:
  minPath = None

while True:
  path = [start]
  seen = startWord.copy()
  pathfound = find(start, words, seen, target, path)

  if pathfound and not shortestPath:
    path.append(target)
    print(len(path) -1, " >> ".join(path))
  elif shortestPath and pathfound:
    path.append(target)
    if pathfound and (minPath == None or len(path) -1 < len(minPath)):
      minPath = path
  elif not pathfound:
    if shortestPath:
      if minPath == None:
        print("No path 1 found")
        break
      print(len(minPath) - 1, " >> ".join(minPath))
    else:
      print("No path 2 found")
    break
  for word in path:
    startWord[word] = True