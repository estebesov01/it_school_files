class Cipher:
    def __init__(self, text):
        self.text = text

    def decrypt(self,text):
        result = ""
        # traverse text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - 7))
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - 7))
        return result


    def encrypt(self):
        result = ""
    # traverse text
        for i in range(len(self.text)):
            char = self.text[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + 7))
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + 7))
        return result

    def __str__(self):
        cipherText = self.encrypt()
        return f'Исходный текст:{self.text}\nТекст после шифровки:{cipherText}\nДешифрованный текст:{self.decrypt(cipherText)} '
text = input('Введите текст: ')
obj = Cipher(text)
print(str(obj))