#word_ladder created by:
#Jake Attard s5138647
#Steven Phan s5080436

# Importing Regular Expressions
import re
import unittest
print("Welcome to the ladder-gram program!")

# Same function
# Original code from the word_ladder given just renamed variables from c and t to better naming conventions
def same(item, target):
  return len([itemWord for (itemWord, targetWord) in zip(item, target) if itemWord == targetWord])

# Build Function
# Original code from the word_ladder
def build(pattern, words, seen, findingWords):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in findingWords]

#Finding word function
# Has some original code from the word_ladder, some changes have been made to make the program more efficient and working as expected
def find(word, words, seen, target, path):

  # Declaring findingWords as a list
  findingWords = list()

  fixedIndexes = [x for x in range(len(word)) if word[x] == target[x]]
  for x in [index for index in range(len(word)) if index not in fixedIndexes]:
    findingWords += build(word[:x] + "." + word[x + 1:], words, seen, findingWords)
  if len(findingWords) == int(0):
    return bool(False)
  findingWords = sorted([(same(word, target), word) for word in findingWords], reverse = bool(True))
  # Loop puts items in the seen findingWords
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

#DictionaryListFile Function
def dictionaryListFile():
  try:
    dictionaryFileName = input("Enter dictionary file name: ")
    file = open(dictionaryFileName)
  except:
    print("The dictionary file can't be found. Please check if you have the correct .txt file.")
    exit("Please re-run the program and try again!")
  
  #Reads the dictionary file inputted bythe user and generates the words in a list of lines
  dictionaryFileLines = file.readlines()
  for dictionaryFileLine in range(len(dictionaryFileLines)):
    dictionaryFileLines[dictionaryFileLine] = dictionaryFileLines[dictionaryFileLine].strip()
    if dictionaryFileLines[dictionaryFileLine] == "":
      dictionaryFileLines.pop(dictionaryFileLine)
  if len(dictionaryFileLines) == int(0):
    print("The dictionary file you entered is empty.")
    exit("Please re-run the program and try again!")
  return dictionaryFileLines

# ExcludedFile function for the additional functionality
def excludedListFile():
  try:
    excludedFileName = input("Enter your excluded file name: ")
    file = open(excludedFileName)
  except:
    print("The excluded file can't be found. Please check if you have the correct .txt file.")
    exit("Please re-run the program and try again!")

  #Reads the excluded file inputted by the user and generates the words in a list of lines
  excludedFileLines = file.readlines()
  for excludedFileLine in range(len(excludedFileLines)):
    #strip is used to remove the character in the new line.
    excludedFileLines[excludedFileLine] = excludedFileLines[excludedFileLine].strip()
    if excludedFileLines[excludedFileLine] == "":
      excludedFileLines.pop(excludedFileLine)
  if len(excludedFileLines) == int(0):
    print("The excluded file you entered is empty.")
    exit("Please re-run the program and try again!")
  return excludedFileLines

# DictionaryList now has access to the dictionaryListFile() function
dictionaryList = dictionaryListFile()

# Declaring startword as a dictionary
startWord = dict()

#Main program while loop
while bool(True):
# Excluding words input
  while bool(True):
    excludeWords = input("Do you want to exclude any words? (y / n) ").lower()
    if excludeWords != "y" and excludeWords != "n":
      print("Please type either 'y' or 'n' ")
      continue
    if excludeWords == "y":
      excludeWords = input("Do you want to enter excluded words via file? Please type 'y'. If you want to enter words without a file please type 'n'. ").lower()
      if excludeWords == "y":
        excludedWords = excludedListFile()
        for word in excludedWords:
          startWord[word] = bool(True)
      elif excludeWords == "n":
        excludedWords = input("Please enter the words you would like to exclude in the same line with a space between each word: ")
        excludedWords = excludedWords.split()
        for word in excludedWords:
          startWord[word] = bool(True)
    break

  #Start word
  # While statement lets the user input their start word
  while bool(True):
    start = input("Enter start word: ").lower()
    if start not in dictionaryList:
      print("The dictionary word inputed can't be found")
      continue
    break
    
  startWord[start] = bool(True)

  #Target Word
  # While statement lets the user input their target word
  while bool(True):
    target = input("Enter target word: ").lower()
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
  # User can input their intermediate word
  while bool(True):
    intermediateWord = input("Please enter intermediate word, or hit enter to skip: ")
    if intermediateWord != "":
      path = [start]
      seen = startWord.copy()

      if find(start, words, seen, intermediateWord, path):
        path.append(intermediateWord)
        if find(intermediateWord, words, seen, target, path):
          path.append(target)
        print(len(path) - 1, "->".join(path))
        exit() 
      else:
        print("No path found")
        exit()
    else:
      break   

  # wordPath variable is equal to True
  wordPath = bool(True)

  # shortestWordPath is None
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
      break

    for word in path:
      startWord[word] = bool(True)

  #User able to restart and add another set of words without having to restart the program again!
  inputAnotherWordSet = input("Would you like to input another set of words? Please type 'y' or hit any other keyboard input to exit: ")
  if inputAnotherWordSet == "y":
    continue
  else:
    break

#Goodbye message for when the user quits.
print("Thankyou for using ladder-gram. Please re-run the program to start again!")