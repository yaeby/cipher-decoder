import pandas as pd

class VigenereCipher:
    def __init__(self, key: str):
        self.key = key.upper()

    def __generate_key(self, msg) -> str:
        """Generates the full key for Vigenère cipher."""
        key = list(self.key)
        if len(msg) == len(key):
            return key
        else:
            for i in range(len(msg) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    def encrypt(self, msg) -> str:
        """Encrypts a message using Vigenère cipher."""
        encrypted_text = []
        key = self.__generate_key(msg)
        for i in range(len(msg)):
            char = msg[i]
            if char.isupper():
                encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
            elif char.islower():
                encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
            else:
                encrypted_char = char
            encrypted_text.append(encrypted_char)
        return "".join(encrypted_text)

    def decrypt(self, msg) -> str:
        """Decrypts a message using Vigenère cipher."""
        decrypted_text = []
        key = self.__generate_key(msg)
        for i in range(len(msg)):
            char = msg[i]
            if char.isupper():
                decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
            elif char.islower():
                decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
            else:
                decrypted_char = char
            decrypted_text.append(decrypted_char)
        return "".join(decrypted_text)
    
    def generate_tabula_recta(self):
        """Generates a Tabula Recta for Vigenère cipher."""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tabula_recta = []
        for i in range(len(alphabet)):
            row = alphabet[i:] + alphabet[:i]
            tabula_recta.append(list(row))
        return pd.DataFrame(tabula_recta, columns=list(alphabet), index=list(alphabet))