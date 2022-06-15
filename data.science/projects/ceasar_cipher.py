# Create a function to encrypt strings
def coder(message, offset=10):
    
    # Set all letter of the message to lowercase
    message = message.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Split each word from the encoded message and store it into a Python list
    words = message.split()
    
    words_coded = []

    # Iterate through each word of the message
    for word in words:

        coded_word = ""

        # Iterate through each letter of the word
        for letter in word:
            
            # If the letter IS in the alphabet
            if letter in alphabet:
                
                # Calculate a coded index to access the correct letter position based on the offset
                coded_index = alphabet.find(letter) - offset
                
                # Store the decoded letter based on the offset
                coded_letter = alphabet[coded_index]
                
            # If the letter IS NOT in the alphabet (when the message has symbols)
            elif letter not in alphabet:
                coded_letter = letter
                
            coded_word += coded_letter

        words_coded.append(coded_word)
    
    coded_message = " ".join(words_coded)
    return coded_message

# Create a function to decrypt a string
def decoder(message, offset=10):
    
    # Set all letter of the message to lowercase
    message = message.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Split each word from the encoded message and store it into a Python list
    words = message.split()
    
    words_decoded = []

    # Iterate through each word of the message
    for word in words:

        decoded_word = ""

        # Iterate through each letter of the word
        for letter in word:
            
            # If the letter IS in the alphabet
            if letter in alphabet:
                
                # Calculate a decoded index to access the correct letter position based on the offset
                decoded_index = alphabet.find(letter) + offset
                
                # If the decoded index is greater than the length of the alphabet...
                if decoded_index > 25:
                    
                    # Adjust the decoded index to start at the beginning of the alphabet
                    decoded_index = decoded_index - 26
                
                # Store the decoded letter based on the offset
                decoded_letter = alphabet[decoded_index]
                
            # If the letter IS NOT in the alphabet (when the message has symbols)
            elif letter not in alphabet:
                decoded_letter = letter
                
            decoded_word += decoded_letter

        words_decoded.append(decoded_word)
    
    decoded_message = " ".join(words_decoded)
    return decoded_message

print()

print("Welcome to Caesar's cipher!\nThis program will encrypt messages based on a shift number.")

print()

print("Each letter of the message will be replaced by another letter some fixed number of positions (offset) down the alphabet.")


# Ask user to input a message to begin cipher
input_message = input("Write a message to encrypt it: ")

input_offset = int(input("Choose the offset number: "))

print()

print(coder(input_message, input_offset))