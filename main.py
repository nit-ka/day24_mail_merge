with open("./Input/Names/invited_names.txt") as name_list_file:
    names_list = name_list_file.readlines()
    names_list_stripped = []
    for name in names_list:
        name_stripped = name.strip("\n")
        names_list_stripped.append(name_stripped)

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    starting_letter_lines = starting_letter.readlines()
    first_line = starting_letter_lines[0]
    rest_of_letter = ''.join(starting_letter_lines[1:])

for name in names_list_stripped:
    updated_first_line = first_line.replace("[name]", name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as letter:
        letter.write(f"""{updated_first_line}{rest_of_letter}""")