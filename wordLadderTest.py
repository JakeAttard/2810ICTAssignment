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

# ExcludedFile function for the additional functionality
def excludedFile(testingExcludedFileName):
  try:
    file = open(testingExcludedFileName)
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
# Original code from the word_ladder given just renamed variables from c and t to better naming conventions
def same(item, target):
  return len([itemLetter for (itemLetter, targetLetter) in zip(item, target) if itemLetter == targetLetter])

# Build Function
# Original code from the word_ladder just renamed variables to have cleaer easier naming conventions
def build(pattern, words, seen, findingWords):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in findingWords]

# TESTING INPUT FILENAME
class TestInputtedFileName(unittest.TestCase):
    def testFileInvalid(self):
      self.assertRaises((SystemExit, FileNotFoundError), dictionaryListFile, "dictionaryFileTest")
    
    def testEmptyFileNameInput(self):
      self.assertRaises(SystemExit, dictionaryListFile, "")

# TESING EXCLUDED FILENAME
class TestInputtedExcludeFileName(unittest.TestCase):
    def testExcludeFileInvalid(self):
      self.assertRaises((SystemExit, FileNotFoundError), excludedFile, "excludedFileTest")
    
    def testEmptyExcludedFileNameInput(self):
      self.assertRaises(SystemExit, excludedFile, "")

class TestInputtedWord(unittest.TestCase):
    def testInputtedSpecialCharacters(self):
        self.assertEqual(checkUserInput('@#test'), "Error no special characters such as @!#%$ can be inputted")

    def testInputtedNumbers(self):
        self.assertEqual(checkUserInput('123TEST'), "Error no numbers can be inputted.")

    def testInputtedSpaces(self):
        self.assertEqual(checkUserInput(' '), "Error no spaces can be inputted.")

    def testCorrectInput(self):
        self.assertEqual(checkUserInput('test'), 'The current input is successful.')

class TestSameFunctionComparingWords(unittest.TestCase):
    def testWordsString1(self):
      self.assertEqual(same("lead", "gold"), 1)

    def testWordsString2(self):
      self.assertEqual(same("hide", "seek"), 0)

    def testWordsString3(self):
      self.assertEqual(same("lead", "lead"), 4)

    def testWordsEmptyString(self):
      self.assertEqual(same("", ""), 0)

if __name__ == '__main__':
    unittest.main()