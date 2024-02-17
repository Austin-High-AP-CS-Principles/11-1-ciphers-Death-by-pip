import string, random
# print(string.ascii_letters)

# CAESAR CIPHER
def caesar_encrypt(text, key):
    encrypted = ""
    for char in text:
        if char in string.ascii_lowercase:
            encrypted += string.ascii_lowercase[(string.ascii_lowercase.find(char)+key)%26]
        elif char in string.ascii_uppercase:
            encrypted += string.ascii_uppercase[(string.ascii_uppercase.find(char)+key)%26]
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(encrypted, key):
    decrypted = ""
    for char in encrypted:
        if char in string.ascii_lowercase:
            decrypted += string.ascii_lowercase[(string.ascii_lowercase.find(char)-key)%26]
        elif char in string.ascii_uppercase:
            decrypted += string.ascii_uppercase[(string.ascii_uppercase.find(char)-key)%26]
        else:
            decrypted += char
    return decrypted



# VIGENERE CIPHER
def vigenere_encrypt(text, keyword):
    encrypted = ""
    for n, char in enumerate(text):
        key = string.ascii_uppercase.find(keyword[n%len(keyword)])
        # print(n,key,char)
        if char in string.ascii_lowercase:
            encrypted += string.ascii_lowercase[(string.ascii_lowercase.find(char)+key)%26]
        elif char in string.ascii_uppercase:
            encrypted += string.ascii_uppercase[(string.ascii_uppercase.find(char)+key)%26]
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(encrypted, keyword):
    decrypted = ""
    for n, char in enumerate(encrypted):
        key = string.ascii_uppercase.find(keyword[n%len(keyword)])
        # print(n,key,char)
        if char in string.ascii_lowercase:
            decrypted += string.ascii_lowercase[(string.ascii_lowercase.find(char)-key)%26]
        elif char in string.ascii_uppercase:
            decrypted += string.ascii_uppercase[(string.ascii_uppercase.find(char)-key)%26]
        else:
            decrypted += char
    return decrypted

try:
    key = int(input("Caesar key: "))
except:
    key = random.randint(0,25)
print("Caesar key =",key)
text = input("Caesar code text to encrypt: ")
print("encrypted = "+caesar_encrypt(text, key))
print("decrypted = "+caesar_decrypt(caesar_encrypt(text, key), key))


while True:
    key = input("Vigenere keyword: ")
    key = key.upper()
    check = True
    if len(key)<=0:
        print("Must enter a key")
        continue
    for char in key:
        if not char in string.ascii_uppercase:
            check = False
            break
    # print(key)
    if check:
        break
    else:
        print("Only include letters")
print("Vigenere keyword =",key)
text = input("Vigenere code text to encrypt: ")
print("encrypted = "+vigenere_encrypt(text, key))
print("decrypted = "+vigenere_decrypt(vigenere_encrypt(text, key), key))