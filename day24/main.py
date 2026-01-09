#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




#read lines 
# f = open("demofile.txt", "r")
# print(f.readlines()) 
# can put optional number to stop at certain point 


#txt.replace
# txt = "I like bananas"

# x = txt.replace("bananas", "apples")

# print(x) - prints I like apples




# Remove spaces at the beginning and at the end of the string:
# txt = "     banana     "

# x = txt.strip()

# print("of all fruits", x, "is my favorite")  - will just have bananas


from pathlib import Path

name_list = []

#get list of names and store str as name_text
data_path = Path(__file__).parent / "Input/Names/invited_names.txt"

with open(data_path) as file:
    name_list_raw = file.readlines()

for name in name_list_raw:
    name_list.append(name.strip())

# print(name_list)


#get str of letter template as letter_template 
data_path = Path(__file__).parent / "Input/Letters/starting_letter.txt"

with open(data_path) as file:
    letter_template = file.read()




#generate new letter and create txt for each letter 
for name in name_list:

    data_path = Path(__file__).parent / f"Output/ReadyToSend/Letter_to_{name}.txt"
    with open(data_path, mode="w") as file:
        file.write(letter_template.replace("[name]", name))






# print(letter_template)
# print(name_text)

# with open("Input/Names/invited_names.txt") as file:
#     name_list = file.read()
#     print(name_list)



