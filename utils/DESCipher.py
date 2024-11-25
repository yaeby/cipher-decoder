class DESCipher:
    def __init__(self, key='abcdefgh'):
        if len(key) != 8:
            raise ValueError("Key must be exactly 8 characters long")
        
        self.key = key
        self.ip_table = [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
        ]
        
        self.pc1_table = [
            57, 49, 41, 33, 25, 17, 9, 1,
            58, 50, 42, 34, 26, 18, 10, 2,
            59, 51, 43, 35, 27, 19, 11, 3,
            60, 52, 44, 36, 63, 55, 47, 39,
            31, 23, 15, 7, 62, 54, 46, 38,
            30, 22, 14, 6, 61, 53, 45, 37,
            29, 21, 13, 5, 28, 20, 12, 4
        ]
        
        self.shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        
        self.pc2_table = [
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32
        ]
        
        self.e_box_table = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        ]
        
        self.s_boxes = [
            [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
            ],
            # S-box 2
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
            ],
            # S-box 3
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
            ],
            # S-box 4
            [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
            ],
            # S-box 5
            [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
            ],
            # S-box 6
            [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
            ],
            # S-box 7
            [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
            ],
            # S-box 8
            [
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
            ]
        ]
        
        self.p_box_table = [
            16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25
        ]
        
        self.ip_inverse_table = [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
        ]

    def str_to_bin(self, user_input):
        """Convert string to 64-bit binary representation"""
        binary_representation = ''
        
        for char in user_input:
            binary_char = format(ord(char), '08b')
            binary_representation += binary_char
            binary_representation = binary_representation[:64]
        
        # Pad or truncate the binary representation to 64 bits
        binary_representation = binary_representation[:64].ljust(64, '0')
        return binary_representation

    def binary_to_ascii(self, binary_str):
        """Convert binary string to ASCII"""
        ascii_str = ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])
        return ascii_str

    def generate_round_keys(self):
        """Generate round keys"""
        # Convert key to binary
        binary_representation_key = self.str_to_bin(self.key)
        
        # Similar key generation logic from original script
        # This is a simplified version and should match the original implementation
        pc1_key_str = ''.join(binary_representation_key[bit - 1] for bit in self.pc1_table)
        
        c0 = pc1_key_str[:28]
        d0 = pc1_key_str[28:]
        round_keys = []
        
        for round_num in range(16):
            # Left circular shift
            c0 = c0[self.shift_schedule[round_num]:] + c0[:self.shift_schedule[round_num]]
            d0 = d0[self.shift_schedule[round_num]:] + d0[:self.shift_schedule[round_num]]
            
            # Concatenate and apply PC2
            cd_concatenated = c0 + d0
            round_key = ''.join(cd_concatenated[bit - 1] for bit in self.pc2_table)
            
            round_keys.append(round_key)
        
        return round_keys

    def encrypt(self, plaintext):
        """Encrypt the plaintext and return encryption details"""
        # Encryption details dictionary to track round-by-round information
        encryption_details = {
            'rounds': [],
            'final_cipher_binary': '',
            'final_cipher_text': ''
        }
        
        # Convert plaintext to binary
        binary_rep_of_input = self.str_to_bin(plaintext)
        
        # Generate round keys
        round_keys = self.generate_round_keys()
        
        # Initial Permutation
        ip_result_str = ''.join(binary_rep_of_input[bit - 1] for bit in self.ip_table)
        
        # Split into left and right parts
        lpt = ip_result_str[:32]
        rpt = ip_result_str[32:]
        
        # Perform 16 rounds of encryption
        for round_num in range(16):
            round_info = {
                'round': round_num + 1,
                'lpt': lpt,
                'rpt': rpt,
                'round_key': round_keys[round_num]
            }
            
            # Expansion
            expanded_result = ''.join([rpt[i - 1] for i in self.e_box_table])
            
            # XOR with round key
            xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(expanded_result, round_keys[round_num]))
            
            # S-box substitution
            s_box_substituted = self._apply_s_boxes(xor_result)
            
            # P-box permutation
            p_box_result = ''.join([s_box_substituted[i - 1] for i in self.p_box_table])
            
            # XOR with LPT
            new_rpt = ''.join(str(int(a) ^ int(b)) for a, b in zip(lpt, p_box_result))
            
            # Update LPT and RPT
            lpt, rpt = rpt, new_rpt
            
            # Store round information
            round_info['expanded_result'] = expanded_result
            round_info['xor_result'] = xor_result
            round_info['s_box_substituted'] = s_box_substituted
            round_info['p_box_result'] = p_box_result
            round_info['new_rpt'] = rpt
            
            encryption_details['rounds'].append(round_info)
        
        # Final swap and inverse initial permutation
        final_result = rpt + lpt
        final_cipher = ''.join([final_result[self.ip_inverse_table[i] - 1] for i in range(64)])
        
        encryption_details['final_cipher_binary'] = final_cipher
        encryption_details['final_cipher_text'] = self.binary_to_ascii(final_cipher)
        
        return encryption_details

    def decrypt(self, ciphertext):
        """Decrypt the ciphertext and return decryption details"""
        # Decryption details dictionary to track round-by-round information
        decryption_details = {
            'rounds': [],
            'final_plaintext_binary': '',
            'final_plaintext': ''
        }
        
        # Convert ciphertext to binary
        binary_cipher = self.str_to_bin(ciphertext)
        
        # Generate round keys
        round_keys = self.generate_round_keys()
        
        # Initial Permutation
        ip_dec_result_str = ''.join(binary_cipher[bit - 1] for bit in self.ip_table)
        
        # Split into left and right parts
        lpt = ip_dec_result_str[:32]
        rpt = ip_dec_result_str[32:]
        
        # Perform 16 rounds of decryption (using keys in reverse order)
        for round_num in range(16):
            round_info = {
                'round': round_num + 1,
                'lpt': lpt,
                'rpt': rpt,
                'round_key': round_keys[15 - round_num]
            }
            
            # Expansion
            expanded_result = ''.join([rpt[i - 1] for i in self.e_box_table])
            
            # XOR with round key
            xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(expanded_result, round_keys[15 - round_num]))
            
            # S-box substitution
            s_box_substituted = self._apply_s_boxes(xor_result)
            
            # P-box permutation
            p_box_result = ''.join([s_box_substituted[i - 1] for i in self.p_box_table])
            
            # XOR with LPT
            new_rpt = ''.join(str(int(a) ^ int(b)) for a, b in zip(lpt, p_box_result))
            
            # Update LPT and RPT
            lpt, rpt = rpt, new_rpt
            
            # Store round information
            round_info['expanded_result'] = expanded_result
            round_info['xor_result'] = xor_result
            round_info['s_box_substituted'] = s_box_substituted
            round_info['p_box_result'] = p_box_result
            round_info['new_rpt'] = rpt
            
            decryption_details['rounds'].append(round_info)
        
        # Final swap and inverse initial permutation
        final_result = rpt + lpt
        final_plaintext = ''.join([final_result[self.ip_inverse_table[i] - 1] for i in range(64)])
        
        decryption_details['final_plaintext_binary'] = final_plaintext
        decryption_details['final_plaintext'] = self.binary_to_ascii(final_plaintext)
        
        return decryption_details

    def _apply_s_boxes(self, xor_result):
        """Apply S-box substitution"""
        # Split the 48-bit input into 8 groups of 6 bits
        six_bit_groups = [xor_result[i:i+6] for i in range(0, 48, 6)]
        
        # Apply S-box substitution
        s_box_substituted = ''
        for i in range(8):
            # Extract row and column bits
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)
            
            # Lookup S-box value
            s_box_value = self.s_boxes[i][row_bits][col_bits]
            
            # Convert to 4-bit binary
            s_box_substituted += format(s_box_value, '04b')
        
        return s_box_substituted