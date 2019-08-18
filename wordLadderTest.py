#wordLadderTest created by:
#Jake Attard s5138647
#Steven Phan s5080436

import unittest
import re
# import word_ladderOriginal

#DictionaryListFile Function
#Removed the fileName import so testing can be conducted.
def dictionaryListFile(fileName):
  try:
    # fileName = input("Enter dictionary file name: ")
    file = open(fileName)
  except:
    print("The dictionary file can't be found. Please check if you have the correct .txt file.")
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

#ExcludedFile Function
#Removed the fileName import so testing can be conducted on the excluded file
def excludedFile(fileName):
  try:
    # excludedFileInputted = input("Enter your excluded file name: ")
    file = open(fileName)
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

# TESTING DICTIONARY INPUT FILENAME
class TestInputtedFileName(unittest.TestCase):
    def testFileInvalid(self):
      self.assertRaises((SystemExit, FileNotFoundError), dictionaryListFile, "dictionaryFileTest")
    
    def testEmptyFileNameInput(self):
      self.assertRaises(SystemExit, dictionaryListFile, "")

# TESING EXCLUDED INPUT FILENAME
class TestInputtedExcludeFileName(unittest.TestCase):
    def testExcludeFileInvalid(self):
      self.assertRaises((SystemExit, FileNotFoundError), excludedFile, "excludedFileTest")
    
    def testEmptyExcludedFileNameInput(self):
      self.assertRaises(SystemExit, excludedFile, "")

if __name__ == '__main__':
    unittest.main()