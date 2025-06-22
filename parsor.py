"""
1. Recreate input file
    - read the file backward
    - put each line into a stack
    - popping the stack into new file

"""
import re

def read_file_backwards(file_path):
    stack1 = []  
    stack2 = []
    queue = []
    

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    i = len(lines) - 1
    while i >= 0:
        line = lines[i]
        stripped_line = line.strip()

        if stripped_line.startswith("END_") or " END_" in line:
            stack1.append(line)

            match = re.match(r"END_([A-Z]+)", stripped_line)
            if match:
                stack2.append(match.group(1))

        elif stack2 and stripped_line.startswith(stack2[-1]):
            section_type = stack2.pop()
            stack1.append(line)
            



        elif line == "                                                               ":
            strack.append(line)
        i -= 1


    with open('secret/new_file.txt', 'w', encoding='utf-8') as new_file:
        while stack1:
            new_file.write(stack1.pop())
            



if __name__ == "__main__":
    file_path = 'secret/file.L5K'
    read_file_backwards(file_path)




