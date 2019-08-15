#word_ladder created by:
#Jake Attard s5138647
#Steven Phan s5080436

# Importing Regular Expressions
import re

#CheckUserInput Function
def checkUserInput(userInput = str(), checkInput =  bool(True)):
  inputText = None
  while bool(True):
    inputText = input(userInput)
    if len(inputText) == int(0):
      print("The input cannot be empty.")
      continue
    break
  return inputText

#DictionaryListFile Function
def dictionaryListFile():
  try:
    file = open(checkUserInput("Enter dictionary file: ", checkInput = bool(False)))
  except:
    print("The dictionary file provided does not exist.")
    exit("Please re-run the program and try again!")
  
  fileLines = file.readlines()
  for fileLine in range(len(fileLines)):
    fileLines[fileLine] = fileLines[fileLine].strip()
    if fileLines[fileLine] == "":
      fileLines.pop(fileLine)
  if len(fileLines) == int(0):
    print("The file you entered is empty.")
    exit("Please re-run the program and try again!")
  return fileLines

# ExcludedFile function
def excludedFile():
  try:
    file = open(checkUserInput("Enter your excluded file: ", checkInput = bool(False)))
  except:
    print("The excluded file provided does not exist.")
    exit("Please re-run the program and try again!")

  excludedFileLines = file.readlines()
  for excludedFileLine in range(len(excludedFileLines)):
    excludedFileLines[excludedFileLine] = excludedFileLines[excludedFileLine].strip()
    if excludedFileLines[excludedFileLine] == "":
      excludedFileLines.pop(excludedFileLine)
  if len(excludedFileLines) == int(0):
    print("The file is empty.")
    exit("Please re-run the program and try again!")
  return excludedFileLines
  
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
  if len(findingWords) == int(0):
    return bool(False)
  findingWords = sorted([(same(word, target), word) for word in findingWords], reverse = bool(True))
  for (match, item) in findingWords:
    if match >= len(target) - int(1):
      if match == len(target) - int(1):
        path.append(item)
      return bool(True)
    seen[item] = bool(True)
  for (match, item) in findingWords:
    path.append(item)
    if find(item, words, seen, target, path):
      return bool(True)
    path.pop()

dictionaryList = dictionaryListFile()

# Declaring startword as a dictionary
startWord = dict()

# Excluding words input
while bool(True):
  excludeWords = input("Do you want to exclude any words? (y / n) ").lower()
  if excludeWords != "y" and excludeWords != "n":
    print("Please type either 'y' or 'n' ")
    continue
  if excludeWords == "y":
    excludedWords = excludedFile()
    for word in excludedWords:
      startWord[word] = bool(True)
  break

#Start word
while bool(True):
  start = checkUserInput("Enter start word: ").lower()
  if start not in dictionaryList:
    print("The dictionary word inputed can't be found")
    continue
  break
startWord[start] = bool(True)

#Target Word
while bool(True):
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

wordPath = bool(True)

shortestWordPath = None

while bool(True):
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
        print("No path found, please try again")
        break
      print(len(shortestWordPath) - 1, "->".join(shortestWordPath))
    # else:
    #   print("No path found")
    break

  for word in path:
    startWord[word] = bool(True)