import numpy

#Set up the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Creata a martrix that we want to use as they key for our encoding, we will use 2X2 smatrix for now
encodingMatrix = np.array([2,5],[7,8])

#Now we need to create the message we want to encode, we would get user input, put all lower and remove spaces. Will need to be multiple
#of two for now to ease of use. Later create way to do any length with padding
message = "attackatdawn"

#Split message into arrays of two letters and perform encoding
for (first, second) in zip(message[0::2], message[1::2]):
    print first, second
  


