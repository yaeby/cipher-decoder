class PlayfairCipher:
    def __init__(self, key: str, alphabet: str):
        self.alphabet = alphabet
        self.key = self._setKey(key)

    def _setKey(self, key: str) -> str:
        """
        Set the key for the Playfair cipher.
        """
        if len(self.alphabet) != 25:
            key = key.replace('Â', 'A').replace(' ', '').upper() + self.alphabet
        else:
            key = key.replace('J', 'I').replace(' ', '').upper() + self.alphabet
        key = "".join(dict.fromkeys(key))
        print(key)
        return key

    def _create_playfair_square(self) -> list:
        """
        Generate the Playfair square for the given phrase.
        """
        # if len(self.alphabet) != 25:
        #     key = self.key.replace('Â', 'A').replace(' ', '').upper() + self.alphabet
        # else:
        #     key = self.key.replace('J', 'I').replace(' ', '').upper() + self.alphabet

        # key = "".join(dict.fromkeys(key))

        rows = (len(self.key) + 4) // 5  
        grid = []
        for i in range(0, len(self.key), 5):
            row = self.key[i:i+5]
            # Pad the last row with empty spaces if needed
            while len(row) < 5:
                row += ' '
            grid.append([k for k in row])
        print(grid)
        return grid

    def _find_location(self, grid, char):
        """
        Helper function to get the row and column of the given char.
        """
        rows = len(grid)
        for i in range(rows):
            for j in range(5):  # Always 5 columns
                if grid[i][j] == char:
                    return i, j
        # If character not found, handle the error
        raise ValueError(f"Character {char} not found in the Playfair square")

    def playfair_encrypt(self, message: str) -> str:
        """
        Encrypt a message using the Playfair cipher.
        """
        playfair_square = self._create_playfair_square()
        ciphertext = ''

        # Remove non-alphabetic characters, but keep Romanian letters
        message = ''.join(c for c in message.upper() if c in self.alphabet)
        
        # Handle repeating letters by inserting 'X' between them
        i = 0
        while i < len(message) - 1:
            if message[i] == message[i+1]:
                message = message[:i+1] + 'X' + message[i+1:]
            i += 2
        
        # Append 'X' if the last block only contains a single character
        if len(message) % 2 == 1:
            message += 'X'

        # For each digraph, substitute the characters using the grid
        for i in range(0, len(message), 2):
            digraph = message[i:i+2]
            try:
                row1, col1 = self._find_location(playfair_square, digraph[0])
                row2, col2 = self._find_location(playfair_square, digraph[1])
                
                rows = len(playfair_square)
                if row1 == row2:
                    sub1 = playfair_square[row1][(col1 + 1) % 5]
                    sub2 = playfair_square[row2][(col2 + 1) % 5]
                elif col1 == col2:
                    sub1 = playfair_square[(row1 + 1) % rows][col1]
                    sub2 = playfair_square[(row2 + 1) % rows][col2]
                else:
                    sub1 = playfair_square[row1][col2]
                    sub2 = playfair_square[row2][col1]
                
                ciphertext += sub1 + sub2
            except ValueError as e:
                print(f"Warning: {str(e)}")
                ciphertext += digraph  # Keep original characters if not found

        return ciphertext

    def playfair_decrypt(self, ciphertext: str) -> str:
        """
        Decrypt a message using the Playfair cipher.
        """
        playfair_square = self._create_playfair_square()
        message = ''
        rows = len(playfair_square)

        # For each digraph, substitute the characters using the grid
        for i in range(0, len(ciphertext), 2):
            digraph = ciphertext[i:i+2]
            try:
                row1, col1 = self._find_location(playfair_square, digraph[0])
                row2, col2 = self._find_location(playfair_square, digraph[1])
                
                if row1 == row2:
                    sub1 = playfair_square[row1][(col1 - 1) % 5]
                    sub2 = playfair_square[row2][(col2 - 1) % 5]
                elif col1 == col2:
                    sub1 = playfair_square[(row1 - 1) % rows][col1]
                    sub2 = playfair_square[(row2 - 1) % rows][col2]
                else:
                    sub1 = playfair_square[row1][col2]
                    sub2 = playfair_square[row2][col1]
                
                message += sub1 + sub2
            except ValueError as e:
                print(f"Warning: {str(e)}")
                message += digraph  # Keep original characters if not found

        # Remove padding X's
        message = message.replace('X', '')
        return message