SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def getMode():
    while True:
        mode = input("Do you wish to encrypt or decrypt a message? ").lower()
        if mode == "encrypt" or "decrypt":
            return mode
        else:
            print("Please input encrypt or decrypt.")

def getMessage():
    return input("Enter your message: ")

def getKey():
    while True:
        key = int(input("Enter the key number (1-52) "))
        if (key < 53) or (key > 0):
            return key
        else:
            print("Please enter a valid number.")

def getTranslatedMessage(mode, message, key):
    newMessage = ""
    if mode == "encrypt":
        for i in message:
            symbol = SYMBOLS.find(i) + key
            if symbol != SYMBOLS:
                message += i
            else:
                newMessage += SYMBOLS.find(symbol)
    else:
        key = -key
        for i in message:
            symbol = SYMBOLS.find(i) + key
            if symbol != SYMBOLS:
                message += i
            else:
                newMessage += SYMBOLS.find(symbol)
    return newMessage

print(getTranslatedMessage(getMode(), getMessage(), getKey()))