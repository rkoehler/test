#Author: Robert Koehler
#Date 5/10/16

#New Project
#input
#make a simple shifting cipher

#save File, and pick up and read File.

#take a string and flip positions of the first and last letters. So on and so forth....

def shiftLetter (letter, shift):
    baseValue = ord(letter)
    shiftedValue = baseValue + shift
    newString = chr(shiftedValue)
    return newString

if __name__ == "__main__":

    firstInput = input('Please give me a string: ')
    shiftNumber = int(input('How many spaces would you like to shift?: '))

def shiftString(firstInput,)
    theMessage = list(firstInput)
    collector = []
    for index in range(len(theMessage)):
        shiftedValue =  shiftLetter(theMessage[index], shiftNumber)
        collector.append(shiftedValue)
    result = ''.join(collector)


    print(result)










