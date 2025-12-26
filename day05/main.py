'''
Day 5: Password generator program
'''


import string
import random

letters_list = []
numbers_list = []
symbols_list = []
password_list = []

"""grab applicable letters numbers and symbols for the password"""
letters = list(string.ascii_uppercase + string.ascii_lowercase)

digits = list(string.digits)

symbols = list(string.punctuation)

'''function to check if the letter num or symbol length is applicable'''
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a number 0 or greater.")
        except ValueError:
            print("Please enter a valid integer.")

'''choose random letters nums and symbols based on user input'''
def get_digits(nums, list_choice, base_list):
    for i in range(0, nums):
        list_choice.append(random.choice(base_list))



print("Welcome to the password generator!\n")

'''user input'''
letter_num = get_non_negative_int("How many letters do you want in your password?\n")
digit_num = get_non_negative_int("How many numbers do you want in your password?\n")
symbols_num = get_non_negative_int("How many symbols do you want in your password?\n")


'''call function to get digits and join lists together'''
get_digits(nums=letter_num, list_choice=letters_list, base_list=letters)
get_digits(nums=digit_num, list_choice=numbers_list, base_list=digits)
get_digits(nums=symbols_num, list_choice=symbols_list, base_list=symbols)
password_list = letters_list + numbers_list + symbols_list

'''randomize order of final list and convert it to a string'''
random.shuffle(password_list)
password = "".join(password_list)


'''output for user '''
print(f"The letters chosen: {letters_list}")
print(f"The numbers chosen: {numbers_list}")
print(f"The symbols chosen: {symbols_list}")
print(f"Complete password list: {password_list}")
print(f"Complete password: {password}")


