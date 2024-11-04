from utils.PlayfairCipher import PlayfairCipher

def test_playfair_cipher():
    # Create an instance of the PlayfairCipher class
    # cipher = PlayfairCipher("First Amendment")
    cipher = PlayfairCipher("First Amendment", alphabet="AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ")

    # Test the encryption method
    message = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."
    message = "Acesta este un mesaj de test pentru cifrul Playfair care conȚine caractere speciale precum Ă, Â, Î, Ș, Ț."

    encrypted_message = cipher.playfair_encrypt(message)
    print(f"Encrypted message: {encrypted_message} \n")

    # Test the decryption method
    decrypted_message = cipher.playfair_decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message} \n")

if __name__ == "__main__":
    test_playfair_cipher()