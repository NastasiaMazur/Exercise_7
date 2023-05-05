#1
def create_file(file_name, names):
    with open(file_name, 'w') as file:
        file.write(','.join(names))

#Usage
create_file('names.txt', ['Ada, Alan, Isabella, Lizbeth, Abigail, Meltem, Gulcan'])


"""
def create_file(file_name):
    with open(file_name, 'w') as file:
        # Write the names to the file
        file.write('Ada, Alan, Isabella, Lizbeth, Abigail, Meltem, Gulcan')

#Usage
create_file('names.txt')
"""

#2
def transform_to_row(input_file, output_file):
    # Open in read mode
    with open(input_file, 'r') as input:
        # Read the contents
        contents = input.read()
        # Split the contents into a list of words
        words = contents.split(',')
    # Open the output file in write mode
    with open(output_file, 'w') as output:
        # Write each word to the output file on a new line
        for word in words:
            output.write(word.strip() + '\n')

#Usage:
transform_to_row('names.txt', 'output.txt')

#3
def add_greeting(input_file, output_file):

    with open(input_file, 'r') as input:
        # Read the contents of the file and split it into lines
        lines = input.readlines()

    # Add "Hello " in front of each word in the lines and split into words
    words = [f"Hello {name.strip()}" for line in lines for name in line.split(",")]

    # Open the output file in write mode
    with open(output_file, 'w') as output:
        # Write the new lines to the output file
        output.write("\n".join(words))

#Usage
add_greeting('output.txt', 'greetings.txt')

#4
def strip_greeting(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, 'r') as input:
        # Read the contents of the file and split it into lines
        lines = input.readlines()

    # Remove "Hello " from each line and join into a single string
    new_lines = [line.replace("Hello ", "") for line in lines]
    new_text = "".join(new_lines)

    # Open the output file in write mode
    with open(output_file, 'w') as output:
        # Write the new text to the output file
        output.write(new_text)
#Usage
strip_greeting('greetings.txt', 'output2.txt')

# I need 2 files for exercise 5: I created them manually


#5
def combine_files(file1, file2, output_file):

    # Open the input files in read mode
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Read the contents of the files and split them into lines
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Check that both files have the same number of lines
    if len(lines1) != len(lines2):
        raise ValueError("Files must have the same number of lines.")

    # Combine the lines from the input files and write to the output file
    with open(output_file, 'w') as out_f:
        for line1, line2 in zip(lines1, lines2):
            combined_line = f"{line1.strip()} {line2.strip()}\n"
            out_f.write(combined_line)

#Usage
combine_files('file1.txt', 'file2.txt', 'combined.txt')

