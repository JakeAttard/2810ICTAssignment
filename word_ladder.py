#word_ladder created by:
#Jake Attard s5138647
#Steven Phan s5080436

# Importing Regular Expressions
import re

#CheckUserInput Function
def checkUserInput(userInput = str(), checkInput =  bool(True)):
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

#DictionaryListFile Function
def dictionaryListFile():
  try:
    file = open(checkUserInput("Enter dictionary file: ", checkInput = bool(False)))
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
def build(pattern, words, seen, findingWords):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in findingWords]

#Finding word function
def find(word, words, seen, target, path):

  # Declaring findingWords as a list
  findingWords = list()
  fixedIndexes = [x for x in range(len(word)) if word[x] == target[x]]
  for x in [index for index in range(len(word)) if index not in fixedIndexes]:
    findingWords += build(word[:x] + "." + word[x + 1:], words, seen, findingWords)
  if len(findingWords) == 0:
    return False
  findingWords = sorted([(same(word, target), word) for word in findingWords], reverse=True)
  for (match, item) in findingWords:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in findingWords:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

dictionaryList = dictionaryListFile()

# Declaring startword as a dictionary
startWord = dict()

# Excluding words
while True:
  excludeWords = input("Do you want to exclude any words? (y / n) ").lower()
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
  if start not in dictionaryList:
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
  elif target not in dictionaryList:
    print("The dictionary word inputed can't be found")
    continue
  break

words = [word for word in dictionaryList if len(word) == len(start)]

wordPath = True

shortestWordPath = None

while True:
  path = [start]
  seen = startWord.copy()
  wordPathFound = find(start, words, seen, target, path)

  if wordPathFound and not wordPath:
    path.append(target)
    print(len(path) -1, "->".join(path))
  elif wordPath and wordPathFound:
    path.append(target)
    if wordPathFound and (shortestWordPath == None or len(path) -1 < len(shortestWordPath)):
      shortestWordPath = path
  elif not wordPathFound:
    if wordPath:
      if shortestWordPath == None:
        print("No path found")
        break
      print(len(shortestWordPath) - 1, "->".join(shortestWordPath))
    else:
      print("No path found")
    break
  for word in path:
    startWord[word] = True