#open and read the list names ----> help: https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file
with open(r".\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

with open(r".\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace("[name]", name.strip())
        with open(f".\Output\ReadyToSend\letter_for_{name.strip()}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)