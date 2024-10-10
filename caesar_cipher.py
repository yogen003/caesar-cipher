def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char)+s - 65)% 26 + 65)
        else:
            result += chr((ord(char)+s - 97)% 26 + 97)
        
    return result

def decrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97)% 26 + 97)
        
    return result

p_text = input("Enter text for encryption : ")
s_value = int(input("Enter shifting value : "))
print("Plain Text  : "+ p_text)
print("Shift value : "+ str(s_value))
print("Cipher text : "+ encrypt(p_text,s_value)) # function calling
print("")
c_text = input("Enter text for decryption : ")
s2_value = int(input("Enter shifting value : "))
print("Cipher Text : "+ c_text)
print("Shift value : "+ str(s2_value))
print("Plain  text : "+ decrypt(c_text,s2_value)) # function calling