#wordLadderTest created by:
#Jake Attard s5138647
#Steven Phan s5080436

import unittest
import re

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

if __name__ == '__main__':
    unittest.main()