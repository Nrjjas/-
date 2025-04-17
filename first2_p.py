english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def monoalphabetic_decrypt(cipher_text):
    
    cipher_text = cipher_text.upper()

    
    freq = Counter(char for char in cipher_text if char.isalpha())

    
    cipher_freq_order = ''.join([item[0] for item in freq.most_common()])

    
    decrypt_map = {cipher_letter: real_letter for cipher_letter, real_letter in zip(cipher_freq_order, english_freq_order)}

    
    decrypted_text = ''.join(decrypt_map.get(char, char) if char.isalpha() else char for char in cipher_text)
    
    return decrypted_text



cipher_text = input("Enter the ciphertext:\n")


print("\nDecrypted text:\n")
print(monoalphabetic_decrypt(cipher_text))