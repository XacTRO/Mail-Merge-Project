#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

list_of_names = []
count = 1
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file_names:
    while True:
        count += 1
        line = file_names.readline()
        if not line:
            break
        list_of_names.append(line.strip())

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as file:
    start_line = file.readline()
    another_lines = []

    while True:
        line = file.readline()
        if not line:
            break
        another_lines.append(line)

    for names in list_of_names:
        with open(f"./Output/ReadyToSend/{names}.txt", "w") as new_file:
            new_line = start_line.replace("[name]", names)
            new_file.write(new_line)
            for lines in another_lines:
                new_file.write(lines)
            # letter_content = file.read()
            # new_file.write(letter_content)
            # first_lines = new_file.readline()
            # first_lines.replace("[name]", names)
