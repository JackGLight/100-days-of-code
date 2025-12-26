'''
Day 8: Caesar cipher
'''

"""list of lower case alphabet"""
import string
alphabet = list(string.ascii_lowercase)


"""codes the message based on message input, shift, and goes + or - depending on code type given """
def caesar(message, shift, code_type):
    coded_message = ""
    if code_type == "decode":
        switcher = -1
    else:
        switcher = 1
        
    for char in message:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift * switcher) % 26
            coded_message += (alphabet[new_index])
        else:
            coded_message += char

    return coded_message


"""Game will keep running until user opts to not press Y when prompted"""
keep_playing = "y"

print("Welcome to the Caesar cipher!\n")

while keep_playing == "Y".lower():


    while True:
        code_choice = input("Would you like to encode or decode a message?\n").lower()
        if code_choice in ("encode", "decode"):
            break
        print("Please type 'encode' or 'decode'.")

    user_message = input("Type your message:\n")

    while True:
        try:
            shift_num = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Please enter a valid integer.")

            
    result = caesar(message=user_message, shift=shift_num, code_type=code_choice)
    print(result)

    keep_playing = input("Type Y to do another cipher\n").lower()

print("Goodbye. Thanks for playing!")





