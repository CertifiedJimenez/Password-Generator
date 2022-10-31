# Password Gen
import json
import random

f = open('simple_english_dictionary.json')
Words = json.load(f)
fetchedWords = []



def GetWordLength(length,json):
    list = []
    for i in Words:
        if len(i) == length and not fetchedWords.count(i):
            list.append(i)
    return list

def SetNumbers(password,numbers):
    NewPassword = ''
    for index in range(numbers):
        randomIndex = random.randint(0,len(password)-1)
        NewPassword += password[0:randomIndex-1] + str(random.randint(0,10)) + password[randomIndex+1:len(password)]

    if NewPassword == '': NewPassword = password
    return NewPassword
        
                

def GeneratePassword(length,words,numbers,specialSymbols):
    wordRequirement = length / words # gets the word requirement
    wordList = GetWordLength(wordRequirement,Words)
    if len(wordList) == 0:
        Password = None
    else:
        Password = ''
        for index in range(words):
            Password += wordList[random.randint(0,len(wordList))] 
            if index != words-1: Password += specialSymbols # last Word
        Password = SetNumbers(Password,numbers)

    return Password


    
def __main__():
    """
        Main program
    """
    print(GeneratePassword( int(input('length: ')),
                            int(input('word count: ')),
                            int(input('numbers count: ')),
                            str(input('Special Keys in-between: '))))
    input()


__main__()
