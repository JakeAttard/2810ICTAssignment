import unittest
import re

#CheckUserInput Function
def checkUserInput(emptyString, checkInput =  bool(True)):
    inputText = None
    while True:
      inputText = emptyString
      if len(inputText) == 0:
        print("The input cannot be empty.")
        # Added a exit instead of the continue as the testing continued to loop over "The input cannot be empty"
        exit()
      elif not inputText.isalpha() and checkInput:
        print("Error")
      break
    return inputText

#DictionaryListFile Function
def dictionaryListFile(testingFileName):
    try:
      file = open(testingFileName)
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

class MyTestCase(unittest.TestCase):
    def testFileInvalid(self):
      self.assertRaises((SystemExit, FileNotFoundError), dictionaryListFile, 'dictionaryFileTest')
    
    def testEmptyFileNameInput(self):
      self.assertRaises(SystemExit, checkUserInput, "")


if __name__ == '__main__':
    unittest.main()