print('''

  _    _   ___   ____    ____  _____     ____   ___   ____   _____ 
| \  / | / _ \ |  _ \  / ___||  ___|   /  __| / _ \ |  _ \ |  ___|
|  \/  || | | || |_| || |__  | |___   |  /   | | | || | | || |___ 
|      || | | ||    /  \__ \ |  ___|  | |    | | | || | | ||  ___|
| |\/| || | | || |\ \     | || |      | |    | | | || | | || |    
| |  | || |_| || | | | ___| || |___   |  \__ | |_| || |_| || |___ 
|_|  |_| \___/ |_| |_||____/ |_____|   \____| \___/ |____/ |_____|

****** Tool Name ::Play with Morse Code ******
       Why This tool :: This tool Is Made for Encrypted and Decrypted Plain text to Morse Code
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 
    


''')



morsecode = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '.----',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.'
}


def encryptor(text):
    encryptedtext = ""
    for letters in text:
        if letters != " ":
            encryptedtext = encryptedtext + morsecode.get(letters) + " "
        else:
            encryptedtext = encryptedtext + " "


    print(encryptedtext)    



def decryptor(text):
    text = text + " "

    key = list(morsecode.keys())
    val = list(morsecode.values())
    morse = ""
    normal = ""
    for letters in text:
        if letters != " ":
            morse = morse + letters
            spacefound = 0

        else:
            spacefound = spacefound + 1
            if spacefound == 2:
                normal = normal + ""
            else:
                normal = normal + key[val.index(morse)]
                morse = ""
    print(normal)




print("\n\n\n\t\tMorse Code Genarator")
ch = input("Press 'E' to Encrypted Or 'D' to Decypted :")
if ch == 'E' or ch == 'e':
    texttoencrypted = input("Enter Some Text to Encrypt :").upper()
    encryptor(texttoencrypted)
else :
    texttodecrypted = input("Enter Morse code to Decrypt :")
    decryptor(texttodecrypted)    


