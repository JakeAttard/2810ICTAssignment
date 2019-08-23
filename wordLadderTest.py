#wordLadderTest created by:
#Jake Attard s5138647
#Steven Phan s5080436

import unittest
import re

def same(item, target):
  return len([itemWord for (itemWord, targetWord) in zip(item, target) if itemWord == targetWord])

def build(pattern, words, seen, findingWords):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in findingWords]

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

#DictionaryListFile Function
#Removed the fileName import so testing can be conducted.
def dictionaryListFile(dictFileName):
  try:
    # dictionaryFileName = input("Enter dictionary file name: ")
    file = open(dictFileName)
  except:
    print("The dictionary file can't be found. Please check if you have the correct .txt file.")
    exit("Please re-run the program and try again!")
    
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
#Removed the fileName import so testing can be conducted.
def excludedListFile(excFileName):
  try:
    # excludedFileName = input("Enter your excluded file name: ")
    file = open(excFileName)
  except:
    print("The excluded file can't be found. Please check if you have the correct .txt file.")
    exit("Please re-run the program and try again!")

  excludedFileLines = file.readlines()
  for excludedFileLine in range(len(excludedFileLines)):
    excludedFileLines[excludedFileLine] = excludedFileLines[excludedFileLine].strip()
    if excludedFileLines[excludedFileLine] == "":
      excludedFileLines.pop(excludedFileLine)
  if len(excludedFileLines) == int(0):
    print("The excluded file you entered is empty.")
    exit("Please re-run the program and try again!")
  return excludedFileLines

# TESTING DICTIONARY INPUT FILENAME
class TestInputtedFileName(unittest.TestCase):
    def testFileInvalid(self):
      self.assertRaises((SystemExit, FileNotFoundError), dictionaryListFile, "dictionaryFileTest")
    
    def testEmptyFileNameInput(self):
      self.assertRaises(SystemExit, dictionaryListFile, "")

# TESING EXCLUDED INPUT FILENAME
class TestInputtedExcludeFileName(unittest.TestCase):
    def testExcludeFileInvalid(self):
      self.assertRaises((SystemExit, FileNotFoundError), excludedListFile, "excludedFileTest")
    
    def testEmptyExcludedFileNameInput(self):
      self.assertRaises(SystemExit, excludedListFile, "")

class TestSameFunction(unittest.TestCase):
  def testSameFuncSuccess1(self):
    self.assertEqual(same('lead', 'gold'), 1)
  
  def testSameFuncSuccess2(self):
    self.assertEqual(same('hide', 'seek'), 0)
    self.assertEqual(same('goal', 'load'), 2)
    
  def testSameFunUnsuccessful1(self):
    self.assertFalse(same('bike', 'car'))
  
  def testSameFunUnsuccessful2(self):
    self.assertFalse(same('truck', 'run'))

class TestBuildFunction(unittest.TestCase):
  def testBuildFuncSuccess1(self):
    words = ['hide', 'side', 'site', 'sits', 'sies', 'sees', 'seek']
    seen = {"site": True}
    list = []
    self.assertEqual(build(".ide", words, seen, list), ['hide','side'])
  
  def testBuildFuncUnSuccess1(self):
    words = ['hide', 'side', 'site', 'sits', 'sies', 'sees', 'seek']
    seen = {"test": True}
    list = []
    self.assertFalse(build(".est", words, seen, list))

if __name__ == '__main__':
    unittest.main()