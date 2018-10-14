import numpy as np

### ENCODING ###

def encryptPassage(message, alphabet):

    encodedMessage = []

    #Split message into arrays of two letters and perform encoding
    for (first, second) in zip(message[0::2], message[1::2]):
        array = [alphabet.index(first),alphabet.index(second)]
        dotProduct = encodingMatrix.dot(np.array(array))
        modDot = dotProduct%len(alphabet)
        encodedMessage.append(alphabet[modDot[0]])
        encodedMessage.append(alphabet[modDot[1]])

    print(encodedMessage)
    return encodedMessage


### Get modulo reciprocals ###

def getModuloRecip(alphabet):

    recipModuloDict = {}

    length = len(alphabet)

    for x in range(0,length):
        for y in range(0, length):
            number = x*y
            if number % length == 1:
                recipModuloDict[x] = y
            continue
        continue

    return recipModuloDict

### DECODING ###

def decryptPassage(message, encodingMatrix, alphabet):
    
    #Find the determinate of the enciphering matrix basic method
    #determinate1 = encodingMatrix[0][0]*encodingMatrix[1][1]
    #determinate2 = encodingMatrix[0][1]*encodingMatrix[1][0]
    #determinateFinal = determinate1-determinate2

    #Find the determinate using Numpy, this is a modification of the above commented out code. Just quicker and easier way.
    determinateFinal = round(np.linalg.det(encodingMatrix))
    print(determinateFinal)

    #recipModuloDict = {
    #    1:1,
    #    3:9,
    #    5:21,
    #    7:15,
    #    9:3,
    #    11:19,
    #    15:7,
    #    17:23,
    #    19:11,
    #    21:5,
    #    23:17,
    #    25:25,
    #}

    # This now uses my custom getModuloRecip function. Very big improvement in that it allows for any size alphabet
    recipModuloDict = getModuloRecip(alphabet)
    print(recipModuloDict)

    repModuloValue = recipModuloDict[abs(determinateFinal)]
    print(determinateFinal**-1%len(alphabet))

    newMatrix = np.array([[repModuloValue*encodingMatrix[1][1],
                        -repModuloValue*encodingMatrix[0][1]],
                        [-repModuloValue*encodingMatrix[1][0],
                        repModuloValue*encodingMatrix[0][0]]])

    newMatrixMod26 = [[newMatrix[0][0]%len(alphabet),
                    newMatrix[0][1]%len(alphabet)],
                    [newMatrix[1][0]%len(alphabet),
                    newMatrix[1][1]%len(alphabet)]]

    #Split the encoded message into arrays of two letters

    decodedMessage = []

    for (first, second) in zip(message[0::2], message[1::2]):
        multiplied = np.array(newMatrixMod26).dot(np.array([alphabet.index(first), alphabet.index(second)]))
        multipliedMod = multiplied%len(alphabet)
        decodedMessage.append(alphabet[multipliedMod[0]])
        decodedMessage.append(alphabet[multipliedMod[1]])

    print(decodedMessage)
    return decodedMessage



#Creata a martrix that we want to use as they key for our encoding, we will use 2X2 smatrix for now
encodingMatrix = np.array([[5, 5], [3, 8]])

#Set up the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '?', ' ']

choiceOfRun = ''

while choiceOfRun != "A" or "B" or "Q":

    choiceOfRun = input("Do you want to: A) Encrypt a passage. B) Decrypt a passage. Q) Quit program [A/B/Q]?").upper()
    
    if choiceOfRun == "A":

        # Encryption
        passageInput = input("Enter passage you wish to encrypt: ")
        passageInput = passageInput.lower()

        encryptedPassage = encryptPassage(passageInput, alphabet)

        encryptedPassageString = ''.join(encryptedPassage)

        print("Your encrypted passage is: " + encryptedPassageString)

        choiceOfRun = ''

        continue
     
    if choiceOfRun == "B":
            
        # Decryption
        encryptedPassageInput = input("Enter passage you wish to decrypt: ")
        encryptedPassageInput = encryptedPassageInput.lower()

        decryptedPassage = decryptPassage(encryptedPassageInput, encodingMatrix, alphabet)

        decryptedPassageString = ''.join(decryptedPassage)

        print("Your decrypted passage is: " + decryptedPassageString)

        choiceOfRun = ''

        continue

    if choiceOfRun == "Q":
        break
